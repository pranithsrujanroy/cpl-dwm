# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:44:46 2018

@author: kirito
STATUS : incomplete, abandoned

Assignment 5
1. Use Hunt's Algorithm to create and test a decision tree on Car Evaluation Dataset.
ref: https://archive.ics.uci.edu/ml/datasets/car+evaluation
https://www-users.cs.umn.edu/~kumar001/dmbook/ch4.pdf
"""

import csv #for importing csv data file

#Read the CSV file into the python environment
data_list = []
with open('data.txt', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    field_headings = data_list[0]
    data_list.remove(data_list[0])

#print raw data
print(field_headings)
#print(record[0:3])
#data_list = data_list[0:50]    

#converting all strings to integers for applying any sort of data mining
from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
le5 = LabelEncoder()
le6 = LabelEncoder()
le7 = LabelEncoder()


le1.fit(["vhigh", "high", "med", "low"])
le2.fit(["vhigh", "high", "med", "low"])
le3.fit(["2","3","4","5","5more"])
le4.fit(["2","4","more"])
le5.fit(["small","med","big"])
le6.fit(["low","med","high"])
le7.fit(["unacc","acc","good","vgood"])

training_data = []
training_data_labels = []
processed_data = []

for record in data_list:
    #print(record)
    record[0] = le1.transform([record[0]])
    record[1] = le2.transform([record[1]])
    record[2] = le3.transform([record[2]])
    record[3] = le4.transform([record[3]])
    record[4] = le5.transform([record[4]])
    record[5] = le6.transform([record[5]])
    record[6] = le7.transform([record[6]])
    processed_data.append(record)
    training_data.append(record[0:6])
    training_data_labels.append(record[6])
    #print(record)
 
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_data, training_data_labels)

#print(processed_data[2],data_list[2])
#print(clf.predict_proba(processed_data[4][0:6]))


#==============================================================================
# import graphviz
# plot = tree.export_graphviz(clf,out_file=None)
# graph = graphviz.Source(plot)
# graph.render("dt")
#==============================================================================
