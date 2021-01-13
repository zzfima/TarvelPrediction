import matplotlib.pyplot as plt
import pandas as pd

dataSet = pd.DataFrame(pd.read_excel('trips_data.xlsx', index_col=0))
print(dataSet.head(), '\n')
print(dataSet.columns, '\n')
print(dataSet.info(), '\n')

print('All desc:\n', dataSet.describe(), '\n')
print('salary desc:\n', dataSet['salary'].describe(), '\n')
# dataSet['salary'].hist()
# plt.show()

print('age desc:\n', dataSet['age'].describe(), '\n')
# dataSet['age'].hist()
# plt.show()

print('city desc:\n', dataSet['city'].describe(), '\n')
print(dataSet['city'].value_counts(), '\n')
# dataSet['city'].hist(xrot=90)
# plt.show()

dataSet['city'].value_counts().plot(kind='bar')
plt.subplots_adjust(bottom=0.3)
plt.show()
