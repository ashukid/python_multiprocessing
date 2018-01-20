import pandas as pd
import numpy as np
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

import time


t=time.time()
with open("categories.txt") as file:
    default=file.read().splitlines()

data=[]
for s in default:
    data.append(list(map(str,s.split(';'))))
# dataNew = pd.get_dummies(data)
oht = OnehotTransactions()
dataNew = oht.fit(data).transform(data)
dataNew=pd.DataFrame(dataNew,columns=oht.columns_)


# print(dataNew.head())
frequent_itemsets = apriori(dataNew, min_support=0.01, use_colnames=True)
frequent_itemsets=np.array(frequent_itemsets)

# for i in range(len(frequent_itemsets)):
# 	print("{}:{}".format(int(frequent_itemsets[i][0]*len(data)),frequent_itemsets[i][1][0]))
# 	for j in range(1,len(frequent_itemsets[i][1])):
# 		print(";{}".format(frequent_itemsets[i][1][j]))

# writing in the text file
write_file=open("patterns.txt","w")
for i in range(len(frequent_itemsets)):
	write_file.write("{}:{}".format(int(frequent_itemsets[i][0]*len(data)),frequent_itemsets[i][1][0]))
	for j in range(1,len(frequent_itemsets[i][1])):
		write_file.write(";{}".format(frequent_itemsets[i][1][j]))
	write_file.write("\n")



# print("time taken by apriori = {}".format(time.time()-t))




