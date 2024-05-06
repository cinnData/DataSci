## [DS-06E] Example - Online retail transaction data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'retail.csv.zip'
df = pd.read_csv(filename, parse_dates=[4])

# Exploring the data #
df.info()
df.head()
pd.crosstab(df['InvoiceNo'].str.contains('C'), df['Quantity'] < 0)

# Q1. New column with the number of days since the invoice was generated #
max_date = df['InvoiceDate'].max()
max_date
df['Diff'] = max_date - df['InvoiceDate']
df['Diff']
df['Diff'] = df['Diff'].dt.days
df.head()

# Q2. Group by customer and aggregate to create the RFM data set #
RF = df.groupby('CustomerID')['Diff'].agg(['min', 'count'])
RF.head()
RF.columns = ['Recency', 'Frequency']
df['Monetary'] = df['Quantity']*df['UnitPrice']
M = df.groupby('CustomerID')['Monetary'].sum()
M.head()
RFM = RF.merge(M, left_index=True, right_index=True)
RFM.head()

# Q3. 8-cluster analysis #
RFM.describe()
def normalize(x): return (x - x.min())/(x.max() - x.min())
RFM1 = RFM.apply(normalize, axis=0)
RFM1.head()
import scipy.cluster.vq as cluster
centers = cluster.kmeans(RFM1, k_or_guess=8)[0]
centers
labels = cluster.vq(RFM1, centers)[0]
labels
RFM['Segment'] = labels
RFM.head()
RFM['Segment'].value_counts()
