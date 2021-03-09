import glob

import geocoder as geocoder
import pandas as pd

from geopy.geocoders import Nominatim

from geopy import distance

from geopy import Point

uni_routes = []
uni_streets = ['Ammerländer Heerstraße', 'Uhlhornsweg', 'Haarenfeld', 'Schützenweg', 'Artillerieweg', 'Wechloyer Weg', 'Quellenweg']
geolocator = Nominatim(user_agent="test_app")
def uni_street_in_route(path):

    data = pd.read_csv(path, sep=';')
    values = data.values

    '''
    for index in range(len(values)):
        print(type(index))
        item = values[index] if values % 2 == 0 else values[len(values) - index]
        print(type(item))
        co1 = str(item['latitude']) + ", " + str(item['longitude'])

    '''
    for index, row in data.iterrows():
        if index % 2 != 0:
            row = data.iloc[len(values) - index]
        if index >= len(values)/2:
            print('durch', index, len(values))
            return False
        co1 = str(row['latitude']) + ", " + str(row['longitude'])  # critical: the order has to be lat, lon

        point = Point(co1)
        result = geolocator.reverse(point)
        result_address = result.raw['address']
        result_road = result_address['road']
        print(result_road)
        if result_road in uni_streets:
            return True

    return False

def search_all_routes():
    counter = 0
    for item in glob.glob("Ecosense\*.csv"):
        print(item)
        if uni_street_in_route(item):
            uni_routes.append(item)
        counter += 1
        if counter > 2:
            print('done')
            return uni_routes
    return uni_routes

print(search_all_routes())
#uni_street_in_route("Ecosense/bikeride-gps-2dde982a4f5acf1a4c06c5d004cefc75cfeed173.csv")