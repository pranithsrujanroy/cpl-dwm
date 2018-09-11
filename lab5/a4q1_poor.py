# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 13:39:00 2018

@author: Student
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

complete_data = data_list

def pre_process_data(string_data):
    convertor = {
        'vhigh': 1,'high': 2,
        'med' : 3,
        'low' : 4,
        '5more' : 6,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        'more' : 5,
        'small' : 2,
        'big' : 4,
        'unacc' : 1,
        'acc' : 2,
        'good' : 3,
        'vgood' : 4}
    clean_data = []
    for record in string_data:
        clean_record = []
        for attribute in record:
            clean_record.append(convertor[attribute])
        clean_data.append(clean_record)
    return clean_data

data_list = complete_data

print("Attribute headings are : ",field_headings)

#PREPROCESSING DATA
clean_data = pre_process_data(data_list)

TOTAL_RECORDS = len(clean_data)
TRAINING_SIZE = int(0.1 * TOTAL_RECORDS)
TESTING_SIZE = TOTAL_RECORDS - TRAINING_SIZE
print("TRAINING SIZE: ",TRAINING_SIZE, " TESTING SIZE : ",TESTING_SIZE)

#shuffle data
import random
clean_data_shuffled = clean_data
random.shuffle(clean_data_shuffled)

#divide data into two parts
training_data_list = clean_data_shuffled[0:TRAINING_SIZE]
testing_data_list = clean_data_shuffled[TRAINING_SIZE:TESTING_SIZE]

training_data = []
training_data_labels = []
for record in training_data_list:
    training_data.append(record[0:6])
    training_data_labels.append(record[6])

#build tree
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_data, training_data_labels)

#plot data
import graphviz
plot = tree.export_graphviz(clf,out_file=None,filled=True,leaves_parallel=False,proportion=True,rotate=True,rounded=True)
graph = graphviz.Source(plot)
graph.render("dt")

#testing model
testing_data = []
testing_data_labels = []
for record in testing_data_list:
    testing_data.append(record[0:6])
    testing_data_labels.append(record[6])

true_predictions = -1
false_predictions = -1
for record,label in zip(testing_data,testing_data_labels):
    pred = clf.predict_proba(record)
    #print(clf.predict_proba(record),label)
    if pred[0][label-1] == 1:
        true_predictions = true_predictions + 1
    else:
        false_predictions = false_predictions + 1
        
print("\n\nCorrect: ", true_predictions, " Incorrect : ",false_predictions, "Accuracy : ", true_predictions/(true_predictions+false_predictions), "\n\n\n\n")
