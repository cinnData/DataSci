## Tutorial - Time series data in Pandas ##

# Datetime indexes in Pandas #
import pandas as pd
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2 = '4.%20Basic%20stats%20in%20Pandas/aapl.csv'
url = url1 + url2
df = pd.read_csv(url, index_col=0, parse_dates=True)
df.info()
df.index
df.index.name = None
df[:'2019-01-08']
df['open'][df.index.day_name() == 'Friday'].head()
df['open'][df.index.month == 2].head()
df['open'].plot(figsize=(10,6), color='black', linewidth=1);

# Calculating returns #
d_return = df['open'].pct_change()
d_return.head()
d_return.plot(figsize=(10,6), color='black', linewidth=1);
w_return = df[df.index.weekday == 4]['open'].pct_change()
w_return.head()
w_vol = df['open'].resample('W').sum()
w_vol.head(3)
w_vol.tail(3)
w_vol.plot(figsize=(10,6), color='black', linewidth=1);

# Rolling windows #
df['open'].rolling(5).mean().head(10)
ma = df['open'].rolling(5, center=True).mean()
ma.head(10)
ma.plot(figsize=(10,6), color='black', linewidth=1)
df['open'].plot(color='gray', linestyle='--', linewidth=1);