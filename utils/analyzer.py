# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class analyzer():

    def __init__(self, df):
        self.df = df

#    def histograms():

    def top_N(self, column_names, n=10):
#        table = df.
        table = self.df[column_names]
        table = pd.Series(table.squeeze().values.ravel()).value_counts()[:10]
#        table = table.apply(pd.value_counts)[:10]
        table.plot.bar()
        return table

    def top_start_stations(self, year):
        return self.top_N(['start_station_name'])

    def top_end_stations(self, year):
        return self.top_N(['end_station_name'])

    def top_stations(self, year):
        return self.top_N(['start_station_name','end_station_name'])

    def top_routes(self, year):
        return self.top_N(['route'])



#    def use_hour()