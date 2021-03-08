import numpy as np
import pandas as pd
import csv

#path="../Ecosense/bikeride-gps-0aad2d83b1bef753c6223006240d4b730ffc755e.csv"

def readCsvFiles(path):
    data = (pd.read_csv(path, sep=';'))
    return data


#print(readCsvFiles("Ecosense/bikeride-gps-5d49d8db2c913a4631c46f77380b67052def385e.csv"))