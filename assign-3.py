## Assignment 3 ##

# Capturing the source code #
import requests
page = requests.get('https://www.iese.edu/search/professors').text

# Parsing the source code #
from lxml import html 
tree = html.fromstring(page)

# Extracting the information #
link = tree.xpath('//a[@class="ficha-profesor"]/@href')
name = tree.xpath('//h4/text()')
description = tree.xpath('//p[@class="profesor-description"]/text()')

# Packing as a data frame #
import pandas as pd
df = pd.DataFrame({'link': link, 'name': name, 'description': description})

# Exporting to CSV #
df.to_csv('iese.csv', index=False)

# Exporting to Excel #
df.to_excel('iese.xls', index=False)

# Exporting to a PostgreSQL database #
import psycopg2
import sqlalchemy as sqla
eng = sqla.create_engine('postgresql://postgres:mcanela11@localhost:5432/postgres')
df.to_sql('iese', eng, index=False)

