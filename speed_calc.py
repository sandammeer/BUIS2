import pandas as pd
import numpy as np

def calc_speed(df):
    avg = np.mean(df['speed'])
    maximum = np.max(df['speed'])
    minimum = np.min(df['speed'])

    return [avg, maximum, minimum]
