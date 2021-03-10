import pandas as pd
import os 
import importlib


reader = importlib.import_module("read_csv")
index_filename = "Index.csv"


def write_to_index(filename: str, 
                   mean_street_quality: float,
                   distance: float, 
                   speed: float,
                   relevant: bool):
    
    new_data = {"Filename": filename, 
                "Mean_Street_Quality": mean_street_quality, 
                "Distance": distance, 
                "Speed": speed, 
                "Relevant": relevant}
    original_data = {"Filename": [filename], 
                    "Mean_Street_Quality": [mean_street_quality], 
                    "Distance": [distance], 
                    "Speed": [speed], 
                    "Relevant": [relevant]}
    
    if os.path.exists(index_filename):
        df = pd.read_csv(index_filename, index_col=0)
        df = pd.concat([df, pd.DataFrame.from_dict(original_data)], ignore_index=True, sort=False)
    else:
        df = pd.DataFrame(original_data) 

    df.to_csv(index_filename)


# For Review

 #if __name__ == "__main__":
    
 #    write_to_index(
  #       filename="test.csv",
   #      mean_street_quality=10.0,
    #     distance= 10.0,
     #    speed=10.0,
      #   relevant=True
     #)