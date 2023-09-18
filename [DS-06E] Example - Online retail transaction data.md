# [DS-06E] Example - Online retail transaction data

## Introduction

The **RFM model** is commonly used in **customer relationship management** and has received particular attention in retail and professional services industries. It has been widely used in measuring customer lifetime value, customer segmentation and behavior analysis, and also for predicting the response to direct marketing campaigns.

The RFM model is a three-dimensional representation of the customer. The three dimensions, which can be briefly defined as:

* **Recency** (R): How recently did that customer purchase?

* **Frequency** (F): How often does he/she purchase?

* **Monetary value** (M): How much does he/she spend?

These three dimensions can be calculated in different ways, depending on the data available. Once the data analist has them as three columns in a data set in which every row stands for a customer, they can be used for **segmentation**, for predicting various outcomes, or other jobs.

In the simplest versions, every dimension is coverted to a **categorical scale**. For instance, recency might be broken into three categories: customers with purchases within the last 90 days, between 91 and 365 days, and longer than 365 days. Such categories may be derived from business rules or by means of data mining techniques.

RFM models are easy for managers to understand as they do not require statistical software or expertise and are straightforward to apply to customer data. For instance, once each of the attributes has the appropriate categories defined, customer segments can be created from the intersection of the values. If there were three categories for each attribute, then the resulting matrix would have 27 possible combinations (a well-known commercial approach uses five bins per attributes, which yields 125 segments). Identifying the most valuable RFM segments can capitalize on chance relationships in the data used for the analysis.

In spite of the popularity of the discrete RFM model, it has been argued that valuable information is lost in the conversion to a categorical scale, so it would be better to keep the original scales. In that case, **clustering techniques** can be used for the segmentation, after normalizing the three dimensions, for instance into the 0-1 range.

In this example, we use a real **online retail transaction** data set of two years. This data set contains all the transactions occurring for a UK-based and registered non-store online retail, between December 1rst 2009 and December 9th 2011. The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.

## The data set

The data come in the file `retail.csv` (zipped), which has 406,829 rows. Every row corresponds to an item included in a transaction. There are 22,190 transactions, identified by the invoice number, involve 4,372 customers. 

The columns are:

* `InvoiceNo`, the invoice number. A 6-digit integer uniquely assigned to each transaction. If the transaction has been a cancellation, that integer is prceded by the letter 'C'.

* `StockCode`, the product code. A 5-digit number uniquely assigned to each distinct product.

* `Description`, the product name.

* `Quantity`, the number of units of that product in that transaction. It takes a negative value for a cancellation.

* `InvoiceDate`, the invoice date and time, as 'yyyy-mm-dd hh:mm:ss'. 

* `UnitPrice`, the product unit price in sterling pounds (£).

* `CustomerID`, the customer identifier. A 5-digit integer uniquely assigned to that customer.

* `Country`, the name of the country where the customer resides.

Source: Daqing Chen, School of Engineering, London South Bank University, London SE1 0AA, UK.

## Questions

Q1. Create a new column indicating, for every transaction, the number of days from the date the invoice was generated to the last day in the data set (2011-12-09).

Q2. Group by customer and aggregate to create the **RFM data set**. This new data set must include the following three columns: (a) `Recency`, obtained by averaging the variable suggested in the preceding question , (b) `Frequency`, obtained by counting the number of transactions per customer, and (c) `Monetary`, obtained by summing the money spent per customer.

Q3. Perform a **8-cluster analysis** of the RFM data set. 

## Importing the data

We import Pandas as usual. In this example, we use the argument `parse_col=[4]` in  `read_csv()`, to indicate that the column `InvoiceData` is to be converted to data type `datetime64`. We could also import the data in the usual way, applying `.astype(datetime64[ns])` to that column. 

```
In [1]: import pandas as pd
   ...: path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
   ...: filename = path + 'retail.csv.zip'
   ...: df = pd.read_csv(filename, parse_dates=[4])
```

## Exploring the data

We explore now the data as usual, with the methods `. info()` and `.head()`. The data are complete and look right. Note the data type of `InvoiceDate`.  

