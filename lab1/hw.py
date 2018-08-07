# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:40:31 2018

@author: kirito
"""
# find mean, median and mode of integers in a list

def mean(a):
    sum = 0
    #print("calling my mean")
    for x in a:
        sum = sum + x
    return sum/len(a)

def median(b):
    #to keep b unaffected for further processing
    a = sorted(b)
    list_length = len(a)
    if(list_length % 2 == 0):
        return (a[int((list_length/2) - 1)] + a[int((list_length)/2)] ) / 2
    else:
        return a[int(list_length/2)]

def mode(a):
    freq_table = {}
    mode_element = 0
    mode_count = 0
    for x in a:
        if x not in freq_table:
            freq_table[x] = 1
        else:
            freq_table[x] = freq_table[x] + 1
        if(mode_count < freq_table[x]):
            mode_count = freq_table[x]
            mode_element = x
    return [mode_element, mode_count]

def multiple_modes(a):
    freq_table = {}
    for x in a:
        if x not in freq_table:
            freq_table[x] = 1
        else:
            freq_table[x] = freq_table[x] + 1
    freq = sorted(freq_table.values(), reverse = True)
    max_mode_count = freq[0]
    mode_list = []
    for x,v in freq_table.items():
        if(v == max_mode_count):
            mode_list.append(x)
    return mode_list

import numpy as np
import statistics as st

MIN = -10
MAX = +10
LIST_SIZE = 100

mylist = np.random.randint(MIN,MAX,LIST_SIZE)

print(mean(mylist), end = "\t|\t")     
print(st.mean(mylist))

print(median(mylist), end = "\t|\t")
print(st.median(mylist))

print(mode(mylist), end = " \t|\t")
try:
    print(st.mode(mylist))
except st.StatisticsError as st_err :
    print("StatisticsError: {0}".format(st_err))
except :
    print("unknown error")

print(multiple_modes(mylist))