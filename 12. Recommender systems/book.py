## Example - Book recommendations ##

# Importing the data #
import pandas as pd
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2a = '12.%20Recommender%20systems/book_ratings.csv'
urla = url1 + url2a
ratings = pd.read_csv(urla)
ratings.info()
url2b = '12.%20Recommender%20systems/book_users.csv'
urlb = url1 + url2b
users = pd.read_csv(urlb)
users.info()
url2c1 = '12.%20Recommender%20systems/book_items-1.csv'
urlc1 = url1 + url2c1
items1 = pd.read_csv(urlc1)
url2c2 = '12.%20Recommender%20systems/book_items-2.csv'
urlc2 = url1 + url2c2
items2 = pd.read_csv(urlc2)
items = pd.concat([items1, items2])
items.info()

# Merging tables #
df = pd.merge(ratings, items)
df = pd.merge(df, users)
df.info()

# How often do bookcrossers rate the books they pick? #
round((ratings['rating'] > 0).mean(), 3)

# Which titles have been picked more times? #
df['title'].value_counts().head(10)

# Which books have been rated highest?  #
df1 = df[df['rating'] > 0].groupby('title')['rating'].agg(['mean', 'count'])
df1[df1['count'] >= 25].sort_values(by='mean', ascending=False).head(10)
df1[df1['count'] >= 100].sort_values(by='mean', ascending=False).head(10)

# Exploring The Martian Chronicles #
items[items['title'] == 'The Martian Chronicles']
(ratings['isbn'] == '0553278223').sum()
((ratings['isbn'] == '0553278223') & (ratings['rating'] > 0)).sum()

# Restricting the data set #
mc_users = ratings[ratings['isbn'] == '0553278223']['user']
mc_users
mc_ratings = ratings[ratings['user'].isin(mc_users)]
mc_ratings
mc_ratings['isbn'].value_counts()
mc_isbn = mc_ratings['isbn'].value_counts().index[1:]
mc_isbn

# Recommendation based on association rules with strong confidence #
mc_conf = mc_ratings['isbn'].value_counts()[1:]/65
mc_conf.index[:10]
t1 = pd.DataFrame({'conf': mc_conf[:10]})
t2 = items.set_index('isbn')
t1.join(t2)[['title', 'author', 'conf']]

# Neighborhood-based recommendation #
dotprod = mc_ratings['isbn'].value_counts()[1:]
dotprod
import numpy as np
mc_mod = np.sqrt(65)
items_mod = np.sqrt(ratings[ratings['isbn'].isin(mc_isbn)]['isbn'].value_counts())
items_mod
cos = dotprod/(mc_mod*items_mod)
cos = cos.sort_values(ascending=False)
cos.head()
cos.index[:10]
t1 = pd.DataFrame({'cos': cos[:10]})
t1.join(t2)[['title', 'author', 'cos']]












