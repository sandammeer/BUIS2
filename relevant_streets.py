import glob
from datetime import datetime
import pandas as pd
from geopy.geocoders import Nominatim
from geopy import Point

uni_routes = []
uni_streets = ['Ammerländer Heerstraße', 'Uhlhornsweg', 'Haarenfeld', 'Schützenweg', 'Artillerieweg', 'Wechloyer Weg',
               'Quellenweg','Ofener Str.','Heiligengeistwall','Theaterwall','Carl-von-Ossietzky-Straße','Im Technologiepark',
               'Tuchtweg','Binsenstraße','Prinzessinweg','Drögen-Hasen-Weg','Grotepool','Küpkersweg','Pophankenweg','Gabelsbergerweg','Franz-Poppe-Straße','Westerstraße','Rummelweg','Zeughausstraße']
geolocator = Nominatim(user_agent="test_app")
def uni_street_in_route(path):

    data = pd.read_csv(path, sep=';')
    values = data.values


    for index, row in data.iterrows():
        if index % 10 == 1:
            row = data.iloc[len(values) - index]
        elif index % 10 == 0:
            row = row
        else:
            continue
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
    print(datetime.now())
    for item in glob.glob("Ecosense\*.csv"):
        print(item)
        if uni_street_in_route(item):
            uni_routes.append(item)
        counter += 1
        if counter > 5:
            print('done')
            return uni_routes
    return uni_routes

print(search_all_routes())
print(datetime.now())
#uni_street_in_route("Ecosense/bikeride-gps-2dde982a4f5acf1a4c06c5d004cefc75cfeed173.csv")