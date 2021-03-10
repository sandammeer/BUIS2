import pandas as pd
from pandas import DataFrame, read_csv
from geopy import distance
from geopy import Point

def calc_distance(route):
    '''
    the function calculates the distance between every recorded location and adds them to a total distance

    :param route: dataframe of one bicycle route
    :return: distance driven in the span of the one recorded route
    '''
    dist = 0.0
    co1 = ""
    co2 = ""
    for index, row in route.iterrows():
        if co1 == "":
            co1 = str(row['latitude']) + " " + str(row['longitude']) #critical: the order has to be lat, lon
        else:
            co2 = str(row['latitude']) + " " + str(row['longitude'])
            dist = dist + distance.distance(Point(co1), Point(co2)).m
            co1 = co2
    return dist
