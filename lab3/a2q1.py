# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:31:31 2018

@author: kirito

Assignment 2
1. Find the rules with support 0.5 and confidence 0.5 in the following databases using Apriori algorithm.

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
"""
#ref1 : https://www3.cs.stonybrook.edu/~cse634/lecture_notes/07apriori.pdf
#ref2 : http://software.ucv.ro/~cmihaescu/ro/teaching/AIR/docs/Lab8-Apriori.pdf

#assumption: each item cqn appear 0 or 1 time in a transaction

transactions = ['ABCD','ACD', 'ABC', 'BCD', 'ABC', 'ABC', 'CDE', 'AC']
N = len(transactions) #total number of transactions
min_support = 0.5 
min_support_freq = N * min_support

print(transactions)

items = {}  #store d ie the list of distinct elements

#find frequent items
def find_frequent_items(transactions,min_support):
    """
        Takes in a list of transactions and returns a list of frequent elements
        from the records/transactions in the transactions database.
    """
    for record_no in range(N):    
        for i in list(transactions[record_no]):
            if i in items:
                items[i] += 1
            else:
                items[i] = 1
    frequent_items = []
    for item, support in items.items():
        if support >= min_support_freq :
            frequent_items.append(item)
    return frequent_items


itemset = find_frequent_items(transactions,min_support)

for i in range(2):
    #cartesian product
    new_itemset = []
    for i in itemset:
        for j in itemset:
            if i<j:
                new_itemset.append(i+j)
    previous_itemset = itemset 
    itemset = []
    for candidate in new_itemset:
        count = 0
        for record_no in range(N):
            current_record_set = set(transactions[record_no])
            if set(candidate) <= current_record_set:
                count += 1
        if count>=min_support_freq:
            itemset.append(candidate)        
    print("Itemset: " , itemset)
    print("previous_itemset: ",previous_itemset)
    




