# -*- coding: utf-8 -*-
__author__ = 'aditya'

from math import sin, cos, sqrt, atan2, radians
import decimal
import datetime

class CabFare:

    def distance_from_lat_lon(self, lat1, lon1, lat2, lon2):

        R = 6373.0
        lat1 = radians(decimal.Decimal(lat1))
        lon1 = radians(decimal.Decimal(lon1))
        lat2 = radians(decimal.Decimal(lat2))
        lon2 = radians(decimal.Decimal(lon2))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return decimal.Decimal(distance)


    def time_between_pickup_drop(self, pickup_time, drop_time):

        diff = datetime.datetime.fromtimestamp(int(drop_time)) - datetime.datetime.fromtimestamp(int(pickup_time))
        diff_in_sec = int(drop_time) - int(pickup_time)
        time_obj = {
            'total_hours':  int(diff_in_sec/3600),
            'total_days': diff.days
        }
        return time_obj

    def fare_calculation(self, fare_obj):
        distance = CabFare().distance_from_lat_lon(fare_obj["pickup_lat"], fare_obj["pickup_lon"], fare_obj["drop_lat"],
                                                   fare_obj["drop_lon"])
        time_obj = CabFare().time_between_pickup_drop(fare_obj['pickup_time'], fare_obj['drop_time'])
        cab_obj = {
            '1': "monthly_rental",
            '2': "sight_seening",
            '3': "luxury",
            '4': "outstation",
            '5': "self_drive",
            '6': "hire_driver",
        }
        for key in fare_obj:
            fare_obj[key] = 0 if fare_obj[key] == None else fare_obj[key]
        cab_type = fare_obj["cab_type"]
        fare = getattr(CabFare(), cab_obj.get(cab_type))(fare_obj, distance, time_obj)
        tax = fare * 0.05
        total_fare = fare + tax
        booking_obj = {
            'total_fare': round(total_fare, 2),
            'tax': round(tax, 2),
            'total_hours': time_obj["total_hours"],
            'total_days': time_obj['total_days'],
            'distance': round(distance, 2)
        }
        return booking_obj

    def monthly_rental(self, fare_obj, distance, time_obj):
        fare = float(2*distance * fare_obj.get("base_fare")*30)
        return fare

    def sight_seening(self, fare_obj, distance, time_obj):
        if fare_obj.get("slab") < time_obj["total_hours"] and fare_obj.get("slab") != 0:
            fare = float(fare_obj.get("base_fare"))
        else:
            fare = None
        return fare

    def luxury(self, fare_obj, distance, time_obj):
        if fare_obj.get("slab") < time_obj["total_hours"] and fare_obj.get("slab") != 0:
            fare = float(fare_obj.get("base_fare"))
        else:
            fare = None
        return fare

    def outstation(self, fare_obj, distance, time_obj):
        fare = float((distance - fare_obj.get("initial_km")) * fare_obj.get("base_fare") + fare_obj.get("initial_km") * \
                     fare_obj.get("initial_km_fare") + fare_obj.get("driver_daily_allowance_charge") * \
                     time_obj.get("total_days"))
        return fare

    def self_drive(self, fare_obj, distance, time_obj):
        fare = float(time_obj.get("total_hours") * fare_obj.get("base_fare"))
        return fare

    def hire_driver(self, fare_obj, distance, time_obj):
        if fare_obj.get("one_way"):
            fare = float((fare_obj.get("driver_per_hr_allowance_charge") * time_obj.get("total_hours")) + fare_obj.get(
                "different_pickup_drop_point_charge"))
        else:
            fare = float(fare_obj.get("driver_per_hr_allowance_charge") * time_obj.get("total_hours"))
        return fare