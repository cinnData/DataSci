# 5. Querying data in Pandas

### Sorting

Pandas series can be sorted by index or by values, with the functions `sort_index` and `sort_values`, respectively. Both work for data frames, but, for the second one, you have to specify either the name of a column or a list of column names, which will be then used in the order that you write them.

The argument `ascending` allows you to choose between ascending and descending ways. The default ordering (in Python as in other languages) is `ascending=True`.

### Missing values

**Missing values** are denoted by `NaN` in Pandas. When a Pandas object is built, both plain Python's `None` and NumPy's `nan` are taken as `NaN`. Since `np.nan` had type `float`, a numeric series containing `NaN`'s gets type `float`. 

Three useful Pandas functions related to missing values, which can be applied to both series and data frames, are: 

* `isna` returns a Boolean mask indicating which terms are missing.

* `fillna` is used for **imputation**, that is, for replacing `NaN`'s by a fixed value, set by the user.

* `dropna` returns the same data frame minus the rows that contain at least one missing value. A list of columns can be specified, so the missing are searched only for those columns.

### Duplicates

There are two useful Pandas functions for managing **duplicates**:

* `drop_duplicates` drops the duplicated entries (in a series) or the duplicated rows (in a data frame).

* `duplicated` returns a Boolean series indicating which entries (for a series) or which rows (for a data frame) are duplicated.

### Grouping and aggregation

Exploring data, we often use tables. They can be produced in various ways in Pandas:

* `value_counts` extracts a table of counts as a series. For a Pandas series `s`, the syntax is `s.value_counts()`. This returns a table containing the counts of the occurrences of every value of `s`. It does not include the missing values.

* `crosstab` extracts a simple cross tabulation as a Pandas data frame. For a pair of series of the same length `s1` and `s2`, the syntax is `pd.crosstab(s1, s2)`. Then `s1` will be placed on the rows and `s2` on the columns. By default, `crosstab` extracts a frequency table, unless an array of values and an aggregation function are passed, eg as `values=s3` and `aggfunc=fname`.

* `pivot_table` extracts a spreadsheet-style pivot table as a data frame. For a Pandas data frame `df`, the syntax is `pd.pivot_table(df, values=cname1, index=cname2)`. This returns a one-way table containing the average value of `cname1` for the groups defined by `cname2`. Instead of the average, you can get a different summary by adding an argument `aggfunc=fname`. With an additional argument `columns=cname3`, you get a two-way table. For two-way tables, it works the same as `crosstab`, but it only applies to columns from the same data frame.

* `groupby` groups the rows of a data frame so that an aggregation function can be applied, extracting a SQL-like table as a data frame. For a Pandas data frame `df`, the syntax could be `df.groupby(by=cname).mean()`. This will return a data frame with the average value of the numeric columns of `df` for the groups defined by `cname`.
