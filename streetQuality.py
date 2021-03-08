import pandas as pd
import numpy as np


class StreetQuality:
    mean: float
    mean_difference: float
    distances: [float]
    mean_distances: float

    def __init__(self, mean, distances):
        self.mean = mean
        self.distances = distances
        self.mean_distances = np.mean(distances)
        self.mean_difference = abs(self.mean - self.mean_distances)


def street_quality_from_data_frame(df):
    '''
    the function calculates the street quality of the route
    :param route: dataframe of one bicycle route
    :return: street quality object
    '''
    # cast values to float
    sensor_df = df[get_sensor_names()].astype(float)
    #sum gyro values in row
    gyro_sums = [np.sum(row) for row in sensor_df.values]

    return StreetQuality(mean = np.mean(gyro_sums),
                         distances = [abs(x - mean) for x in gyro_sums])

def get_sensor_names():
    '''
    internal helper function
    :return: column names -> gyro_x_01 ... gyro_z_24
    '''
    #array 1 to 24 wih leading zeros
    numbers = ["".join(["0", str(number)]) if number <10 else str(number) for number in np.arange(24) + 1]
    # column names from gyro_x_01 to gyro_z_24
    gyro_names = [ ["gyro_" + axis + "_" + n for n in numbers] for axis in ["x", "y", "z"] ]
    return gyro_names