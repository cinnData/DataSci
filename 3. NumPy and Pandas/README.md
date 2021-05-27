# 3. NumPy and Pandas

### NumPy arrays

In Mathematics, a **vector** is a sequence of numbers, and a **matrix** is a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In Python (and in many other languages), vectors are called one-dimensional (1d) **arrays**, while matrices are called two-dimensional (2d) arrays. Arrays of more than two dimensions can be managed in Python without pain.

Python arrays are not necessarily numeric. Indeed, vectors of dates and strings appear frequently in data science. In principle, all the terms of an ordinary array must have the same type, so that the array itself can have a type, although you can relax this constraint using mixed types, not covered by this course. Arrays were already implemented in plain Python, but the functionality of the Python arrays was enlarged in the NumPy library, intended to be the fundamental library for scientific computing in Python.

The usual way to load NumPy is:

`import numpy as np`

Arrays can then be created directly from lists with the function `np.array`. Two simple examples:

`arr1 = np.array(['a', 'b', 'c', 'd'])`

`arr2 = np.array([[2, 3, 1], [7, -3, 2.6]])`

An array has a collection of attributes, such as `ndim`, `shape` and `dtype`. They are extracted as `arr.attr`. So, `arr1.shape` will return `(10,)`, while `arr2.shape` will return `(2,4)`.

### NumPy functions

NumPy incorporates vectorized forms of the **mathematical functions** of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with same shape, whose terms are the values of the function on the corresponding terms of the original array. For instance, the square root function `np.sqrt` takes the square root of every term of a numeric array.

NumPy also provides common **statistical functions**, such as `mean`, `max`, `sum`, etc.

### Subsetting arrays

A slice of a 1d array is extracted as for a list. So, `myarr1[1:3]` would extract an array containing `'b'` and `'c'`. The same applies to 2d arrays, but we need two indexes within the square brackets. The first index selects the rows, and the second index the columns. Subarrays can also be extracted by means of expressions.

### The package Pandas

**Pandas** provides a wide range of data wrangling tools. It is typically imported as:

`import pandas as pd`

Pandas allows for two data container classes, the series (one-dimensional) and the data frames (two-dimensional).

A Pandas **series** can be understood as the combination of a 1d array containing the **values** and a list containing the row of the values, called the **index**. These two components can be extracted as the attributes `values` and `index`.

A **data frame** can be seen as formed by one or several series with the same index (hence, with the same length). It can be seen as a table for which the index provides the row names. In a Pandas data frame, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for many things, not only strings.

### Pandas series

You can store practically any data container in a series of type `object`: lists, dictionaries, etc. As an example, we can turn the 1d array `arr1` into a series:

`s1 = pd.Series(arr1)`

Here, `arr1` provides the values of the series, so `s1.values` would return an array exactly equal to `arr1`. The index is created automatically, as a numeric range, but we can replace this by our own choice. Example:

`s1.index = ['I', 'II', 'III', 'IV']`

There are many types of indexes. The first one, created automatically, would have been a `RangeIndex`, while the second one would be a plain `Index`. Indexes are useful for combining, filtering and joining data sets. The different types of indexes allow for specific operations, so do not look at them as an embarrassment, which is what they seem at first sight, but as a tool for data transformation.

### Pandas data frames

Data frames can be built directly, as in:

`df = pd.DataFrame(arr2)`

or extracted from a data source (local or remote), which can be a CSV file, and Excel sheet, a table from a relational database, etc. As for the series, a range index is automatically created unless an alternative definition is provided. The same is true for column names, so, in the above example, `df.columns` would return a range of integers. It is recommended to provide column names which are suggestive of the content of the column.

Columns can be extracted from a data frame by naming them:

* `df[colname]` returns the column `colname` as a Pandas series.

* `df[[colname1, colname2, . . .]]` returns a data frame containing the columns specified. Note that  `df[colname]` is a series, while `df[[colname]]` is a data frame with one column, which is not the same thing.
