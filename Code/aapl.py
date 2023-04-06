## Example - Apple Inc. stock prices ##

# Q1. Import the data with date index #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'aapl.csv'
df = pd.read_csv(filename, index_col=0, parse_dates=True)
df.info()
df.index
df.index.name = None
df['open'].plot(figsize=(10,6), color='black', linewidth=1);

# Q2. Data previous to January 15th #
df[:'2019-01-14']

# Q3. Data for Fridays #
df[df.index.day_name() == 'Friday'].head()
df[df.index.day_name('ca_ES') == 'Divendres'].head()
df[df.index.weekday == 4].head()

# Q4. Distribution of daily returns #
returns = df['open'].pct_change()
returns
returns.plot(figsize=(10,6), color='black', linewidth=1);
returns.plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Q5. Plot weekly average opening price #
w_open = df['open'].resample('W').mean()
w_open.head()
w_open.plot(figsize=(10,6), color='black', linewidth=1);

# Q6. 5-day moving average trend #
df['open'].rolling(5).mean().head(10)
ma = df['open'].rolling(5, center=True).mean()
ma.head(10)
ma.plot(figsize=(10,6), color='black', linewidth=1)
df['open'].plot(color='gray', linestyle='--', linewidth=1);
