# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:58:50 2020

@author: alber
"""
import pandas as pd

class ReadData():
    def __init__(self,path_file: str = 'data/OD_2014.csv',path_file_stations: str = 'data/Stations_2014.csv'):
        #case when no file warning
        self.path_file = path_file
        self.path_file_stations = path_file_stations

    def _join_station_data(self, data, stations, join_station: str):
        PREFIX = '{}_station_'
        ON = '{}_station_code'
#        if station != 'start':
#            print('error')

        return data.merge(stations.add_prefix(PREFIX.format(join_station)),
                          how='inner',
                          on=ON.format(join_station))

    def _fetch(self):

        data = pd.read_csv(self.path_file,
                           index_col=0,
                           low_memory=False)
        stations = pd.read_csv(self.path_file_stations)

        return data, stations

    def _prepare_data(self):
        data, stations = self._fetch()

        data = self._join_station_data(data, stations, 'start')
        data = self._join_station_data(data, stations, 'end')
        data['route'] = data['start_station_name'].astype(str) + ' -> '+ data['end_station_name']
        return data

    def get_data(self):
        return self._prepare_data()