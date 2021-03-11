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

        lat_list =  [float(x.replace(",", ".")) for x in df['latitude'].values]
        lon_list = [float(x.replace(",", ".")) for x in df['longitude'].values]

        coordinates = []
        for i in range(len(lat_list)):
            coordinates.append((lat_list[i], lon_list[i]))

        line = fm.PolyLine(coordinates, color=best_colors[index], weight=8, opacity=1)
        line.add_to(map)

    for index, worst in enumerate(worst_filenames):
        try:
            df = pd.read_csv(worst, sep=";")
        except:
            print("Failed to open: ", worst)
            continue
    
        lat_list =  [float(x.replace(",", ".")) for x in df['latitude'].values]
        lon_list = [float(x.replace(",", ".")) for x in df['longitude'].values]

        coordinates = []
        for i in range(len(lat_list)):
            coordinates.append((lat_list[i], lon_list[i]))

        line = fm.PolyLine(coordinates,
                            color=worst_colors[index],
                            weight=8, opacity=1)
        line.add_to(map)

    map.save("Map.html")
    


