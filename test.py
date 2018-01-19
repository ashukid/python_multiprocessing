#Python 3.5

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import time


# reducing the input time

t=time.time()
# filename = "combine.csv"
# data = pd.read_csv(filename)
data = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
# dataNew = pd.get_dummies(data)
oht = OnehotTransactions()
dataNew = oht.fit(data).transform(data)
dataNew=pd.DataFrame(dataNew,columns=oht.columns_)
print("time taken for input = {}".format(time.time()-t))




t1=time.time()
df = pd.DataFrame(dataNew, columns=dataNew.columns)
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
# frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)


# patterns = association_rules(frequent_itemsets, metric="lift", min_threshold=1.)
# print(patterns)
print("time taken by apriori = {}".format(time.time()-t1))