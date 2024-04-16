## [DS-04E] Example - Netflix data ##

# Capturing the source code #
import requests
html_str = requests.get('https://jobs.lever.co/netflix').text

# Parsing the source code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

# Job titles #
job = soup.find_all('h5', {'data-qa': 'posting-name'})
len(job)
job[:5]
job[-5:]
job = [j.string for j in job]
job[:5]

# Workplace types #
worktype = soup.find_all('span', 'display-inline-block small-category-label workplaceTypes')
worktype = [w.string for w in worktype]
worktype[:5]
worktype = [w.replace('\xa0—\xa0', '') for w in worktype]
worktype[:5]

# Job locations #
location = soup.find_all('span', 'sort-by-location posting-category small-category-label location')
location = [l.string for l in location]
location[:5]

# Links #
link = soup.find_all('a', 'posting-title')
link = [l['href'] for l in link]
link[:5]

# Packing #
import pandas as pd
df = pd.DataFrame({'job': job, 'worktype': worktype, 'location': location, 'link': link})
df.info()
df.head()

# Exporting the data to a CSV file (edit path) #
df.to_csv('netflix.csv', index=False)
