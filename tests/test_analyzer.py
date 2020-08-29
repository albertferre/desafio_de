# -*- coding: utf-8 -*-
import unittest
import pandas as pd

from utils.analyzer import Analyzer

class TestStringMethods(unittest.TestCase):

    def _list_generator(self, elements, repetitions):
        return [ele for i, ele in enumerate(elements) for j in range(repetitions[i])]

    def _get_mock_data(self):
        repetitions = list(range(10,0,-1))
        city_start_names = ['city_start_' + str(n) for n in range(1,11)]
        city_end_names = ['city_end_' + str(n) for n in range(1,11)]
        route = ['route_' + str(n) for n in range(1,11)]
        d = {'duration_sec': self._list_generator(list(range(1,11)), repetitions),
             'start_station_name': self._list_generator(city_start_names, repetitions),
             'end_station_name': self._list_generator(city_end_names, repetitions),
             'route': self._list_generator(route, repetitions),
             'year': '2014'}
        return pd.DataFrame(data=d)

    def test_top_start_stations(self):
        an = Analyzer(self._get_mock_data())
        df = an.top_start_stations('2014')
        self.assertEqual(list(df.recuento),
                         [10,9,8,7,6,5,4,3,2,1],
                         "Incorrect results")
        self.assertEqual(list(df.index),
                         ['city_start_' + str(n) for n in range(1,11)],
                         "Incorrect results")


    def test_top_end_stations(self):
        an = Analyzer(self._get_mock_data())
        df = an.top_end_stations('2014')
        self.assertEqual(list(df.recuento),
                         [10,9,8,7,6,5,4,3,2,1],
                         "Incorrect results")
        self.assertEqual(list(df.index),
                         ['city_end_' + str(n) for n in range(1,11)],
                         "Incorrect results")

    def test_top_routes_stations(self):
        an = Analyzer(self._get_mock_data())
        df = an.top_routes('2014')
        self.assertEqual(list(df.recuento),
                         [10,9,8,7,6,5,4,3,2,1],
                         "Incorrect results")
        self.assertEqual(list(df.index),
                         ['route_' + str(n) for n in range(1,11)],
                         "Incorrect results")
#        an.top_routes(2014)
#        df = self.get_mock_data()
#        an = Analyzer(df)
#        self.assertEqual(an.top_routes(2014).values[0], 2853, "Should be 2853")
#        self.assertEqual(an.top_routes(2014).values[0], 2853, "Should be 2853")
#        self.assertEqual( 2853, 2853, "Should be 2853")

