## Skills requested in Google job posts ##

# Importing the data #
import pandas as pd
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2 = '6.%20String%20data%20in%20Pandas/google.csv'
url = url1 + url2
df = pd.read_csv(url, encoding='utf_8')
df.info()
df.head()

# Duplicated job posts #
df.duplicated().sum()
df = df.drop_duplicates()
df.info()

# Exploring the company #
df['company'].value_counts()

# Exploring the job title #
len(df['title'].value_counts())
df['title'].value_counts().head(10)
df['title'].str.contains('Intern').sum()
df['title'].str.contains('Sales').sum()
df['title'].str.contains('Cloud').sum()
df['title'].str.contains('Google Cloud').sum()

# Exploring the category #
len(df['category'].value_counts())
df['category'].value_counts().head(10)

# Exploring the location #
country = df['location'].str.replace(pat='.+, ', repl='')
len(country.value_counts())
country.value_counts().head(10)

# Exploring the last three columns #
df[df['responsibilities'].isna() | df['minqual'].isna() | df['prefqual'].isna()]
df = df.dropna()
df['responsibilities'].str.len().min()
df['minqual'].str.len().min()
df['prefqual'].str.len().min()

# Analysis of the preferred qualifications #
prefqual = df['prefqual'].str.lower()
prefqual[0]
terms = prefqual.str.findall('[a-z]+')
len(terms[0])
terms[0][:10]
allterms = []
for t in terms: allterms = allterms + t
len(allterms)
pd.Series(allterms).value_counts().head(10)
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2 = '6.%20String%20data%20in%20Pandas/stopwords.csv'
url = url1 + url2
stopwords = pd.read_csv(url)
stopwords = stopwords.squeeze().tolist()
xx = [t for t in allterms if t not in stopwords]
len(xx)
pd.Series(xx).value_counts().head(10)
prefqual.str.contains('experience').mean().round(3)
prefqual.str.contains('ability').mean().round(3)
prefqual.str.contains('skills').mean().round(3)
prefqual.str.contains('management').mean().round(3)
prefqual.str.contains('communication').mean().round(3)
prefqual.str.contains('pyhton').mean().round(3)


