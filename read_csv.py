import pandas as pd


def dataframe_from_csv_file(path):
    data = pd.read_csv(path, sep=';')
    #data = data.stack().str.replace(',', '.').unstack()
    return data