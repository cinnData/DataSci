## Book recommendations ##

# Importing data from CSV files (edit path) #
import pandas as pd
path = 'Dropbox/ds_course/data/'
ratings = pd.read_csv(path + 'book_ratings.csv')
ratings.info()
items = pd.read_csv(path + 'book_items.csv')
items.info()


# Q1. How often do bookcrossers rate the books they pick? #
(ratings['rating'] > 0).mean().round(3)

# Q2. Which titles have been picked more times? #
df = ratings.merge(items)
df.info()
df['title'].value_counts().head(10)

# Q3. Which books have been rated highest? #
df1 = df[df['rating'] > 0][['title', 'rating']].groupby(by='title').agg(['mean', 'count'])
df1.columns= ['mean', 'count']
df1[df1['count'] >= 25].sort_values(by='mean', ascending=False).head(10)

# Q4. How many editions of The Martian Chronicles are offered by BookCrossing? #
items[items['title'].str.contains('martian chronicles', case=False)]
mc_isbn = items[items['title'].str.contains('martian chronicles', case=False)]['isbn']
mc_isbn

# Q5a. How many ratings of The Martian Chronicles #
(ratings['isbn'].isin(mc_isbn)).sum()
((ratings['isbn'].isin(mc_isbn)) & (ratings['rating'] > 0)).sum()

# Q5b. Selecting data for the recommendation #
mc_users = ratings[ratings['isbn'].isin(mc_isbn)]['user']
rec_ratings = ratings[ratings['user'].isin(mc_users)]
rec_ratings = rec_ratings[~rec_ratings['isbn'].isin(mc_isbn)]

# Q5c. Recommendation for readers of The Martian Chronicles #
conf = rec_ratings['isbn'].value_counts()/93
pd.DataFrame({'conf': conf[:5]}).join(items.set_index('isbn'))[['title', 'author', 'conf']]
