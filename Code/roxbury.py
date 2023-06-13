## Example - Assessing home values in West Roxbury ##

# Importing the data (edit path) #
import pandas as pd
path = 'Dropbox/ds_course/data/'
filename = path + 'roxbury.csv'
df = pd.read_csv(filename)
df.shape
df.index
df.columns
df.head()
df.tail()
df.info()
df.describe()

# Q1. Distribution of the home assessed value #
df['value'].plot.hist(figsize=(7,5), color='gray', edgecolor='white');

# Q2. Association between value and size measures #
df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr()
df[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)
df.plot.scatter(x='living_area', y='value', figsize=(5,5), color='gray');

# Q3. Trimming the data #
df1 = df[df['living_area'].between(1000, 2000)]
df1[['value', 'lot_sqft', 'gross_area', 'living_area']].corr().round(2)
df1.plot.scatter(x='living_area', y='value', figsize=(5,5), color='gray');
