#Python 3.5

import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import time

from multiprocessing import Pool


filename = "combine.csv"
data = pd.read_csv(filename)
dataNew = pd.get_dummies(data)

t1=time.time()
df = pd.DataFrame(dataNew, columns=dataNew.columns)
frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)
print("time taken = {}".format(time.time()-t1))

t2=time.time()

def func(df):
	frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)
	frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
	return frequent_itemsets


df = pd.DataFrame(dataNew, columns=dataNew.columns)
p=Pool(4)
print(p.map(func,))
print("parallel time taken = {}".format(time.time()-t2))
p.close()
p.join()

