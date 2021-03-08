import pandas as pd
import os 


def write_to_index(filename: str, 
                   mean_street_quality: float,
                   distance: float, 
                   speed: float,
                   relevant: bool):
    data = {
        "Filename": [filename],
        "Mean_Street_Quality": [mean_street_quality],
        "Distance": [distance],
        "Speed": [speed],
        "Relevant": [relevant]
    }

    df = None
    if os.path.exists("Index.csv"):
        # read csv
        # append data to df
        print("todo")
    else:     
        df = pd.DataFrame(data)

    df.to_csv("Index.csv")


if __name__ == "__main__":
    print("test")
    write_to_index(
        filename="test.csv",
        mean_street_quality=10.0,
        distance= 10.0,
        speed=10.0,
        relevant=True
    )