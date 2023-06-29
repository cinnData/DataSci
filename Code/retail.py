## Example - RFM based segmentation in online retail transaction data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'retail.csv.zip'
df = pd.read_csv(filename)
df.head()
pd.crosstab(df['InvoiceNo'].str.contains('C'), df['Quantity'] < 0)

# Q1. New column with the number of days since the invoice was generated #
df['InvoiceDate'] = df['InvoiceDate'].astype('datetime64[D]')
max_date = max(df['InvoiceDate'])
max_date
df['Diff'] = (max_date - df['InvoiceDate']).dt.days
df.head()

# Q2a. Creating recency and frequency data #
RF = df.groupby('CustomerID')['Diff'].agg(['min', 'count'])
RF.head()
RF.columns = ['Recency', 'Frequency']

# Q2b. Creating monetary data #
df['Monetary'] = df['Quantity']*df['UnitPrice']
M = df.groupby('CustomerID')['Monetary'].sum()
M.head()

# Q2c. Joining the two data sets #
RFM = RF.merge(M, left_index=True, right_index=True)
RFM.head()
RFM.describe()

# Q3a. Normalization #
import numpy as np
def normalize(x): return (x - np.min(x))/(np.max(x) - np.min(x))
RFM1 = RFM.apply(normalize, axis=0)

# Q3b. 8-cluster analysis #
import scipy.cluster.vq as cluster
center = cluster.kmeans(RFM1, 8)[0]
center
label = cluster.vq(RFM1, center)[0]
RFM['Segment'] = label
RFM.head()
RFM['Segment'].value_counts()

# Q4a. Binarization #
RFM['BinRecency'] = ((RFM['Recency'] > RFM['Recency'].median()) + 0).astype(str)
RFM['BinFrequency'] = ((RFM['Frequency'] > RFM['Frequency'].median()) + 0).astype(str)
RFM['BinMonetary'] = ((RFM['Monetary'] > RFM['Monetary'].median()) + 0).astype(str)
RFM.head()

# Q4b. Compare this partition with that of the preceding question #
RFM['BinSegment'] = RFM['BinRecency'] + RFM['BinFrequency'] + RFM['BinMonetary']
RFM.head()
pd.crosstab(RFM['Segment'], RFM['BinSegment'])
