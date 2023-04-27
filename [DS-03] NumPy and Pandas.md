# [DS-03] NumPy and Pandas

## NumPy arrays

In mathematics, a **vector** is a sequence of numbers, and a **matrix** is a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In Python (and in many other languages), vectors are called one-dimensional (1D) **arrays**, while matrices are called two-dimensional (2D) arrays. Arrays of more than two dimensions can be managed in Python without pain.

Python arrays are not necessarily numeric. Indeed, vectors of dates and strings appear frequently in data science. In principle, all the terms of an ordinary array must have the same type, so the array itself can have a type, though you can relax this constraint using mixed types (not covered by this course). Arrays were already implemented in plain Python, but the functionality of the Python arrays was enlarged in **NumPy**, intended to be the fundamental library for scientific computing in Python.

The usual way to import NumPy is:

```
In [1]: import numpy as np
```

A 1D array can be created from a list with the NumPy function `array`. If the items of the list have different type, they are converted to a common type when creating the array. A simple example follows.

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

NumPy incorporates vectorized forms of the **mathematical functions** of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with the same shape, whose terms are the values of the function on the corresponding terms of the original array.

For instance, the square root function `np.sqrt` takes the square root of every term of a numeric array:

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
NumPy also provides common **statistical functions**, such as `mean`, `max`, `sum`, etc.

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

## The package Pandas

**Pandas** provides a wide range of data wrangling tools. It is typically imported as

```
In [15]: import pandas as pd
```

Pandas provides two data container classes, the series (one-dimensional) and the data frames (two-dimensional). A **series** can be understood as the combination of a 1D array containing the **values** and a list containing the names of the values, called the **index**. These components can be extracted as the attributes `values` and `index`.

A **data frame** can be seen as formed by one or several series with the same index (hence, with the same length). It can also be seen as a table for which the index provides the row names. In a Pandas data frame, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for many things, in particular for strings.

## Pandas series

Although we rarely do it in data science, where the data are imported from external data files, a Pandas series can be created directly, for instance from an array, with the Pandas function `Series`:

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

Instead of an array, a list can be used to provide the values of a series. In the list, the items can have different type, but Pandas converts them to a common type, as shown in the following example. Here, instead of letting the Python kernel to create an index automatically, as a `RangeIndex`, we specify an index directly:

```
In [19]: s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
    ...: s2
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

Indexes are useful for combining, filtering and joining data sets. There are many types of indexes, which allow for specific operations. So, do not look at the index as an embarrassment, which is what it seems at first sight, but as a tool for data management.

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

Data frames can also be extracted from a data source (local or remote), such as a CSV file, an Excel sheet, or a table from a relational database. As for the series, a range index is automatically created unless an alternative specification is provided. The same is true for column names, so, in the above example, `df.columns` returns a range of integers. It is recommended to choose a column name which suggests the content of the column.

## Exploring Pandas objects

The methods `head` and `tail` extract the first and the last rows of a data frame, respectively. The default number of rows extracted is 5, but you can pass a custom number.

```
In [26]: df.head(2)
Out[26]:
   v1 v2   v3
0   0  a -1.3
1   1  b -1.3
```

The content of a data frame can also be explored with the method `info`. It reports the dimensions, the data type and the number of non-missing values of every column of the data frame. Note that the data type of the second column, for which you would have expected `str`, is reported as `object`. Don't worry about this, you can apply the string methods to this column, as will be seen later in this course.

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

The method `describe` extracts a conventional statistical summary of a Pandas object. The columns of type `object` are omitted, except when all the columns have that type. Then the report contains only counts. 

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

## Subsetting data frames

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

Note that the syntax is the same as for extracting the value of a key from a dictionary (not by chance). You can also extract a **data subaframe** containing a subset of complete columns from a data frame. You can specify this with a list containing the names of those columns:

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

Besides this, there are two additional ways to carry out a selection, specifying rows and columns in one shot:

* **Selection by label** is specified by adding  `.loc` after the name of the data frame. The selection of the rows is based on the index, and that of the columns is based on the column names.

* **Selection by position** uses `.iloc`. The selection of the rows is based on the row number and that of the columns on the column number.

In both cases, if you enter a single specification inside the brackets, it refers to the rows. If you enter two specifications, the first one refers to the rows and the second one to the columns. We don't use `loc` and `iloc` in this course, since you can live in Pandas without that, selecting first the rows and then the columns. Sticking to this simple approach, you will save the time wasted learning too many methods.

## Homework

For `x = np.array([True, False])` and `y = np.array([True, True])`, calculate `~x`, `x & y` and `x | y`. What is the meaning of these operations?
