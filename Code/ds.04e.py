## [DS-04E] Example - Finding a job at Netflix ##

# Downloading the source code #
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

# Job locations #
location = soup.find_all('span', 'sort-by-location posting-category small-category-label location')
location = [l.string for l in location]
location[:5]

# Teams #
team = soup.find_all('span', 'sort-by-team posting-category small-category-label department')
team = [t.string for t in team]
team[:5]
team = [t.split(' – ') for t in team]
team[:5]
division = [t[0] for t in team]
division[:5]
dept = [t[1] for t in team]
dept[:5]

# Links #
link = soup.find_all('a', 'posting-title')
link = [l['href'] for l in link]
link[:5]

# Packing #
import pandas as pd
df = pd.DataFrame({'job': job, 'location': location, 'division': division, 'dept': dept, 'link': link})
df.info()
df.head()

# Exporting the data to a CSV file (edit path) #
df.to_csv('netflix.csv', index=False)
