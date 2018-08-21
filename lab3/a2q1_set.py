# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:07:06 2018

@author: Student
"""

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
    return frequent_items


#Line 2
itemset = find_frequent_items(transactions,min_support)

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

#print(cartesian_product(cartesian_product(cartesian_product(cartesian_product(cartesian_product(cartesian_product(itemset)))))))

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
    #print("Itemset: " , itemset)
    #print("previous_itemset: ",previous_itemset)

from itertools import combinations
def print_rules(itemset):
    final_freq_elements = list(''.join(str(x) for x in(set(itemset))))
    final_set = set(final_freq_elements)
    for i in range(len(final_freq_elements) -1) :
        comb = combinations(final_freq_elements,i+1)
        for rule in (comb):
            print(set(rule), "->", final_set - set(rule))

print_rules(previous_itemset)

#a = (set('ab') | set('bc'))
#print(''.join(str(x) for x in a))
