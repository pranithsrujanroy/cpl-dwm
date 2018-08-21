# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:36:15 2018

@author: Student
"""

import pandas as pd

def subsets(s):
    sets = []
    subset = ''
    for i in range(1 << len(s)):
        for bit in range(len(s)):
            if is_bit_set(i, bit):
                subset = subset + s[bit] 
        sets.append(subset)
        subset = ''
    return sets

def is_bit_set(num, bit):
    return num & (1 << bit) > 0  


df = pd.read_csv('a2q1_sgs_data.csv')
df1 = df.iloc[:,1:]

minsup = 0.5*(len(df1))
val ={}
sarila = {}
last_val = {}
data = []
for i in range(len(df1)):
    #print(df1.iloc[i][0])
    data.append(df1.iloc[i][0])
    for j in range(len(df1.iloc[i][0])):
        if df1.iloc[i][0][j] in val:
            val[df1.iloc[i][0][j]] = val[df1.iloc[i][0][j]] + 1
        else:
            val[df1.iloc[i][0][j]] = 1
#print(data)
print(val)
new_val = []
goku=5
while len(val)>1 :
    temp = val.copy()
    goku = goku - 1
    for key, value in temp.items():
        if value < minsup:
            #val.pop(key,None)
            del val[key]
    print(val)

    for key,value in val.items():
        for l_key,l_value in val.items():
            c = set(key+l_key)
            c = list(c)
            #print(c)
            d = ''
            for g in range(len(c)):
                d = d + c[g]
            if l_key != key and ((d not in new_val) and (d not in new_val)):
                new_val.append(d)
    #print(new_val)
    sarila.update(val)
    last_val = val.copy()
    val.clear()
    for i in range(len(new_val)):
        new_data = set(new_val[i])
        for j in range(len(data)):
            old_data = set(data[j])
            if new_data.issubset(old_data):
                if(new_val[i] in val):
                    val[new_val[i]] = val[new_val[i]] + 1
                else:
                    val[new_val[i]] = 1
    #print(new_val)
    new_val.clear()
    print(val)
print(last_val)
print(sarila)  

l = {}
for key,value in last_val.items():
    if len(key)!=1:
        x = subsets(key)
        for i in range(len(x)):
            if len(x[i])!=0 and len(x[i])!=len(key):
                conf = value/sarila[x[i]]
                ide = {x[i] : conf}
                l.update(ide)
print(l)
                
 
            
          
                
            
        