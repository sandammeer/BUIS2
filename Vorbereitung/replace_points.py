import glob

import pandas as pd

for item in glob.glob("Ecosense\*.csv"):
    data = pd.read_csv(item)


    data = data.stack().str.replace(',', '.').unstack()

    data.to_csv(item)