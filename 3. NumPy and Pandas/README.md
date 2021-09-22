# 3. NumPy and Pandas

### NumPy arrays

In Mathematics, a **vector** is a sequence of numbers, and a **matrix** is a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In Python (and in many other languages), vectors are called one-dimensional (1d) **arrays**, while matrices are called two-dimensional (2d) arrays. Arrays of more than two dimensions can be managed in Python without pain.

Python arrays are not necessarily numeric. Indeed, vectors of dates and strings appear frequently in data science. In principle, all the terms of an ordinary array must have the same type, so the array itself can have a type, although you can relax this constraint using mixed types, not covered by this course. Arrays were already implemented in plain Python, but the functionality of the Python arrays was enlarged in the NumPy library, intended to be the fundamental library for scientific computing in Python.

The usual way to import NumPy is:

`import numpy as np`

Arrays can be created directly from lists with the NumPy function `array`. Two simple examples:

`arr1 = np.array(['a', 'b', 'c', 'd'])`

`arr2 = np.array([[2, 3, 1], [7, -3, 2.6]])`

An array has a collection of attributes, such as `ndim`, `shape` and `dtype`. They are extracted as `arr.attr`. For instance, `arr1.shape` would return `(4,)`, while `arr2.shape` will return `(3,3)`.

### NumPy functions

NumPy incorporates vectorized forms of the **mathematical functions** of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with the same shape, whose terms are the values of the function on the corresponding terms of the original array. For instance, the square root function `np.sqrt` takes the square root of every term of a numeric array.

NumPy also provides common **statistical functions**, such as `mean`, `max`, `sum`, etc.

### Subsetting arrays

Slicing works in 1d arrays as in lists. For instance, `arr1[1:3]` would extract an array containing `'b'` and `'c'`. The same applies to 2d arrays, but we need two indexes within the square brackets. The first index selects the rows, and the second index the columns.

Subarrays can also be extracted by means of expressions. For instance, the first row of `arr2` can be extracted with:

`arr2[arr2[:, 1] > 0, :]`

This is easier to manage in Pandas data frames, where rows and columns have names, than in NumPy 2d arrays. So, there is more detail below.

### The package Pandas

**Pandas** provides a wide range of data wrangling tools. It is typically imported as:

`import pandas as pd`

Pandas allows for two data container classes, the series (one-dimensional) and the data frames (two-dimensional).

A Pandas **series** can be understood as the combination of a 1d array containing the **values** and a list containing the names of the values, called the **index**. These two components can be extracted as the attributes `values` and `index`.

A **data frame** can be seen as formed by one or several series with the same index (hence, with the same length). It can be seen as a table for which the index provides the row names. In a Pandas data frame, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for many things, not only strings.

### Pandas series

You can create a series from any Python data container: lists, dictionaries, etc. As an example, we can turn the 1d array `arr1` into a series:

`s1 = pd.Series(arr1)`

Here, `arr1` provides the values of the series, so `s1.values` would return an array exactly equal to `arr1`. The index is created automatically, as a numeric range, but we can replace this by your own choice. Example:

`s1.index = ['I', 'II', 'III', 'IV']`

There are many types of indexes. The first one, created automatically, would have been a `RangeIndex`, while the second one would be a plain `Index`. Indexes are useful for combining, filtering and joining data sets. The different types of indexes allow for specific operations, so do not look at them as an embarrassment, which is what they seem at first sight, but as a tool for data transformation.

### Pandas data frames

Data frames can be built directly, as in:

`df = pd.DataFrame(arr2)`

They can also be extracted from a data source (local or remote), which can be a CSV file, an Excel sheet, a table from a relational database, etc. This will be the case in most of the examples of this course. As for the series, a range index is automatically created unless an alternative definition is provided. The same is true for column names, so, in the above example, `df.columns` would return a range of integers. It is recommended to choose column names which are suggestive of the content of the column.

Columns can be extracted from a data frame by naming them:

* `df[colname]` returns the column `colname` as a Pandas series.

* `df[[colname1, colname2, . . .]]` returns a data frame containing the columns specified. Note that `df[colname]` is a series, while `df[[colname]]` is a data frame with one column, which is not the same thing.

### Exploring Pandas objects

There are many ways to explore a Pandas object:

* The functions `head` and `tail` extract the first and the last rows of either a series or a data frame, respectively (default is 5 rows).

* The content of a data frame can be explored with the function `info`. It reports the dimensions, the data type and the number of non-missing values of every column of the data frame.

### Subsetting in Pandas

Pandas offers multiple ways for subsetting series and data frames. We have already seen how to select one or several columns. Rows are typically selected with a filtering condition, or based on the row numbers, as in 2d arrays. For instance, the same selection that we made in `arr2` can be done in the associate data frame as

`df[df[1] > 0]`

Besides these simple methods, there are two additional ways to carry out a selection:

* **Selection by label** is specified by adding  `.loc` after the name of the data frame. The selection of the rows is based on the index, and that of the columns is based on the column names.

* **Selection by position** uses `.iloc`. The selection of the rows is based on the row number and that of the columns on te column number.

In both cases, if you enter a single specification inside the brackets, it refers to the rows. If you enter two specifications, the first one refers to the rows and the second one to the columns. We don't use much `loc` and `iloc` in this course, since you can live in Pandas without that, selecting first the rows and then the columns.

*Note*. Special methods for Pandas objects with date indexes will be explained later in this course.
