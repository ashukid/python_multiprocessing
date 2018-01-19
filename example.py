#Python 3.5


import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori

# Load CSV
import pandas

filename = "D:\\Audience_TF_100.csv"
data = pandas.read_csv(filename)

import pandas as pd
dataNew = pd.get_dummies(data)

df = pd.DataFrame(dataNew, columns=dataNew.columns)

frequent_itemsets = apriori(df, min_support=0.9, use_colnames=True)

frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

# Create patterns block to retreive latter
patterns = association_rules(frequent_itemsets, metric="lift", min_threshold=1.)
patterns