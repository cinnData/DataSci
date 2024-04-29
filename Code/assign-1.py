## Assignment 1 ##

# Capturing the source code #
import requests
html_str = requests.get('https://jobs.lever.co/netflix').text

# Parsing the source code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

# Failed attempt #
commit = soup.find_all('span', 'sort-by-commitment posting-category small-category-label commitment')
commit = [c.string for c in commit]
len(commit)

# Posts #
post = soup.find_all('a', 'posting-title')
len(post)
post[0]

# Job title #
job = [p.find('h5', {'data-qa': 'posting-name'}).string for p in post]
job[:5]

# Workplace type #
worktype = [p.find('span', 'display-inline-block small-category-label workplaceTypes').string.replace('\xa0—\xa0', '') for p in post]
worktype[:5]

# Commitment #
commit = [p.find('span', 'sort-by-commitment posting-category small-category-label commitment') for p in post]
commit = [(c.string if c else None) for c in commit]
commit[:5]

# Job location #
location = [p.find('span', 'sort-by-location posting-category small-category-label location').string for p in post]
location[:5]

# Link #
link = [p['href'] for p in post]
link[:5]

# Packing #
import pandas as pd
df = pd.DataFrame({'job': job, 'worktype': worktype, 'commit': commit, 'location': location, 'link': link})
df.info()
df.head()
df.isna().sum()

# Exporting the data to a CSV file (edit path) #
df.to_csv('netflix.csv', index=False)

# Positions in India (1) #
df['location'].str.contains('INDIA').sum()
df['location'].str.contains('india', case=False).sum()
df[['job', 'location']][df['location'].str.contains('india', case=False)]

# Positions in India (2) #
filter = df['location'].str.contains('india', case=False) & df['job'].str.contains('data', case=False)
df[filter]
