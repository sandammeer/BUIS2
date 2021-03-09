import pandas as pd


def dataframe_from_csv_file(path):
    data = pd.read_csv(path, sep=';', index_col=0)
    data = data.stack().str.replace(',', '.').unstack()
    return data