```
In [2]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 406829 entries, 0 to 406828
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype  
---  ------       --------------   -----  
 0   InvoiceNo    406829 non-null  object        
 1   StockCode    406829 non-null  object        
 2   Description  406829 non-null  object        
 3   Quantity     406829 non-null  int64         
 4   InvoiceDate  406829 non-null  datetime64[ns]
 5   UnitPrice    406829 non-null  float64       
 6   CustomerID   406829 non-null  int64         
 7   Country      406829 non-null  object        
dtypes: datetime64[ns](1), float64(1), int64(2), object(4)
memory usage: 24.8+ MB
```

```
In [3]: df.head()
Out[3]: 
  InvoiceNo StockCode                          Description  Quantity   
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  \
1    536365     71053                  WHITE METAL LANTERN         6   
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

           InvoiceDate  UnitPrice  CustomerID         Country  
0  2010-12-01 08:26:00       2.55       17850  United Kingdom  
1  2010-12-01 08:26:00       3.39       17850  United Kingdom  
2  2010-12-01 08:26:00       2.75       17850  United Kingdom  
3  2010-12-01 08:26:00       3.39       17850  United Kingdom  
4  2010-12-01 08:26:00       3.39       17850  United Kingdom  
```

According to the description of the data, there must be cancellations, identified with a special ID. Indeed, we have 8,905 cancellations, with negative quantities.

```
In [4]: pd.crosstab(df['InvoiceNo'].str.contains('C'), df['Quantity'] < 0)
Out[4]: 
Quantity    False  True 
InvoiceNo               
False      397924      0
True            0   8905
```

## Q1. New column with the number of days since the invoice was generated

We take as the reference for counting the days the date of the last invoice included in the data.

```
In [5]: max_date = max(df['InvoiceDate'])
   ...: max_date
Out[5]: Timestamp('2011-12-09 12:50:00')
```

Next, we subtract the invoice dates from the reference date. The new columns has a special data type, `timeDelta64`.

```
In [6]: df['Diff'] = max_date - df['InvoiceDate']
   ...: df['Diff']
Out[6]: 
0        373 days 04:24:00
1        373 days 04:24:00
2        373 days 04:24:00
3        373 days 04:24:00
4        373 days 04:24:00
                ...       
406824     0 days 00:00:00
406825     0 days 00:00:00
406826     0 days 00:00:00
406827     0 days 00:00:00
406828     0 days 00:00:00
Name: Diff, Length: 406829, dtype: timedelta64[ns]
```

With `.days`, we convert the column `Diff` from type `timeDelta64` to type `int` (flooring down), getting a number of days, which indicates the recency of the invoice.

```
In [7]: df['Diff'] = df['Diff'].dt.days
    ..: df.head()
Out[7]: 
  InvoiceNo StockCode                          Description  Quantity   
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  \
1    536365     71053                  WHITE METAL LANTERN         6   
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   

          InvoiceDate  UnitPrice  CustomerID         Country  Diff  
0 2010-12-01 08:26:00       2.55       17850  United Kingdom   373  
1 2010-12-01 08:26:00       3.39       17850  United Kingdom   373  
2 2010-12-01 08:26:00       2.75       17850  United Kingdom   373  
3 2010-12-01 08:26:00       3.39       17850  United Kingdom   373  
4 2010-12-01 08:26:00       3.39       17850  United Kingdom   373  
```

## Q2. Group by customer and aggregate to create the RFM data set

In the RFM data set, every custmer must a row, with the RFM values. To create the first two columns, `Recency` and `Frequency`, we group by customer and aggregate with functions `min()` and `count()`.

```
In [8]: RF = df.groupby('CustomerID')['Diff'].agg(['min', 'count'])
   ...: RF.head()
Out[8]: 
            min  count
CustomerID            
12346       325      2
12347         1    182
12348        74     31
12349        18     73
12350       309     17
```

For clarity, we change the names of the columns. Note that `Recency` contains, for every customer, the number of days since the last invoice of that customer.

```
In [9]: RF.columns = ['Recency', 'Frequency']
```

For the monetary value, we first create a column in the original data set with the total amount of every invoice. This will the product of the unit price by the quantity.

