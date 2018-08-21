# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:02:27 2018

@author: Student
"""

import csv #for importing csv data file
from itertools import combinations #for print_rules method
import pyfpgrowth
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

#Read the CSV file into the python environment
data_list = []
with open('a2q2_data.csv', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    field_headings = data_list[0]
    data_list.remove(data_list[0])

#print raw data
print(field_headings)
for record in data_list:
    print(record)

#convert table to transaction records
transactions = []
i = 1
element = set()
for record in data_list:
    for i in range(1,5):
        if record[i] == '1':
            element.add(str(i))
    key = ''.join(str(i) for i in element)
    transactions.append(key)
    element = set()

transactions = data_list
patterns = pyfpgrowth.find_frequent_patterns(transactions, 1)
print(patterns)
rules = pyfpgrowth.generate_association_rules(patterns, 0)
print(rules)
df = pd.DataFrame.from_dict(rules,orient='index')
print(df)
