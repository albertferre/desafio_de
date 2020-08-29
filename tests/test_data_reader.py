# -*- coding: utf-8 -*-
import unittest
import pandas as pd

from utils.data_reader import DataReader


class TestDataReader(unittest.TestCase):


    def test_reader(self):
        files_path = 'resources/tests/{}'
        data_file_path = files_path.format('OD_2014_sample.csv')
        stations_file_path = files_path.format('Stations_2014_sample.csv')
        d = DataReader()
        d.append_year_data(data_file_path,stations_file_path)
        df = d.get_data()

        data = pd.read_csv(data_file_path).drop(columns=['Unnamed: 0'])
        stations = pd.read_csv(stations_file_path)

        data = data.merge(stations.add_prefix('start_station_'),
                          how='inner',
                          on='start_station_code')

        data = data.merge(stations.add_prefix('end_station_'),
                          how='inner',
                          on='end_station_code')

        data['route'] = data['start_station_name'].astype(str) + ' -> '+ data['end_station_name']
        data['start_hour'] = data['start_date'].apply(lambda x: x[11:13])
        data['year'] = data['start_date'].str[0:4]

        df_expected = data
        self.assertEqual(df.equals(df_expected), True, "No equals")