```
In [10]: df['Monetary'] = df['Quantity']*df['UnitPrice']
```

By aggregating (now with `sum()`) for every customer, we get a series with the monetary data.

```
In [11]: M = df.groupby('CustomerID')['Monetary'].sum()
    ...: M.head()
Out[11]: 
CustomerID
12346       0.00
12347    4310.00
12348    1797.24
12349    1757.55
12350     334.40
Name: Monetary, dtype: float64
``` 

Finally, we join this series for the data frame `RF`. We use the method `merge()`, specifying that the join is based on the indexes. The same could be done with `.join()` and with the function `concat()` (everyone with its own rules).

```
In [12]: RFM = RF.merge(M, left_index=True, right_index=True)
    ...: RFM.head()
Out[12]: 
            Recency  Frequency  Monetary
CustomerID                              
12346           325          2      0.00
12347             1        182   4310.00
12348            74         31   1797.24
12349            18         73   1757.55
12350           309         17    334.40
```

## Q3. 8-cluster analysis

The quick exploration of the RFM data set given by `RFM.head()` suggests that, using the data as they are, we can give more weight to `Monetary` than the other two variables. This is confirmed by the statistical summary that follows. 

```
In [13]: RFM.describe()
Out[13]: 
           Recency    Frequency       Monetary
count  4372.000000  4372.000000    4372.000000
mean     91.047118    93.053294    1898.459701
std     100.765435   232.471608    8219.345141
min       0.000000     1.000000   -4287.630000
25%      16.000000    17.000000     293.362500
50%      49.000000    42.000000     648.075000
75%     142.000000   102.000000    1611.725000
max     373.000000  7983.000000  279489.020000
```

So, normalizing the data looks like a reasonable step. **Min-max normalization** can be performed directly by applying the following function to every column of the data frame.

```
In [14]: def normalize(x): return (x - x.min())/(x.max() - x.min())
```
This function can be applied to a vector-like data container (NumPy 1D array or Pandas series) which admits the methods `.max()` and `.min()`. There are many ways of applying it to the columns of the data frame `RFM`. One way to it in one line is by means of the method `.apply()`. The argument `axis=0` means that the function is applied by column. With `axis=1`, it woukld be applied by row.

```
In [15]: RFM1 = RFM.apply(normalize, axis=0)
    ...: RFM1.head()
Out[15]: 
             Recency  Frequency  Monetary
CustomerID                               
12346       0.871314   0.000125  0.015109
12347       0.002681   0.022676  0.030297
12348       0.198391   0.003758  0.021442
12349       0.048257   0.009020  0.021303
12350       0.828418   0.002005  0.016288
```

We are ready now for the **cluster analysis**. We use the version of the package **SciPy**, import the $k$-means clustering tools, from the subpackage `scipy.cluster.vq`, as follows.

```
In [16]: import scipy.cluster.vq as cluster
```

Note that `cluster` is here a user-provided name. We extract from the data the eight **cluster centers**, and then use the centers to create a new column with **cluster labels**. The centers are obtained as a 2D array with eight rows and three columns. Every row stands for the center of one cluster, and the three entries there are the RFM values of that center. So, the center can be seen as the average customer of the corresponding cluster (in mathematical terms, this is, precisely what it is). 

The function `kmeans()` returns a tuple containing two objects: the first one is the center matrix, and the second one is the average (non-squared) Euclidean distance between a customer and the closest center (the homework includes an exercise on this). So, we extract the first item of that tuple to get the center matrix.

```
In [17]: centers = cluster.kmeans(RFM1, k=8)[0]
    ...: centers
Out[17]: 
array([[0.51290262, 0.00406231, 0.01708207],
       [0.14106821, 0.00802362, 0.01890266],
       [0.90729203, 0.00279722, 0.01624688],
       [0.69792636, 0.00283802, 0.0167874 ],
       [0.22355487, 0.00616986, 0.01864267],
       [0.06643687, 0.01063504, 0.02016824],
       [0.35541264, 0.00553187, 0.0178437 ],
       [0.01576313, 0.0268319 , 0.03266514]])
```

