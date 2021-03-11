from idlelib import tooltip

import folium as fm
import pandas as pd
import random


map = fm.Map(location=[53.14998528073779, 8.18176724453504], zoom_start=15)

def visualize_ranking(best, worst):
    best_filenames = best["Filename"]
    worst_filenames = worst["Filename"]

    best_colors = ["cadetblue", "blue", "darkblue"]
    worst_colors = ["purple", "orange", "red"]

    for index, best in enumerate(best_filenames):
        try:
            df = pd.read_csv(best, sep=";")
        except:
            print("Failed to open: ", best)
            continue

        lat_list =  [float(x) for x in df['latitude'].values]
        lon_list = [float(x) for x in df['longitude'].values]

        coordinates = []
        for i in range(len(lat_list)):
            coordinates.append((lat_list[i], lon_list[i]))


        line = fm.PolyLine(coordinates, color=best_colors[index], weight=7, opacity=1)
        line.add_to(map)

    for index, worst in enumerate(worst_filenames):
        try:
            df = pd.read_csv(worst, sep=";")
        except:
            print("Failed to open: ", worst)
            continue
    
        lat_list =  [float(x) for x in df['latitude'].values]
        lon_list = [float(x) for x in df['longitude'].values]

        coordinates = []
        for i in range(len(lat_list)):
            coordinates.append((lat_list[i], lon_list[i]))
        df = pd.read_csv("Index.csv")
        df = df[df['Filename'] == worst]
        values = df.values
        speed = str(round(values[0][4],2))
        vibration = str(round(values[0][2],2))
        distance = str(round(values[0][3],2))
        line = fm.PolyLine(coordinates,
                            color=worst_colors[index],
                            weight=7, opacity=1, popup="<i>vibration: "+vibration+ "<br/>speed: "+speed+"<br/>distance: "+ distance+"</i>")
        line.add_to(map)

    fm.Marker([53.146867706791234, 8.18312897559883], popup="<i>Carl von Ossietzky Universität Oldenburg</i>", tooltip=tooltip).add_to(map)
    map.save("Map.html")
    


