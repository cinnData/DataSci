## Example - Market basket analysis at the grocery outlet ##

# The data set #
import pandas as pd
url1 = 'https://raw.githubusercontent.com/cinnData/DataSci/main/'
url2 = '11.%20Association%20rules/groceries.csv'
url = url1 + url2
df = pd.read_csv(url)
df.shape
df[df.columns[:10]].head()
df.count().sum()
df.sum().sum()

# Mining itemsets #
from mlxtend.frequent_patterns import apriori
freq_itemsets = apriori(df, min_support=0.01, use_colnames=True)
freq_itemsets.info()
freq_itemsets.sort_values('support', ascending=False).head()
freq_itemsets.sort_values('support', ascending=False).tail()
freq_itemsets.itemsets[0]
freq_itemsets['length'] = freq_itemsets['itemsets'].apply(len)
item1 = freq_itemsets[freq_itemsets['length'] == 1]
item1.sort_values('support', ascending=0).head(10)
item2 = freq_itemsets[freq_itemsets['length'] == 2]
item2.sort_values('support', ascending=0).head(10)
item3 = freq_itemsets[freq_itemsets['length'] == 3]
item3.sort_values('support', ascending=0).head(10)

# Mining association rules #
from mlxtend.frequent_patterns import association_rules
rules = association_rules(freq_itemsets, metric="confidence", min_threshold=0.4)
rules = rules.sort_values('confidence', ascending=0).head(10)
rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
