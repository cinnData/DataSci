## Amazon jobs data #

# Importing the data (edit path) #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'amzn.csv.zip'
df = pd.read_csv(filename, index_col=0)
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
df['location'][df['location'].str.startswith('IN')].value_counts()
df['location'][df['location'].str.contains('^IN')].value_counts()

# Q2c. Positions incomplete #
(df['location'].str.count(',') == 2).mean().round(3)
df.location[df['location'].str.count(',') == 1].value_counts().head(10)
df.location[df['location'].str.count(',') == 0].value_counts()

# Q3a. Programming languages in the basic qualifications field #
df['basic_qualifications'].str.contains('java', case=False).mean().round(3)
df['basic_qualifications'].str.contains('javascript', case=False).mean().round(3)
df['basic_qualifications'].str.contains('java script', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c#', case=False).mean().round(3)
df['basic_qualifications'].str.contains('c\+\+', case=False, regex=True).mean().round(3)
df['basic_qualifications'].str.contains('c++', case=False, regex=False).mean().round(3)
df['basic_qualifications'].str.contains('sql', case=False).mean().round(3)
df['basic_qualifications'].str.contains('mysql', case=False).mean().round(3)
df['basic_qualifications'].str.contains('python', case=False).mean().round(3)

# Q3b. Programming languages in basic qualifications (alternative) #
bags = df['basic_qualifications'].str.lower().str.findall('\w+\+*')
def f(x): return 'java' in x
def g(x): return 'c++' in x
bags.apply(f).mean().round(3)
bags.apply(g).mean().round(3)

# Q4. Experience in preferred qualifications #
df['preferred_qualifications'].str.contains('experience', case=False).mean().round(3)
df['preferred_qualifications'].str.count('\+?[0-9]\+? years').value_counts()
df[df['preferred_qualifications'].str.count('[0-9]\+? years')> 5]
df['preferred_qualifications'][1542577]
df['preferred_qualifications'][1588664]
