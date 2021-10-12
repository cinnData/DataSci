## Example - Netflix job postings ##

# Capturing the source code #
import requests
page = requests.get('https://jobs.lever.co/netflix').text

## Parsing the source code ##
from lxml import html
tree = html.fromstring(page)
type(tree)

# Getting the ID's for the job postings #
id = tree.xpath('//div/@data-qa-posting-id')
id[:5]
len(id)
link = ['https://jobs.lever.co/netflix/' + i for i in id]
link[:5]

# Job titles #
job = tree.xpath('//h5[@data-qa="posting-name"]/text()')
job[:5]

# Job location #
location = tree.xpath('//span[@class="sort-by-location posting-category small-category-label"]/text()')
location[:5]

# Team #
team = tree.xpath('//span[@class="sort-by-team posting-category small-category-label"]/text()')
team[:5]
team = [t.split(' – ') for t in team]
team[:5]
division = [t[0] for t in team]
division[:5]
dept = [t[1] for t in team]
dept[:5]

# The package json #
import json
json_list = [{'Name': 'John', 'Age': 27},
     {'Name': 'Peter', 'Age': 32, 'Children': 'Louis'},
     {'Name': 'Maria', 'Age': 29, 'Children': ['Edward', 'Christine']}]
json_doc = json.dumps(json_list)
json_doc
json.loads(json_doc)

# Scraping data in JSON format #
link[0]
page = requests.get(link[0]).content
tree = html.fromstring(page)
json_doc = tree.xpath('//script[@type="application/ld+json"]/text()')
len(json_doc)
json_dict = json.loads(json_doc[0])
type(json_dict)
json_dict.keys()
json_dict['employmentType']
json_dict['datePosted']
json_dict['description']

# A function to scrape information from an individual page #
def f(l):
    page = requests.get(l).content
    tree = html.fromstring(page)
    json_doc = tree.xpath('//script[@type="application/ld+json"]/text()')
    json_dict = json.loads(json_doc[0])
    return [json_dict['employmentType'], json_dict['datePosted'], json_dict['description']]
f(link[0])

# Looping over the individual pages #
employmentType, datePosted, description = [], [], []
for l in link:
    data = f(l)
    employmentType = employmentType + [data[0]]
    datePosted = datePosted + [data[1]]
    description = description + [data[2]]

# Gather the information collected in a data frame #
import pandas as pd
df = pd.DataFrame({'job': job, 'location': location, 'division': division, 'dept': dept,
  'employmentType': employmentType, 'datePosted': datePosted, 'description': description}, index=id)
df.info()
df.head()
