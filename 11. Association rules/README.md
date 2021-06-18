# 11. Association rules

### What is an association rule?

An **association rule** takes usually the form A => B. A is the **antecedent** (LHS) and B is the **consequent** (RHS). The rule is read as *if A, then B*. Association rules are, in general, **local patterns**, which apply only to a small proportion of samples.

Association rules are typically searched in **transactions data**. Each transaction contains a set of **items**. The antecedent and the consequent of a rule are always **disjoint**, that is, they do not have common items. Let me refresh two popular examples:

* In a typical application to **market basket analysis**, the transactions are the visits of the customers to a supermarket, and the items are the different products purchased: milk, sugar, etc. An example of an association rule is {butter} => {whole milk}.

* In **clickstream analysis**, the items are the pages visited by an individual and a transaction is an uninterrupted sequence of pages (you have to specify what this specifically means).  

Although we see a transaction as a set of items purchased at a time, transaction data rarely come in this way. There are two typical formats:

* **Transactional data**, with two fields: (a) an ID field, which identifies the transaction, and (b) a content field, which contains the items involved in the transaction, one per row. Thus, one transaction covers as many rows as items it contains.

* **Tabular data**, with transactions in the rows and items in the columns. For each combination transaction/item, the entry is one if that particular transaction contained this particular item and zero if it was not so (in Python, this can also be `True/False`). This is called a **transaction/item matrix**. An ID column, identifying the transactions, may be included.

Since the number of items in each transaction is usually low, most of the entries in the transaction/item matrix are zeros. So, tabular data are **sparse data**, which makes them inefficient. The best way to store such matrices is listing the coordinates (row and column) of the nonzero entries. This is not discussed here.

### Frequent itemsets

An **itemset** is a set of items. The **support of an itemset** is the proportion of transactions containing that itemset. So, if *A* is an itemset, *N*(*A*) is the number of transactions containing the items of *A* and *N* is the total number of transactions, the support is

supp(*A*) = *N*(*A*)/*N*.

To illustrate this, suppose that a supermarket data set covers 9,835 transactions, and that whole milk is included in 2,513 transactions, butter in 545 transactions, and both together in 271 transactions. Then, the support of {whole milk} is 2,513/9,385 = 0.256, the support of {butter} is 545/9,385 = 0.505, and the support of {butter, whole milk} is 271/9,385 = 0.028.

The support of an itemset can be regarded as an estimate of the **probability** that a transaction includes that itemset. So, we may think that the probability that a customer buys whole milk in a visit to the supermarket is 25.6%.

The **frequent itemsets** are those with the highest support. The favorite algorithm for searching frequent itemsets is the **Apriori algorithm**, which uses a **minimum support** threshold, picking first one-item frequent sets, then two-item sets containing only items already selected, and so on. If the analyst is interested in finding rules, a second step follows, in which the rules are generated from the frequent itemsets, based the **parameters** described below.

### Parameters for mining association rules

Formally defined, a rule is a pair of disjoint itemsets, the antecedent and the consequent. Association rules are evaluated by means of three parameters, the support, the confidence and the lift. The **support of a rule** of is the same as the support of the itemset resulting from the union of the antecedent and the consequent, that is, the proportion of transactions containing both antecedent and consequent,

supp(*A* => *B*) = *N*(*AB*)/N.

Here, *AB* denotes the union of *A* and *B*. The **confidence** of a rule is the proportion of transactions that contain both the antecedent and the consequent among those that contain the antecedent,

conf(*A* => *B*) = supp(*AB*)/supp(*A*) = *N*(*AB*)/*N*(*A*).

In the same way as the support can be regarded as a probability, the confidence can be regarded as the **conditional probability** of the consequent given the antecedent. In the supermarket example, the confidence of {butter} = > {whole milk} is 0.028/0.055 = 0.497 or, equivalently, 271/545 = 0.497.

This can be read as *if you are buying butter, the probability that you are also buying whole milk is 49.7%*. Finally, the **lift** is the ratio of the confidence of a rule (a conditional probability) to the support of the consequent (an unconditional probability),

lift(*A* => *B*) = conf(*A* => *B*)/supp(*B*).

Although it is not always used as a parameter for mining the rules, the lift is sometimes the better measure of how relevant is a rule. In the supermrket example, the  lift of {butter} => {whole milk}es 0.497/0.256 = 1.941, which is read as *customers buying butter buy whole milk 1.941 times more often than the average customer*.

### The Apriori algorithm

In the typical implementation of the Apriori algorithm, the user specifies a minimum support and a **minimum confidence**. Since the objective is to discover local patterns, the minimum support must be low (eg less than 10%) when the number of items is high. Note that finding itemsets with a minimum support can be computationally intensive if that minimum support is low. Once frequent itemsets have been extracted, mining association rules with a minimum confidence is straightforward.

### Association rules in Python

Association rules can be mined in Python with functions from the  package `mlextend`, which was developed as an extension of scikit-learn. The process is split in two steps: (a) extracting the most frequent itemsets, and (b) selecting association rules by support and confidence. We do not always find these two steps separated in data science software applications, but they are so in `mlextend`.

The two steps are made by means of the functions `apriori` and `association_rules`, respectively. We load them as usual:

`from mlxtend.frequent_patterns import apriori, association_rules`

The function `apriori` takes a transaction/item matrix as a data frame,  returning the frequent itemsets as a data frame with two columns, `support` and `itemset`. Suppose that `df` is the user/item matrix and that you set the **minimum support** to 0.01. Then, you extract the frequent itemsets with:

`frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)`

The terms of the column `itemsets` of this data frame are **frozen sets**. The length of one of these itemsets is the number of items in the itemset, so you can extract the itemsets with a specific number of items.

*Note*. The frozen set is an immutable version of the Python set. While elements of a set can be modified at any time, elements of a frozen set remain the same after creation.

To mine association rules, you can use the function `association_rules`. For instance, you can set the minimum confidence to 0.4, in order to select the most relevant rules:

`rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)`

The function `association_rules` returns a data frame with many columns. Among them, we find `antecedents`, `consequents`, `support`, `confidence`, and `lift`.

