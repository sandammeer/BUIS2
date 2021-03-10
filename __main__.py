import glob
import importlib
import os
from datetime import datetime
import pandas as pd


# add imports here
reader_module = importlib.import_module("read_csv")
distance_module = importlib.import_module("distance_calc")
speed_module = importlib.import_module("speed_calc")
quality_module = importlib.import_module("streetQuality")
writer_module = importlib.import_module("write_index")
relevance_module = importlib.import_module("relevant_streets")
visualizer_module = importlib.import_module("visualizer_module")


def create_index_from_ecosensedata():
    start_time = datetime.now()

    for filename in glob.glob("Ecosense/*.csv"):
        print(filename)
        if os.path.exists('Index.csv'):
            index_df = pd.read_csv("Index.csv")
            if filename in index_df.values:
                print("Skipping: ", filename)
                continue

        if relevance_module.uni_street_in_route(filename):
            print("Relevant: ", filename)
            df = reader_module.dataframe_from_csv_file(filename)
            quality = quality_module.street_quality_from_data_frame(df)
            speed = speed_module.calc_speed(df)
            avg_speed = speed[0]
            distance = distance_module.calc_distance(df)

            writer_module.write_to_index(filename, quality.mean_distances, distance, avg_speed, True)
        else:
            print("Not relevant: ", filename)
            writer_module.write_to_index(filename, 0.0, 0.0, 0.0, False)

    duration = datetime.now() - start_time 
    print("Dauer: ", duration)


def create_ranking_from_index():
    df_index = pd.read_csv("Index.csv", index_col=0)
    df_index["Filename"] = df_index["Filename"].str.replace("\\", "/")

    df_relevant = df_index[df_index["Relevant"] == True]
    df_relevant = df_relevant[df_relevant["Distance"] > 800.0]
    df_relevant = df_relevant[df_relevant["Distance"] < 1000000.0]
    df_relevant = df_relevant.round(0)

    df_sorted_by_street = df_relevant.sort_values(by=["Mean_Street_Quality", "Speed"], ascending=(True, False))  
    df_sorted_by_street.to_csv("Ranking.csv")
    return

def get_best_3_routes():
    df_ranking = pd.read_csv("Ranking.csv", index_col=0)
    return df_ranking.head(3)

def get_worst_3_routes():
    df_ranking = pd.read_csv("Ranking.csv", index_col=0)
    return df_ranking.tail(3)

def combine_index():
    names = ["Index_Rafael.csv", "Index_Dennis.csv", "Index_Sandro.csv"]
    df = pd.DataFrame()

    for name in names:
        input_df = pd.read_csv(name, index_col=0)
        df = df.append(input_df, ignore_index=True)
    df.to_csv("Index.csv")

if __name__ == "__main__":
    # create_index_from_ecosensedata()
    create_ranking_from_index()
    best_routes = get_best_3_routes()
    worst_routes = get_worst_3_routes()

    # combine_index()
    visualizer_module.visualize_ranking(best_routes, worst_routes)