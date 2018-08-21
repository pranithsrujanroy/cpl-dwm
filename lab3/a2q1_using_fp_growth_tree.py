# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:07:41 2018

@author: kirito

Assignment 2
1. Find the rules with support 0.5 and confidence 0.5 in the following databases using FP-growth tree method.

------------------
TID | Transaction
------------------
1   | ABCD
2   | ACD
3   | ABC
4   | BCD
5   | ABC
6   | ABC
7   | CDE
8   | AC
------------------

ref for library used: https://github.com/conda-forge/pyfpgrowth-feedstock
ref for code of library used: https://github.com/evandempsey/fp-growth
"""
import pyfpgrowth
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

transactions = ['ABCD','ACD', 'ABC', 'BCD', 'ABC', 'ABC', 'CDE', 'AC']
patterns = pyfpgrowth.find_frequent_patterns(transactions, 4)
print(patterns)
rules = pyfpgrowth.generate_association_rules(patterns, 0.5)
print(rules)
df = pd.DataFrame.from_dict(rules,orient='index')
print(df)