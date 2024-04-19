## [DS-02E] Example - Amazon Jobs data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'amzn.csv.zip'
df = pd.read_csv(filename, index_col=0)

# Exploring the data #
df.info()
df.head()

# Q1. Count and drop duplicates #
df.duplicated().sum()
df.index.duplicated().sum()
df = df.drop_duplicates()
df.shape

# Q2. Top-ten locations for software developers at Amazon #
df['location'].value_counts().shape
df['location'].value_counts().head(10)

# Q3. Positions in India #
df['location'][df['location'].str[:2] == 'IN'].value_counts()
df['location'][df['location'].str.contains('^IN', regex=True)].value_counts()

# Q4. Programming languages in the basic qualifications field #
df['basic_qualifications'].str.contains('c#', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c+', case=False, regex=False).mean().round(3)
df['basic_qualifications'].str.contains('c+', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c\+', case=False).mean().round(3)
