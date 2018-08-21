# -*- coding: utf-8 -*-
#author: anubhav

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
dataset = [['A','B','C','D'],
           ['A','C','D',],
           ['A','B','C'],
           ['B','C','D'],
           ['A','B','C'],
           ['A','B','C'],
           ['C','D','E'],
           ['A','C']]
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
#print(df)
"print(apriori(df, min_support=0.6, use_colnames=True))"

val = apriori(df, min_support=0.5, use_colnames=True)
asr = association_rules(val, metric="confidence", min_threshold=0)
print(val)
print(asr)