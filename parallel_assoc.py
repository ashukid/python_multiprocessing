import pandas as pd
import numpy as np
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import pyfpgrowth

import time
# reading file as lines of string
with open("categories.txt") as file:
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
print(dataNew.head())

# print(dataNew.head())
# # apriori algorithm, parameter are given
# t1=time.time()
# frequent_itemsets = apriori(dataNew, min_support=0.1, use_colnames=True) 
# assoc_rules=association_rules(frequent_itemsets, metric="lift", min_threshold=0.1)
# print("using apriori : {}".format(time.time()-t1))
# # print(assoc_rules)

# # fp-growth algorithm, prameters are given
# t2=time.time()
# frequent_itemsets=pyfpgrowth.find_frequent_patterns(data,4000)
# rules = pyfpgrowth.generate_association_rules(frequent_itemsets, 0.1)
# print("using fp_growth : {}".format(time.time()-t2))
# print(frequent_itemsets)
# # print(rules)


support=[]
confidence=[]
antecedants=[]
consequents=[]

for i in rules.keys():
	antecedants.append(i)
	consequents.append(rules[i][0])
	confidence.append(rules[i][1])
	support.append(rules[i][1]*float(frequent_itemsets[i]/float(len(data))))

ante = []
for items in antecedants:
	temp=[]
	for j in items:
		x=j.split("=")
		temp.append(x[0])
	ante.append(temp)

conse=[]
for items in consequents:
	temp=[]
	for j in items:
		x=j.split("=")
		temp.append(x[0])
	conse.append(temp)

for i in range(len(confidence)):
    print('{} -> {} = {} | {}'.format(antecedants[i],consequents[i],support[i],confidence[i]))
