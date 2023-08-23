## [DS-02E] Example - Amazon jobs ##

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

# Q2a. Top-ten locations for software developers at Amazon #
df['location'].value_counts().shape
df['location'].value_counts().head(10)

# Q2b. Positions in India #
df['location'][df['location'].str[:2] == 'IN'].value_counts()
df['location'][df['location'].str.contains('^IN', regex=True)].value_counts()

# Q3a. Programming languages in the basic qualifications field #
df['basic_qualifications'].str.contains('c#', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c+', case=False, regex=False).mean().round(3)
df['basic_qualifications'].str.contains('c+', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c\+', case=False).mean().round(3)

# Q3b. Programming languages in the basic qualifications field (alt) #
bags = df['basic_qualifications'].str.lower().str.findall('\w+\+*')
bags.head()

# Q4. Experience in preferred qualifications #
df['preferred_qualifications'].str.contains('experience', case=False).mean().round(3)
df['preferred_qualifications'].str.count('\+?[0-9]\+? years').value_counts()
df[df['preferred_qualifications'].str.count('[0-9]\+? years')> 5]
df['preferred_qualifications'][1542577]
df['preferred_qualifications'][1588664]
