# Cheatsheet - Pandas

## Pandas methods for series

* `s.astype()`: changes the data type, if possible.

* `s.count()`: counts the non-missing terms of a series.

* `s.cumsum()`: returns a series containing the cumulative sums of the terms of a series.

* `s.describe()`: returns a statistical summary. The `NaN` values are ignored.

* `s.diff()`: returns a series containing the differences between consecutive terms, with a `NaN` value on top.

* `s.drop_duplicates()`: removes the duplicated values.

* `s.dropna()`: removes the missing values.

* `s.drop(lst)`: removes the values listed.

* `s.dtype`: returns the data type.

* `s.duplicated()`: returns a Boolean series indicating duplicated values.

* `s.fillna(value)`: fills missing values with a user-provided value.

* `s.head()`: returns the first terms of a series.

* `s.index`: returns the index of a series, as an object of type `Index` (not just one type, but a family). 

* `s.isna()`: returns a Boolean series indicating missing values.

* `s.max()`: returns the maximum of the terms of a series.

* `s.mean()`: returns the mean of the terms of a numeric series.

* `s.min()`: returns the minimum of the terms of a series.

* `s.pct_change()`: returns a series with the proportion changes between consecutive terms, with a `NaN` on top.

* `s.plot()`: the same as `s.plot.line()`.

* `s.plot.bar()`: displays a vertical bar plot of a numeric series, using the index as the labels in the horizontal axis.

* `s.plot.barh()`: displays a horizontal bar plot of a numeric series, using the index as the labels in the vertical axis.

* `s.plot.hist()`: displays a histogram of a numeric series.

* `s.plot.line()`: displays a line plot of a numeric series.

* `s.sample(n)`: extracts a random sample of size `n` of a series. 

* `s.shape`: returns the length of a series.

* `s.shift(k)`: shifts `k` places the terms of a series, filling the holes with `NaN` values. `k` can be negative.

* `s.sort_index()`: sorts a series by the index.

* `s.sort_values()`: sorts a series by its values.

* `s.tail()`: returns the last terms of a series.

* `s.to_frame()`: converts a series to a data frame with one column.

* `s.sum()`: returns the sum of the terms of a numeric series.

* `s.value_counts()`: counts the unique values of a series.

* `s.values`: converts a series to a 1D array.

## Pandas methods for data frames

* `df1.append(df2)`: appends `df2` after the last row of `df1`. 

* `df.apply(func)`: aggregates the columns of a data frame with an aggregation function.

* `df.columns`: returns the column names.

* `df.count()`: counts the rows that have at least a non-missing term.

* `df.cumsum()`: replaces the columns by the corresponding cumulative sums. For the string columns the sum is interpreted as concatenation.

* `df.describe()`: returns a statistical summary of the numeric columns of a data frame.

* `df.drop(lst)`: drops from the columns specified.

* `df.drop_duplicates()`: removes duplicated rows.

* `df.dropna()`: removes rows with at least on missing value.

* `df.dtypes`: returns the column data types.

* `df.duplicated()`: returns a Boolean series indicating the duplicated rows.

* `df.fillna(value)`: fills the missing values with a user-provided value.

* `df.head()`: returns the first rows of a data frame.

* `df.index`: returns the index of  a data frame, as an object of type `Index` (not just one type, but a family). 

* `df.info()`: prints a report of the contents of a data frame.

* `df.isna()`: returns a Boolean data frame indicating missing values.

* `df1.join(df2)`: a simplified version of the method `.merge()`. Merges two data frames, or a series to a data frame, based on the index. It is practical for adding new columns to a data frame. 

* `df.mean()`: returns the means of the numeric columns of a series.

* `df1.merge(df2)`: merges two data frames. The default is an inner join (to include the rows common to both tables) based on the columns that have the same name in the two data frames. A collection of parameters allow for various options.

* `df.plot.bar(x, y)`: displays a vertical bar plot of a numeric column (`y`) by a categorical column (`x`).

* `df.plot.bar(x, y)`: displays a vertical bar plot of a numeric column (`y`) by a categorical column (`x`).

* `df.plot.barh(x, y)`: displays a horizontal bar plot of a numeric column (`y`) by a categorical column (`x`).

* `df.plot.scatter(x, y)`: displays a scatter plot, with `x` in the horizontal axis and `y` in the vertical axis. 

* `df.sample(n)`: extracts a random sample of `n` rows of a data frame.

* `df.set_index(col)`: sets the specified column as the index.

* `df.shape`: returns the numbers or rows and columns as a tuple.

* `df.sort_index()`: sorts the rows of a data frame by the index.

* `df.sort_values(lst)`: sorts the rows of a data frame by the columns specified.

* `df.squeeze()`: converts a data frame with one column to a series.

* `df.sum()`: returns the column totals of a data frame. For the string columns the sum is interpreted as concatenation.

* `df.tail()`: returns the last rows of a data frame.

* `df.to_csv(file)`: exports data from a data frame to a CSV file. If the file already exists, the previous version is overwritten.

* `df.values`: converts a data frame to a 2D array with the same values, coercing data types if necessary.

## Pandas functions

* `pd.concat(lst)`: concatenates the data frames specified. With `axis=0` (the default), the frames are concatenated vertically. With `axis=1`, horizontally. Horizontal concatenation is not just pasting the two matrices together, but a join based on the index (the same as `.join()`).

* `pd.crosstab()`: cross tabulation of two or more vector-like objects.

* `pd.DataFrame(dict)`: converts a dictionary whose values are the vector-like objects of the same length to a data frame. The keys of the dictionary are taken as the column names. 

* `pd.pivot_table()`: returns a 1-way or 2-way pivot table.

* `pd.read_csv(file)`: imports data from a CSV file to a data frame. 

* `pd.Series(v)`: converts a vector-like object to a Pandas series.
