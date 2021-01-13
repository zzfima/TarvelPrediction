import matplotlib.pyplot as plt
import pandas as pd

dataSet = pd.read_excel('trips_data.xlsx', index_col=0)
print(dataSet.head(), '\n')
print(dataSet.columns, '\n')
print(dataSet.info(), '\n')

print('All desc:\n', dataSet.describe(), '\n')
print('salary desc:\n', dataSet.salary.describe(), '\n')
dataSet.salary.hist()
plt.show()
