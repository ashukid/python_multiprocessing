#Python 3.5

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import time


t=time.time()
filename = "combine.csv"
data = pd.read_csv(filename)
dataNew = pd.get_dummies(data)
print(time.time()-t)


t1=time.time()
df = pd.DataFrame(dataNew, columns=dataNew.columns)
frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)
print("time taken for apriori = {}".format(time.time()-t1))