The function `vq()` takes the centers and also returns two objects. The first one is the vector of cluster labels, and the second one a vector containing, for every customer, the distance to the closest center, both as 1D arrays. So the labels are obtained as:

```
In [18]: labels = cluster.vq(RFM1, centers)[0]
    ...: labels
Out[18]: array([2, 7, 4, ..., 7, 7, 1], dtype=int32)

```

Note that `centers` and `labels`are NumPy arrays. We can add the labels as a column to the data frame `RFM`:

```
In [19]: RFM['Segment'] = label
    ...: RFM.head()
Out[19]: 
            Recency  Frequency  Monetary  Segment
CustomerID                                       
12346           325          2      0.00        2
12347             1        182   4310.00        7
12348            74         31   1797.24        4
12349            18         73   1757.55        5
12350           309         17    334.40        2
```

We can use now `.value_counts()` to check the sizes of the segments:

```
In [20]: RFM['Segment'].value_counts()
Out[20]: 
Segment
7    1022
5     946
1     630
4     468
0     350
3     343
6     332
2     281
Name: count, dtype: int64
```

## Q4. Segments based on binarized RFM dimensions 

Binarization

```
In [22]: RFM['BinRecency'] = ((RFM['Recency'] > RFM['Recency'].median()) + 0).astype(str)
    ...: RFM['BinFrequency'] = ((RFM['Frequency'] > RFM['Frequency'].median()) + 0).astype(str)
    ...: RFM['BinMonetary'] = ((RFM['Monetary'] > RFM['Monetary'].median()) + 0).astype(str)
    ...: RFM.head()
Out[22]: 
            Recency  Frequency  Monetary  Segment BinRecency BinFrequency   
CustomerID                                                                  
12346           325          2      0.00        2          1            0  \
12347             1        182   4310.00        7          0            1   
12348            74         31   1797.24        4          1            0   
12349            18         73   1757.55        5          0            1   
12350           309         17    334.40        2          1            0   

           BinMonetary  
CustomerID              
12346                0  
12347                1  
12348                1  
12349                1  
12350                0  
```
Compare this partition with that of the preceding question

```
In [23]: RFM['BinSegment'] = RFM['BinRecency'] + RFM['BinFrequency'] + RFM['BinMonetary']
    ...: RFM.head()
Out[23]: 
            Recency  Frequency  Monetary  Segment BinRecency BinFrequency   
CustomerID                                                                  
12346           325          2      0.00        2          1            0  \
12347             1        182   4310.00        7          0            1   
12348            74         31   1797.24        4          1            0   
12349            18         73   1757.55        5          0            1   
12350           309         17    334.40        2          1            0   

           BinMonetary BinSegment  
CustomerID                         
12346                0        100  
12347                1        011  
12348                1        101  
12349                1        011  
12350                0        100  
```

```
In [24]: pd.crosstab(RFM['Segment'], RFM['BinSegment'])
Out[24]: 
BinSegment  000  001  010  011  100  101  110  111
Segment                                           
0             0    0    0    0  238   27   27   58
1            92   24   25   96  170   47   37  139
2             0    0    0    0  228   11   29   13
3             0    0    0    0  277   22   20   24
4             0    0    0    0  198   73   35  162
5           295   77  101  473    0    0    0    0
6             0    0    0    0  184   41   26   81
7           143   65   61  753    0    0    0    0
```

## Homework

1. As explained in lecture DS-06, the $k$-means algorithm uses a random start. So, different runs will give different results. In real applications we don't these differences to be relevant. Compare the results of two partitions obtained in different runs of the $k$-means algorithm, using cross tabulation.

2. The second item in the outcome of the function `kmeans()` is the average Euclidean distance between a customer and the closest center, and be taken as a measure of the "quality" of the segmentation. Apply `means()` with different values of the parameter `k` and compare the corresponding quality measures. Do you think that `k=8` was a good choice?

3. Drop extreme values from the RFM data (before the normalization), perform the normalization and the cluster analysis again. Compare the new clusters with those obtained in question Q3.

4. Convert every dimension of the RFM data set to a **binary scale** (High/Low), and a create a segmentation based on the eight combinations. Compare this partition with the clusters obtained in question Q3. 
