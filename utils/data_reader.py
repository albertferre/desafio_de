# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:58:50 2020

@author: alber
"""
import pandas as pd

class DataReader():

    def __init__(self):
        self.df = pd.DataFrame()
        #case when no file warning


    def _join_station_data(self, data, stations, join_station: str):
        PREFIX = '{}_station_'
        ON = '{}_station_code'
#        if station != 'start':
#            print('error')

        return data.merge(stations.add_prefix(PREFIX.format(join_station)),
                          how='inner',
                          on=ON.format(join_station))

    def _fetch_data(self,path_file):
        return pd.read_csv(path_file).drop(columns=['Unnamed: 0'])


    def _fetch_stations(self, path_file_stations):
        return pd.read_csv(path_file_stations)


    def _prepare_data(self, path_file, path_file_stations):
        data = self._fetch_data(path_file)
        stations = self._fetch_stations(path_file_stations)

        data = self._join_station_data(data, stations, 'start')
        data = self._join_station_data(data, stations, 'end')
        data['route'] = data['start_station_name'].astype(str) + ' -> '+ data['end_station_name']
        data['start_hour'] = data['start_date'].apply(lambda x: x[11:13])
        data['year'] = data['start_date'].str[0:4]
        return data

    def append_year_data(self, path_file, path_file_stations):
        self.df = self.df.append(self._prepare_data(path_file, path_file_stations))

    def get_data(self):
        return self.df

