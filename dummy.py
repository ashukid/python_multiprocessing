#Python 3.5

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import time

# using pool for multiprocessing 
from multiprocessing import Pool




def apriori_without_multiprocessing(df):
	t1=time.time()
	frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
	frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
	print(frequent_itemsets)
	print("time taken = {}".format(time.time()-t1))


def apriori_with_multiprocessing(df):
	t2=time.time()

	# calculating the frequent itemset
	frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
	frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
	return frequent_itemsets


# file input part
filename = "combine.csv"
data = pd.read_csv(filename)
dataNew = pd.get_dummies(data)
df = pd.DataFrame(dataNew, columns=dataNew.columns)

# part 1
# apriori_with_multiprocessing(df)

#part 2
p=Pool(4)
print(p.map(apriori_without_multiprocessing,(df,)))
print("parallel time taken = {}".format(time.time()-t2))
p.close()
p.join()

