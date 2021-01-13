import pandas as pd

dataSet = pd.read_excel('trips_data.xlsx', index_col=0)
print(dataSet.head())
print(dataSet.columns)
print(dataSet.describe())
print(dataSet.info())
