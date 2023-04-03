## [DS-03] NumPy and Pandas ##

# NumPy arrays #
import numpy as np
arr1 = np.array([2, 7, 14, 5, 9])
arr1
arr2 = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
arr2
arr1.shape
arr2.shape

# NumPy functions #
np.sqrt(arr1)
def f(t): return 1/(1 + np.exp(t))
f(arr2)

# Subsetting arrays #
arr1[:3]
arr2[:1, 1:]
arr1 > 3
arr2 > 2
arr1[arr1 > 3]
arr1[[False,  True,  True,  True,  True]]
arr2[arr2[:, 0] > 0, :]

# Pandas series #
import pandas as pd
s1 = pd.Series(arr1)
s1
s1.values
s1.index
s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
s2
s2.index

# Pandas data frames #
df = pd.DataFrame({'v1': range(5),
    'v2': ['a', 'b', 'c', 'd', 'e'],
    'v3': np.repeat(-1.3, 5)})
df
df.values
df.index
df.columns
pd.DataFrame(arr2)

# Exploring Pandas objects #
df.head(2)
df.info()
df.describe()

# Subsetting in Pandas #
df['v2']
df[['v1', 'v2']]
df[df['v1'] > 2]
df[df['v1'] > 2]['v2']
