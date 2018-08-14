# -*- coding: utf-8 -*-
__author__ = 'aditya'

from math import sin, cos, sqrt, atan2, radians


class CabFare:

    def distance_from_lat_lon(self, lat1, lon1, lat2, lon2):

        R = 6373.0
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def fare_calculation(self, lat1, lon1, lat2, lon2, cab_type):
        distance = CabFare.distance_from_lat_lon(lat1, lon1, lat2, lon2)
        if cab_type == 1:
            base
        return total_fare