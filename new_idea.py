import pandas as pd
import numpy as np
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

from multiprocessing import Pool
import time


with open("categories.txt") as file:
    default=file.read().splitlines()
data=[]
for s in default:
    data.append(list(map(str,s.split(';'))))
oht = OnehotTransactions()
dataNew = oht.fit(data).transform(data)
dataNew=pd.DataFrame(dataNew,columns=oht.columns_)


# dividing the input file into 4 different parts for parallel processing
length_of_input_file=len(data)
total_offset_count=4  # number of parallel process to run
offset=length_of_input_file/total_offset_count
dataNew1=dataNew.loc[:offset-1:]
dataNew2=dataNew.loc[offset:2*offset-1,:]
dataNew3=dataNew.loc[2*offset:3*offset-1,:]
dataNew4=dataNew.loc[3*offset:,:]

# Function that calculated the frequent dataset parallely
def calculate_frequent_itemset(fractional_data):
	ans=apriori(fractional_data, min_support=0.2, use_colnames=True) 
	return ans

# creating the pool object
# Map Part
# Mapping the input to different process object
p=Pool()
t1=time.time()
frequent_itemsets=p.map(calculate_frequent_itemset,(dataNew1,dataNew2,dataNew3,dataNew4))
p.close()
p.join()
print("time taken by apriori : {}".format(time.time()-t1))

# converting the parallel processed output to numpy arrays
frequent_itemsets1=frequent_itemsets[0]
frequent_itemsets2=frequent_itemsets[1]
frequent_itemsets3=frequent_itemsets[2]
frequent_itemsets4=frequent_itemsets[3]
frequent_itemsets1=np.array(frequent_itemsets1)
frequent_itemsets2=np.array(frequent_itemsets2)
frequent_itemsets3=np.array(frequent_itemsets3)
frequent_itemsets4=np.array(frequent_itemsets4)
frequent_dict1={}
frequent_dict2={}
frequent_dict3={}
frequent_dict4={}

# Reduce part
# calculating the unique count of each element fron transaction table by joing from 4 different tables
unique=set()
for i in range(len(frequent_itemsets1)):
	frequent_dict1[tuple(frequent_itemsets1[i][1])]=frequent_itemsets1[i][0]
	unique.add(tuple(frequent_itemsets1[i][1]))
for i in range(len(frequent_itemsets2)):
	frequent_dict2[tuple(frequent_itemsets2[i][1])]=frequent_itemsets2[i][0]
	unique.add(tuple(frequent_itemsets2[i][1]))
for i in range(len(frequent_itemsets3)):
	frequent_dict2[tuple(frequent_itemsets3[i][1])]=frequent_itemsets3[i][0]
	unique.add(tuple(frequent_itemsets3[i][1]))
for i in range(len(frequent_itemsets4)):
	frequent_dict2[tuple(frequent_itemsets4[i][1])]=frequent_itemsets4[i][0]
	unique.add(tuple(frequent_itemsets4[i][1]))


# final joining part
final_support=[]
final_itemsets=[]
unique=list(unique)
for i in range(len(unique)):
	total_count=0
	if(unique[i] in frequent_dict1.keys()):
		total_count+=(frequent_dict1[unique[i]]*offset)
	if(unique[i] in frequent_dict2.keys()):
		total_count+=(frequent_dict2[unique[i]]*offset)
	if(unique[i] in frequent_dict3.keys()):
		total_count+=(frequent_dict3[unique[i]]*offset)
	if(unique[i] in frequent_dict4.keys()):
		total_count+=(frequent_dict4[unique[i]]*offset)
	final_support.append(total_count/float(length_of_input_file))
	final_itemsets.append(list(unique[i]))

# print(final_itemsets,final_support)
final_frequent_itemsets=pd.DataFrame({'support':final_support,'itemsets':final_itemsets})
print(final_frequent_itemsets.head())
assoc_rules=association_rules(final_frequent_itemsets, metric="lift", min_threshold=0.1)
print(assoc_rules)


if __name__ == '__main__':
    freeze_support()
