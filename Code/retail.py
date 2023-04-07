## Example - RFM based segmentation in online retail transaction data ##

# Importing the data #
import pandas as pd
path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
filename = path + 'retail.csv.zip'
df = pd.read_csv(filename)
df.head()
pd.crosstab(df['InvoiceNo'].str.contains('C'), df['Quantity'] < 0)

# Q1. Create a new column with the number of days since the invoice was generated #
df['InvoiceDate'] = df['InvoiceDate'].astype('datetime64[D]')
max_date = max(df['InvoiceDate'])
max_date
df['Diff'] = (max_date - df['InvoiceDate']).dt.days
df

# Q2a. Creating recency and frequency data #
RF = df.groupby('CustomerID')['Diff'].agg(['min', 'count'])
RF
RF.columns = ['Recency', 'Frequency']

# Q2b. Creating monetary data #
df['Monetary'] = df['Quantity']*df['UnitPrice']
M = df.groupby('CustomerID')['Monetary'].sum()
M.head()

# Q2c. Joining the two data sets #
RFM = RF.join(M)
RFM.head()
RFM.describe()

# Q3a. Removing outliers #
def not_outlier(x): return x.between(x.quantile(0.025), x.quantile(0.975))
RFM = RFM[not_outlier(RFM['Recency']) & not_outlier(RFM['Frequency']) & not_outlier(RFM['Monetary'])]
RFM.shape

# Q3b. Normalization #
import numpy as np
def normalize(x): return (x - np.min(x))/(np.max(x) - np.min(x))
RFM1 = RFM.apply(normalize, axis=0)

# Q3c. 8-cluster analysis #
import scipy.cluster.vq as cluster
center = cluster.kmeans(RFM1, 8)[0]
center
label = cluster.vq(RFM1, center)[0]
RFM['Segment'] = label
RFM.head()
RFM['Segment'].value_counts()

# Q4a. Convert every dimension of the RFM data set to a binary scale (High/Low) #
def high_low(s): return s.apply(lambda x: (x > s.median()) + 0).astype(str)
RFM2 = high_low(RFM['Frequency']) + high_low(RFM['Frequency']) + high_low(RFM['Monetary'])

# Q4b. Compare this partition with that of the preceding question #
pd.crosstab(RFM['Segment'], RFM2)

# Visualization # 
segment = 1
from matplotlib import pyplot as plt
# Set the size of the figure
plt.figure(figsize = (18,6))
# First subplot
plt.subplot(1, 3, 1)
plt.hist(RFM['Recency'][RFM['Segment'] == segment], color='gray', rwidth=0.96)
plt.title('Figure 1. Recency ')
plt.xlabel('Recency')
# Second subplot
plt.subplot(1, 3, 2)
plt.hist(RFM['Frequency'][RFM['Segment'] == segment], color='gray', rwidth=0.96)
plt.title('Figure 2. Frequency')
plt.xlabel('Frequency')
# Third subplot
plt.subplot(1, 3, 3)
plt.hist(RFM['Monetary'][RFM['Segment'] == segment], color='gray', rwidth=0.96)
plt.title('Figure 3. Monetary')
plt.xlabel('Monetary');

