# NumPy and Pandas

### NumPy arrays

In Mathematics, a **vector** is a sequence of numbers, and a **matrix** is a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In Python (and in many other languages), vectors are called one-dimensional (1d) **arrays**, while matrices are called two-dimensional (2d) arrays. Arrays of more than two dimensions can be managed in Python without pain.

Python arrays are not necessarily numeric. Indeed, vectors of dates and strings appear frequently in data science. In principle, all the terms of an ordinary array must have the same type, so that the array itself can have a type, although you can relax this constraint using mixed types, as we will see later. Arrays were already implemented in plain Python, but the functionality of the Python arrays was enlarged in the NumPy library, intended to be the fundamental library for scientific computing in Python.

A typical way to load NumPy is:

`import numpy as np`

Arrays can then be created directly from lists with the function `np.array`. Two simple examples:

`myarr1 = np.array(['a', 'b', 'c', 'd'])`

`myarr2 = np.array([[2, 3, 1], [7, -3, 2.6]])`

An array has a collection of attributes, such as `ndim`, `shape` and `dtype`. They are extracted as `arr.attr`.

### NumPy functions

NumPy incorporates vectorized forms of the mathematical functions of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with same shape, whose terms are the values of the function on the corresponding terms of the original array. For instance, the square root function `np.sqrt` takes the square root of every term of a numeric array. It also provides common **statistical functions**, such as `mean`, `max`, `sum`, etc.

### Subsetting arrays

A slice of a 1d array is extracted as for a list. So, `myarr1[1:3]` would extract an array containing `'b'` and `'c'`. The same applies to 2d arrays, but we need two indexes within the square brackets. The first index selects the rows, and the second index the columns. Subarrays can also be extracted by means of expressions.

### The package Pandas

**Pandas** provides a wide range of data wrangling tools. It typically imported as:

`import pandas as pd`

Pandas allows for two data container classes, Pandas allows for two data container classes, the series (one-dimensional) and the data frames (two-dimensional). An individual data vector is called a **series**. A series is like one-dimensional array plus the **index**, which contains the names of the values of the series.

A **data frame** is formed by one or several series with the same index (hence, with the same length). It can be seen as a two-dimensional array plus the column names and the index, which contains the row names. A difference between two-dimensional NumPy arrays and Pandas data frames is that a data frame does not have a data type, each column has its own data type.

### Pandas series

A Pandas series has three important attributes: `shape`, `dtype` and `index`. The first one indicates the length of the series. The numeric types work as usual, but Pandas uses the data type `object` for many things, not only strings. You can store practically any data container in a series of type `object`: lists, dictionaries, etc.

The index of a series is a vector-like object that contains the names of the terms of the series. Besides the plain `Index`, there are many types of indexes, such as `RangeIndex`, and `DatetimeIndex`. Indexes are useful for combining, filtering and joining data sets. The different types of indexes allow for specific operations, so do not look at them as an embarrassment, which is what they seem at first sight, but as a tool for data transformation.
