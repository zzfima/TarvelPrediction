import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression

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
# plt.show()

print(dataSet['vacation_preference'].describe())
# dataSet['vacation_preference'].value_counts().plot(kind='bar')
# plt.show()

# sns.pairplot(dataSet)
# plt.show()

# Model can work with numbers, but not a names
# Convert
# Wrong way - do enumeration
# For example:
# Krasnodar = 1, Tomsk = 2 etc.
# Why wrong? Model will consider that Tomsk = 2 * Krasnodar
# Right way - make columns of names
# For example:
# city_Krasnodar, city_Tomsk etc. Each column contains 0 or 1
# Model can get it in right way
# process name: One-Hot Encoding.
# One-hot uses for X ('salary', 'city', 'age' etc), for Y ('target') do not use
# One Hot Encoding is a process in the data processing that
# is applied to categorical data, to convert it into a binary vector representation
# for use in machine learning algorithms
print(pd.get_dummies(dataSet, columns=['city']))
modifiedDataSet = pd.get_dummies(dataSet, columns=[
    'city', 'vacation_preference', 'transport_preference'])

print(modifiedDataSet['target'].value_counts())

# Partitioning DataFrame into X and Y
X = modifiedDataSet.drop(axis=1, columns=['target'])
y = modifiedDataSet['target']
print(X.head())
print(y.head())

# LogisticRegression - classification algorithm
model = LogisticRegression()
model.fit(X, y)
# predict first row
print(model.predict(X.drop(X[X.index > 0].index)))
