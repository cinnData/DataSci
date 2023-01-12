# [DS-03T] Tutorial - NumPy and Pandas

## NumPy arrays

This tutorial presents some simple examples of NumPy and Pandas data containers, so you can get familiar with the different ways in which data sets can be managed in Python. In NumPy, vectors are called one-dimensional (1D) **arrays**, and matrices are called two-dimensional (2D) arrays. Arrays of more than two dimensions can be managed without pain. 

A typical way to import NumPy is:

```
In [1]: import numpy as np
```

A 1D arrays can be created from a list with the NumPy function `array`. If the items of the list have different type, they are converted to a common type when creating the array. A simple example follows.

```
In [2]: arr1 = np.array([2, 7, 14, 5, 9])
   ...: arr1
Out[2]: array([ 2,  7, 14,  5,  9])
```

A 2D array can be directly created from a list of lists of equal length. The terms are entered row-by-row:

```
In [3]: arr2 = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
   ...: arr2
Out[3]: 
array([[ 0,  7,  2,  3],
       [ 3,  9, -5,  1]])
```

Although we visualize a vector as a column (or as a row) and a matrix as a rectangular arrangement, with rows and columns, it is not so in the computer. The 1D array is just a sequence of elements of the same type, neither horizontal nor vertical. It has one **axis**, which is the 0-axis.

In a similar way, a 2D array is a sequence of 1D arrays of the same length and type. It has two axes. When we visualize it as rows and columns, `axis=0` means *across rows*, while `axis=1` means *across columns*.

The number of terms stored along an axis is the **dimension** of that axis. The dimensions are collected in the attribute `shape`.

```
In [4]: arr1.shape
Out[4]: (5,)
```

```
In [5]: arr2.shape
Out[5]: (2, 4)
```

## NumPy functions

NumPy incorporates vectorized forms of the mathematical functions of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with same shape, whose terms are the values of the function on the corresponding terms of the original array. For instance, the NumPy square root function takes the square root of every term of a numeric array.

```
In [6]: np.sqrt(arr1)
Out[6]: array([1.41421356, 2.64575131, 3.74165739, 2.23606798, 3.        ])
```

The functions that are defined in terms of vectorized functions are automatically vectorized. For instance:

```
In [7]: def f(t): return 1/(1 + np.exp(t))
   ...: f(arr2)
Out[7]: 
array([[5.00000000e-01, 9.11051194e-04, 1.19202922e-01, 4.74258732e-02],
       [4.74258732e-02, 1.23394576e-04, 9.93307149e-01, 2.68941421e-01]])
```

## Subsetting arrays

**Subsetting** a 1D array is done as for a list:

```
In [8]: arr1[:3]
Out[8]: array([ 2,  7, 14])
```

The same applies to 2D arrays, but we need two indexes within the square brackets. The first index selects the rows (`axis=0`), and the second index the columns (`axis=1`):

```
In [9]: arr2[:1, 1:]
Out[9]: array([[7, 2, 3]])
```

When an expression involving an array is evaluated by the Python kernel, a Boolean array with the same shape is returned:

```
In [10]: arr1 > 3
Out[10]: array([False,  True,  True,  True,  True])
```

```
In [11]: arr2 > 2
Out[11]: 
array([[False,  True, False,  True],
       [ True,  True, False, False]])
```

A subarray can be extracted by means of an expression. The expression is evaluated, returning a Boolean array called **Boolean mask**. The terms for which the mask is true are selected: 

```
In [12]: arr1[arr1 > 3]
Out[12]: array([ 7, 14,  5,  9])
```

Note that this is the same as

```
In [13]: arr1[[False,  True,  True,  True,  True]]
Out[13]: array([ 7, 14,  5,  9])
```

Boolean masks can also be used to filter out rows or columns of a 2d array. For instance, you can select the rows of `arr2` for which the first column is positive,

```
In [14]: arr2[arr2[:, 0] > 0, :]
Out[14]: array([[ 3,  9, -5,  1]])
```

## Pandas series

**Pandas** is typically imported as

```
In [15]: import pandas as pd
```

Pandas provides two data container types, series (one-dimensional) and data frames (two-dimensional). A **series** is composed of a 1D array of **values** and a list containing the names of the values of the series, called the **index**. These two components can be extracted as the attributes `values` and `index`.

Let me illustrate this with a simple example. To get it, I'll create directly a short series, something you rarely do in data science, where the data are imported from external data files. But a Pandas series can be created directly, for instance from an array, with the Pandas function `Series`:

```
In [16]: s1 = pd.Series(arr1)
    ...: s1
Out[16]: 
0     2
1     7
2    14
3     5
4     9
dtype: int64
```

Now, the values of the series are extracted as:

```
In [17]: s1.values
Out[17]: array([ 2,  7, 14,  5,  9])
```

