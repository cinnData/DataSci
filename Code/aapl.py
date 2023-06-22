## Example - Apple Inc. stock prices ##

# Q1. Import the data with date index #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'aapl.csv'
df = pd.read_csv(filename, index_col=0, parse_dates=True)
df.info()
df.index
df.index.name = None
df.head()
df['open'].plot(figsize=(8,5), color='black');

# Q2. Data previous to January 15th #
df[:'2019-01-14']

# Q3. Data for Fridays #
df[df.index.day_name() == 'Friday'].head()
df[df.index.day_name('ca_ES') == 'Divendres'].head()
df[df.index.weekday == 4].head()

# Q4. Distribution of daily returns #
returns = df['open'].pct_change()
returns.head()
returns.plot(figsize=(7,5), color='black');
returns.plot.hist(figsize=(7,5), color='gray', edgecolor='white');

# Q5. Plot weekly average opening price #
w_open = df['open'].resample('W').mean()
w_open.head()
w_open.plot(figsize=(8,5), color='black');

# Q6. 5-day moving average trend #
df['open'].rolling(5).mean().head(10)
ma = df['open'].rolling(5, center=True).mean()
ma.head(10)
ma.plot(figsize=(8,5), color='black', linestyle='--')
df['open'].plot(color='gray');
