# Example - RFM based segmentation in online retail transaction data

## Introduction

The **RFM model** is commonly used in database marketing and direct marketing and has received particular attention in retail and professional services industries. It has been widely used in measuring customer lifetime value, customer segmentation and behavior analysis, and also for predicting the response to direct marketing campaigns.

The RFM model is a three-dimensional representation of the customer. The three dimensions, which can be briefly defined as:

* **Recency** (R): How recently did the customer purchase?

* **Frequency** (F): How often do he/she purchase?

* **Monetary value** (M): How much do he/she spend?

These three dimensions can be calculated in different ways, depending on the data available. Once the data analist has them as three columns in a data set in which every row stands for a customer, they can be used for segmention, for predicting various outcomes, or other jobs.

In the simplest versions, every dimension is coverted to a **categorical scale**. For instance, recency might be broken into three categories: customers with purchases within the last 90 days, between 91 and 365 days, and longer than 365 days. Such categories may be derived from business rules or using data mining techniques to find meaningful intervals.

RFM models are easy for managers to understand as they do not require statistical software or expertise and are straightforward to apply to customer data. For instance, once each of the attributes has the appropriate categories defined, segments can be created from the intersection of the values. If there were three categories for each attribute, then the resulting matrix would have 27 possible combinations (one well-known commercial approach uses five bins per attributes, which yields 125 segments). Identifying the most valuable RFM segments can capitalize on chance relationships in the data used for the analysis.

In spite of the popularity of the discrete RFM model, it has been argued that valuable information is lost in the conversion to a categorical scale, so it would be better to keep te original scales. In that case, **clustering techniques** can be used for the segmentation, after normalizing the three dimensions, for instance into the 0-1 range.

In this example, we use a real online retail transaction data set of two years. This data set contains all the transactions occurring for a UK-based and registered non-store online retail, between December 1rst 2009 and December 9th 2011. The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.

# The data set

The data come in the file `retail.csv` (zipped), which has 406,829 rows. Every row corresponds to an item included in a transaction. There are 22,190 transactions, identified by the invoice number. These transactions involve 4,372 different customers. 

The columns are:

* `InvoiceNo`, the invoice number. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.

* `StockCode`, the product code. A 5-digit number uniquely assigned to each distinct product.

* `Description`, the product name.

* `Quantity`, the quantity of product in that transaction.

* `InvoiceDate`, the invoice date and time, as 'yyyy-mm-dd hh:mm:ss'. 

* `UnitPrice`, the product unit price in sterling (£).

* `CustomerID`, the customer identifier. A 5-digit number uniquely assigned to each customer.

* `Country`, the name of the country where the customer resides.

Source: Daqing Chen, School of Engineering, London South Bank University, London SE1 0AA, UK.

## Questions

Q1. Create a new column indicating, for every transaction, the number of days from the date the invoice was generated to the last day in the data set (2011-12-09).

Q2. Group by customer and aggregate to create the RFM data set. In this new data set there should be three columns: (a) `Recency`, obtained by averaging the variable suggested in the preceding question , (b) `Frequency`, obtained by counting the number of transactions per customer, and (c) `Monetary`, obtained by summing the money spent per customer.

Q3. Perform a 8-cluster analysis of the RFM data set. 

Q4. Convert every dimension in this RFM data set to a binary scale (High/Low), and a create a segmentation based on the eight combinations. Compare this partition with that of the preceding question and discuss. 

