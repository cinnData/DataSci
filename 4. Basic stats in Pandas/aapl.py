## Apple Inc. stock prices ##

# Importing the data #
import pandas as pd
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2 = '4.%20Basic%20stats%20in%20Pandas/aapl.csv'
url = url1 + url2
df = pd.read_csv(url, index_col=0)
df.shape
df.index
df.columns
df.head()
df.tail()
df.info()
df.describe()

# The price trend #
df['open']
df['open'].plot(figsize=(10,6), color='gray');

# Daily returns #
df['return'] = 100*df['open'].pct_change()
df['return'].head()
df['return'].plot(figsize=(10,6), color='gray');
df['return'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Trading volume #
df['volume'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);

# Association between daily returns and trading volume #
df.plot.scatter(x='volume', y='return', figsize=(6,6), color='gray');
df['volume'].corr(df['return'])
df['absreturn'] = df['return'].abs()
df.plot.scatter(x='volume', y='absreturn', figsize=(6,6), color='gray');
df['volume'].corr(df['absreturn'])

