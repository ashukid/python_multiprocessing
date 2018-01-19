#Python 3.5

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from multiprocessing import Pool

def func(df):
	frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
	frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
	print(frequent_itemsets)

filename = "combine.csv"
data = pd.read_csv(filename)

dataNew = pd.get_dummies(data)

df = pd.DataFrame(dataNew, columns=dataNew.columns)



# Create patterns block to retreive latter
# patterns = association_rules(frequent_itemsets, metric="lift", min_threshold=1.)
# patterns