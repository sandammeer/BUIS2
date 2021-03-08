import numpy as np
import pandas as pd
import glob

gyro_sum = 0
count = 0
for item in glob.glob("Ecosense\*.csv"):
    df = pd.read_csv("Ecosense\\bikeride-gps-0aad2d83b1bef753c6223006240d4b730ffc755e.csv", sep=";")

    array = np.arange(start=1, stop=24)
    for i in array:
        if (i < 10):
            number = "0" + str(i)
        else:
            number = str(i)

        x = df["gyro_x_" + number].astype('float').to_numpy()

        x = np.absolute(x)

        y = df["gyro_y_" + number].astype('float').to_numpy()
        y = np.absolute(y)
        z = df["gyro_z_" + number].astype('float').to_numpy()
        z = np.absolute(z)

        count = count + len(x) + len(y) + len(z)
        gyro_sum = gyro_sum + x.sum() + y.sum() + z.sum()

avg_gyro = gyro_sum / count
print(gyro_sum)
print(count)
print(avg_gyro)
