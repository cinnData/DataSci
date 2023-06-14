## Barcelona Airbnb listings ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'airbnb.csv'
df = pd.read_csv(filename, index_col=0)
df.info()
df.head()

# Q1. Counting duplicates #
df.index.duplicated().sum()
df.duplicated().sum()
df = df.drop_duplicates()
df.shape

# Q2. How old are the hosts? #
df['host_id'][df['host_since'] < '2010-01-01'].value_counts()
df['host_id'].unique().shape

# Q3. Proportion of listings with missing ratings #
df.isna().sum()
df['review_scores_rating'].isna().mean().round(3)

# Q4. Distribution of the price #
df['price'].plot.hist(figsize=(7,5), color='gray', edgecolor='white');
df['price'].describe()
df['price'][df['price'].between(25,150)].plot.hist(figsize=(7,5), color='gray', edgecolor='white', bins=25);

# Q5. Average price per room type #
df.groupby(by='room_type')['price'].mean().round()
df.groupby(by='room_type')['price'].median().round()

# Q6. Top-10 neighbourhoods #
df['neighbourhood'].value_counts().head(10)
df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count', ascending=False).head(10)
