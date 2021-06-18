# 10. Time series data in Python

### Date and datetime

In computer environments, we typically find two **time data types**, called `date` and `datetime` (or `timestamp`). In type `date` we store dates, that is, year, month and day. Software applications for data management and analysis can deal with different date formats. The default format for dates in most languages, including Python, is `yyyy-mm-dd`. I advise you to use this format wherever. Under the hood, a variable of type `date` is just a number, the number of days since a time origin, which is, typically, `1970-01-01` (in particular in Python).

In data of type `datetime`, we also store hour, minute and second. The preferred format is `yyyy-mm-dd hh:mm:ss`. In some languages, an indication of the time zone is added at the end. Examples are CET (Central European Time), CEST (Central European Summer Time), GMT (Greenwich Mean Time) and UTC (Coordinated Universal Time). A datetime is the number of seconds since the time origin.

Data of type `datetime` can be managed in many ways in Python. The package `datetime` is recommended for dealing with times one by one. The functions `datetime.date` and `datetime.datetime` can be used to create dates and datetimes. The dates are just datetimes in disguise, that is, the date `1954-04-30` is the same as the datetime `1954-04-30 00:00:00`.

The old date and datetime types became obsolete when the type `datetime64` was introduced in NumPy. In this data type, times are recorded down to the nanosecond. So, a `datetime64` is just the number of nanoseconds since the time origin. 

Pandas inherits the type `datetime64` from NumPy. Just as Pandas incorporates vectorized versions of many string functions, as `s.str.fname`, it also incorporates vectorized versions of time functions, as `s.dt.fname`. For instance, if `s` is a series of type `datetime64`, we can use `s.dt.weekday` to get the weekday as a number (in Python, Monday = 0, Sunday = 6), or `s.dt.month` to get the month as a number (January = 1, December = 12).

### Datetime indexes in Pandas

Dates and times can be used as the index of a Pandas data frame. Many time series methods which use data in Pandas format rely on the time information in the index to provide time series functionality. There are three types of indexes specific for that: `DatetimeIndex`, `TimedeltaIndex` and `PeriodIndex`. In addition to this three, `IntervalIndex` can be used in certain situations.

Your index will be a `DatetimeIndex` in most cases. The data to build the index will be probably included in your data source, as one of the columns, but, if this were not the case, you can create an appropriate index with the Pandas function `date_range`. For an index of type `PeriodIndex`, you can use the function `period_range`.

Suppose that your data source is a CSV file, and that one of the columns contains dates. You can import these data to a Pandas data frame `df`, with the dates as the index, by means of the argument `index_col` of the Pandas function `read_csv`. Then, the argument `parse_dates=True` converts to dates the column taken as the index. 

A data index can be used to select rows, as a plain index. For instance, `df[:'2019-01-08']` would select the data up to January 8th, 2019 (included). Note that the selection is not based on the order of the index values in the data frame, but on the dates themselves.

The structure of the index also helps to select the data in special ways. For instance, to select the Friday's data, you can apply the function `day_name` to the index, as in `df[df.index.day_name() == 'Friday']`. Or, to select the February data, you can use `df[df.index.month == 2]`. 

### Resampling time series data

Often you need to summarize or aggregate time series data by a new time period. For instance, you may want to summarize hourly data as a daily maximum value. Changing the time period to the one data are summarized for is often called **resampling**.

There is a nice method `resample`, designed for Pandas data frames with a `Datetime` index. This method is a special case of `groupby`, driven by the index. For instance, `df.resample('M').mean()` returns the monthly average of the data in `df`.

### Rolling windows in Pandas

The logic of `rolling` is similar to that of `resampling`, but it groups the rows around every value of the index (except at the extremes). The set of these groups is called a **rolling window**. For instance, `df[cname].rolling(5).mean()` would extract a **moving average** (MA) trend for a specific column (moving average is a popular name for the rolling mean). As a default, the terms included in the rolling window are collected leftwards.
