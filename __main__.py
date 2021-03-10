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
    return

def visualize_ranking():
    return


if __name__ == "__main__":
    create_index_from_ecosensedata()
    create_ranking_from_index()
    visualize_ranking()