As shown above, when a series is printed, the index appears on the left. Since the index of `s1` has not been specified, a range of consecutive integers has been assigned as the index.

```
In [18]: s1.index
Out[18]: RangeIndex(start=0, stop=5, step=1)
```

Instead of an array, a list can be used to provide the values of a series. In the list, the items can have different type, but Pandas converts them to a common type, as shown in the following example. Now, instead of leting Python to create an index automatically, as a `RangeIndex`, I specify an index directly:

```
s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
s2
Out[19]: 
a        1
b        5
c    Messi
dtype: object
```

Now the index is a plain `Index`:

```
In [20]: s2.index
Out[20]: Index(['a', 'b', 'c'], dtype='object')
```

## Pandas data frames

A Pandas **data frame** can be seen as a collection of series with the same index (hence, with the same length). Data frames can be built in many ways with the Pandas function `DataFrame`, for instance from a dictionary of vector-like objects of the same length, as in

```
In [21]: df = pd.DataFrame({'v1': range(5),
    ...:     'v2': ['a', 'b', 'c', 'd', 'e'],
    ...:     'v3': np.repeat(-1.3, 5)})
    ...: df
Out[21]: 
   v1 v2   v3
0   0  a -1.3
1   1  b -1.3
2   2  c -1.3
3   3  d -1.3
4   4  e -1.3
```

As the series, the data frames have the attributes `values` and `index`: 

```
In [22]: df.values
Out[22]: 
array([[0, 'a', -1.3],
       [1, 'b', -1.3],
       [2, 'c', -1.3],
       [3, 'd', -1.3],
       [4, 'e', -1.3]], dtype=object)
```

```
In [23]: df.index
Out[23]: RangeIndex(start=0, stop=5, step=1)
```

Without a explicit specification, the index is automatically created as a `RangeIndex`. In this example, since the columns have different data types, `df.values` takes `object` type. The third component of the data frame is a list with the column names, which can be extracted as the attribute `columns`:

```
In [24]: df.columns
Out[24]: Index(['v1', 'v2', 'v3'], dtype='object')
```

A data frame has the same shape of the array of values. Having rows and columns, a data frame looks like a 2D array with row and column names. Indeed, we can also create data frames in this way:

```
In [25]: pd.DataFrame(arr2)
Out[25]: 
   0  1  2  3
0  0  7  2  3
1  3  9 -5  1
```

But not all data frames are so simple. While a NumPy 2D array has a data type, in a Pandas data frame every column has its own data type.

## Exploring Pandas objects

The functions `head` and `tail` extract the first and the last rows of a data frame, respectively. The default number of rows extracted is 5, but you can pass a custom number.

```
In [26]: df.head(2)
Out[26]: 
   v1 v2   v3
0   0  a -1.3
1   1  b -1.3
```

The content of a data frame can also be explored with the function `info`. It reports the dimensions, the data type and the number of non-missing values of every column of the data frame. Note that the data type of the second column, for which you would have expected `str`, is reported as `object`. Don't worry about this, you can apply string functions to this column, as will be seen later in this course. 

```
In [27]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   v1      5 non-null      int64  
 1   v2      5 non-null      object 
 2   v3      5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes
```

The function `describe` returns a conventional statistical summary. The columns of type `object` are omitted, except when all the columns have that type. Then the report contains only counts. This function also works for series.

```
In [28]: df.describe()
Out[28]: 
             v1   v3
count  5.000000  5.0
mean   2.000000 -1.3
std    1.581139  0.0
min    0.000000 -1.3
25%    1.000000 -1.3
50%    2.000000 -1.3
75%    3.000000 -1.3
max    4.000000 -1.3
```

##  Subsetting data frames

Pandas offers multiple ways for subsetting data frames. First, you can extract a column, as a series:

```
In [29]: df['v2']
Out[29]: 
0    a
1    b
2    c
3    d
4    e
Name: v2, dtype: object
````

You can also extract a **data subaframe** containing a subset of complete columns from a data frame. You can specify this with a list containing the names of those columns:

```
In [30]: df[['v1', 'v2']]
Out[30]: 
   v1 v2
0   0  a
1   1  b
2   2  c
3   3  d
4   4  e
```

*Note*. You can extract a subframe with a single column. Beware that this is not the same as a series. `df['v2']`is a series with shape `(5,)`, and `df[['v2']]` is a data frame with shape `(5,1)`.

In data science, rows are typically filtered by expressions. Example:

```
In [31]: df[df['v1'] > 2]
Out[31]: 
   v1 v2   v3
3   3  d -1.3
4   4  e -1.3
```

Combining a row filter and a column selection:

```
In [32]: df[df['v1'] > 2][['v1', 'v2']]
Out[32]: 
   v1 v2
3   3  d
4   4  e
```

