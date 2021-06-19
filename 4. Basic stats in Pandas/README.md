# 4. Basic stats in Pandas

### Importing data from CSV files

Data sets in tabular form can be imported as Pandas data frames from many file formats. In particular, CSV files are imported to data frames with the function `read_csv`. The syntax is `dfname = pd.read_csv(fname)`. The data frame name is chosen by the user, and the file name has to contain the **path** of that file (either local or remote).

Although defaults work in most cases satisfactorily, it is worth to comment a few things about some arguments of `read_csv`. The list is not complete, but you can guess the extent to which you can customize this function.

* `sep` specifies the column separator. The default is `sep=','`, but CSV files created with Excel may need `sep=';'`.

* `header` and `names` specify the row where the data start and the column names. The default is `header=0, names=None`, which makes Pandas start reading from the first row and take it as the column names. When the data come without names, you can use {`header=0, names=namelist` to provide a list of names. With a positive value for `header`, you can skip some rows.

* `index_col` specifies a column that you wish to use as the index, if that is the case. The default is `index_col=None`. If the index comes in the first column, you use `index_col=0`.

* `usecols` specifies the columns to be read. You can specify them in a list, either by name or by position. The default is `usecols=None`, which means that you wish to read all the columns. 

* `dtype` specifies the data types of the columns of the data frame. This saves a lot of time with big data sets. The default is `dtype=None`, which means that Python will guess the data type, based on what it reads. When all the entries in a column are numbers, that column is imported as numeric. If there is, at least, one entry that is not numeric, it is read as strings, and type `object` is assigned.

* `encoding`. If the string data contained in a CSV file can contain special characters (such as \~n, or \'a), which can make trouble, I recommend you to set the argument as `encoding='utf-8'`, which is the default in Python.

### Summary statistics

The function `describe` returns a conventional statistical summary. Columns of type `object` are omitted, except when all the columns have that type. Then the report contains only counts. This function also works for series.

Basic statistics can also be calculated separately. For instance, `df.mean()` returns the means of the columns of `df`. Correlations are also pretty easy:

* `s1.corr(s2)` returns the correlation of `s1` and `s2`.

* `df.corr()` returns the correlation matrix for the columns of `df`.

### Plotting

We typically visualize the data with bar plots, histograms, scatter plots and line plots. They can be obtained directly from a Pandas object. 

Suppose first that `df` is a Pandas data frame and let `cname1` be the *x*-column and `cname2` the *y*-column (numeric). To explore the dependence of the *y*-column on the *x* column, we use a **bar plot**, when the *x*-column is categorical, and a **scatter plot**, when it is numeric:

* `df.plot.bar(x=cname1, y=cname2)` returns a bar plot. The bars represent the values of `cname2` for the different values of `cname1`. If you do not specify the *x*-column, the index is used instead.

* `df.plot.scatter(x=cname1, y=cname2)` returns a scatter plot.

Suppose now that `s` is a numeric Pandas series. To explore the distribution of `s`, you use a **histogram**. Alternatively, to explore a trend, you use a **line plot**. This is pretty easy in Pandas:

* `s.plot.hist()` returns a histogram.

* `s.plot.line()` returns a line plot.

Pandas uses the Matplotlib functions, but this is not explicit. If you are satisfied with a basic functionality, you can skip Matplotlib in your code. If you want to add labels, titles, or other features, you can import `matplotlib.pyplot` and add code lines for labels, title, legends, etc. 
