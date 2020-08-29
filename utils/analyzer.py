# -*- coding: utf-8 -*-
import pandas as pd

class Analyzer():

    def __init__(self, df):
        self.df = df

#    def histograms():

    def top_N(self, column_names, year, plot=False, n=10, sort_index=False):
#        table = df.
        table = self.df[self.df.year == year]
        table = table[column_names]
        table = pd.Series(table.squeeze().values.ravel()).value_counts()
        if sort_index:
            table.sort_index(inplace=True)
        table = table[:n]
#        table = table.apply(pd.value_counts)[:10]
        if plot:
            table.plot.bar()
        return pd.DataFrame(table, columns=['recuento'])


    def top_start_stations(self, year, plot=False):
        return self.top_N(['start_station_name'], year, plot)


    def top_end_stations(self, year, plot=False):
        return self.top_N(['end_station_name'], year, plot)


    def top_stations(self, year, plot=False):
        return self.top_N(['start_station_name','end_station_name'], year, plot)


    def top_routes(self, year, plot=False):
        return self.top_N(['route'], year, plot)


    def top_hours(self, year, plot=False):
        return self.top_N(['start_hour'], year, plot, sort_index=True,n=24)


    def travel_time_hist(self,year, plot=False):
        self.df['duration_sec'].hist()


    def year_comparison(self, year_1, year_2):
        table_year1 = self.df[self.df.year == year_1]
        total_services_year_1 = table_year1['start_date'].count()
        total_hours_year_1 = table_year1['duration_sec'].sum() / 3600

        table_year2 = self.df[self.df.year == year_2]
        total_services_year_2 = table_year2['start_date'].count()
        total_hours_year_2 = table_year2['duration_sec'].sum() / 3600

        services_differences = total_services_year_1 - total_services_year_2
        hours_differences = total_hours_year_1 - total_hours_year_2

        print(f'El año {year_1} se hicieron {services_differences} servicios y '
              f'{int(hours_differences)} horas de servicio en comparación a {year_2}')

        return services_differences, hours_differences

#    def use_hour()
