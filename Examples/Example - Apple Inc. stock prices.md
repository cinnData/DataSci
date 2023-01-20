# Example - Apple Inc. stock prices

## Introduction

This example is based on data on the Apple Inc. stock prices in the Nasdaq stock market, for the year 2019, as published by Yahoo Finance. These data are used to illustrate the time series methods provided by the Python package Pandas.

## The data set

The data set (file `aapl.csv`) covers 251 trading days. The data come in the typical OHLC format (Open/High/Low/Close).

The variables are:

* `date`, the date, as `'yyyy-mm-dd'`.

* `open`, the price (US dollars) of the stock at the beginning of the trading day. It can be different from the closing price of the previous trading day.

* `high`, the highest price (US dollars) of the stock on that trading day.

* `low`, the lowest price (US dollars) of the stock on that day.

* `close`, the price (US dollars) of the stock at closing time.

* `adj_close`, the closing price adjusted for factors in corporate actions, such as stock splits, dividends, and rights offerings.

* `volume`, the amount of Apple stock that has been traded on that day.

Source: `finance.yahoo.com/quote/AAPL/history?p=AAPL`.

## Questions

Q1. Import the data to a Pandas data frame in such a way that the dates became the index of the data frame, in a `DatetimeIndex` format.

Q2. Use that index to extract the data for the trading days previous to January 15th. 

Q3. Extract the data for the trading days which are Fridays.

Q4. The **daily return** is the percentage change in the price with respect to the preceding trading day. If $p(t)$ is the price on day $t$, the corresponding return would be

$$r(t) =\frac{p(t) - p(t-1)}{p(t-1)}=\frac{p(t)}{p(t-1)}-1,$$

which can multiplied by 100 to get percentage scale. How is the distribution of the daily return of the opening price?

Q5. Plot the weekly average opening price.

Q6. Extract a nonparametric trend for the opening price, based on a 5-day moving average. Plot it together with the opening price.