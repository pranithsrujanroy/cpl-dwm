# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:05:44 2018

@author: Student
STATUS : IN PROGRESS

Assignment 2
2. Find association rules using apriori algorithm for the data given in a2q2_data.csv with support > 0.5 and confidence > 0.5
"""

import csv #for importing csv data file
from itertools import combinations #for print_rules method


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
            element.add(i)
    key = ''.join(str(i) for i in element)
    transactions.append(key)
    element = set()

N = len(transactions) #total number of transactions
min_support = 0.5 
min_conf = 0.5
min_support_freq = N * min_support
min_confidence_count = N * min_conf
print(transactions)
items = {}  #store d ie the list of distinct elements
confidence = {}

#find frequent items
def find_frequent_items(transactions,min_support):
    """
        Takes in a list of transactions and returns a set of frequent elements
        from the records/transactions in the transactions database.
    """
    for record_no in range(N):    
        for i in list(transactions[record_no]):
            if i in items:
                items[i] += 1
            else:
                items[i] = 1
    frequent_items = set()
    for item, support in items.items():
        if support >= min_support_freq :
            if item not in frequent_items:
                frequent_items.add(item)
                #print(item)
                confidence[item] = support
    return frequent_items
#print(itemset)

#cartesian product function
def cartesian_product(this_set):
    """
    It takes a set of elements and returns the cartesian product of the set with itself where element considered is a single character
    """
    next_set = set()
    for i in this_set:
        for j in this_set:
            if i < j:
                element = ''.join(str(x) for x in(set(i) | set(j)))
                next_set.add(element)
    return next_set

def objectify(x):
    obj_list = []
    for e in x:
        for i in range(1,5):
            if str(e) == str(i):
                obj_list.append(field_headings[i])
    return obj_list

def print_rules(itemset,min_confidence_count):
    final_freq_elements = list(''.join(str(x) for x in(set(itemset))))
    final_set = set(final_freq_elements)
    final_obj_set = set(objectify(list(final_set)))
    for i in range(len(final_freq_elements) -1) :
        comb = combinations(final_freq_elements,i+1)
        for rule in (comb):
            lhs_key = (''.join(str(x) for x in((rule))))
            rule_conf =  (min_support_freq / confidence[lhs_key])
            if( rule_conf > min_conf):
                obj_rule = objectify(rule)
                print(set(obj_rule), "->", final_obj_set - set(obj_rule), rule_conf)

#Line 2
itemset = find_frequent_items(transactions,min_support)
#apriori algorithm
while itemset:    
    new_itemset = cartesian_product(itemset)
    previous_itemset = itemset 
    itemset = set()
    for candidate in new_itemset:
        count = 0
        for record_no in range(N):
            current_record_set = set(transactions[record_no])
            if set(candidate) <= current_record_set:
                count += 1
        if count>=min_support_freq:
            itemset.add(candidate)
            #print(candidate)
            confidence[candidate] = count

print_rules(previous_itemset,min_confidence_count)
