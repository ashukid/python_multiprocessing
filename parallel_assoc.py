import pandas as pd
import numpy as np
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import pyfpgrowth

import time
# reading file as lines of string
with open("transaction.txt") as file:
    default=file.read().splitlines()

# converting the strings into list type
data=[]
for s in default:
    data.append(list(map(str,s.split(';'))))
# dataNew = pd.get_dummies(data)

# converting the dataset into one hot trnasaction [0 if exist,1 in not]
oht = OnehotTransactions()
dataNew = oht.fit(data).transform(data)
dataNew=pd.DataFrame(dataNew,columns=oht.columns_)


# print(dataNew.head())
# apriori algorithm, parameter are give
t1=time.time()
frequent_itemsets = apriori(dataNew, min_support=0.1, use_colnames=True) 
assoc_rules=association_rules(frequent_itemsets, metric="lift", min_threshold=0.1)
print("using apriori : {}".format(time.time()-t1))
print(frequent_itemsets)
print(assoc_rules)

t2=time.time()
frequent_itemsets=pyfpgrowth.find_frequent_patterns(data,7718)
rules = pyfpgrowth.generate_association_rules(frequent_itemsets, 0.1)
print("using fp_growth : {}".format(time.time()-t2))
print(frequent_itemsets)
print(rules)



