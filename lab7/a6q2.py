# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:39:27 2018

@author: Student
Assignment 6
1. Implement Modified K-Nearest Neighbour.
Input : IRIS and Car Evaluation Dataset
Output : Classification Accuracy
"""


import csv #for importing csv data file
import helper_functions

#Read the CSV file into the python environment
data_list = []
with open('../lab5/data.txt', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    field_headings = data_list[0]
    data_list.remove(data_list[0])
print("Attribute headings are : ",field_headings)
complete_data = data_list


#PREPROCESSING DATA AND SHUFFLING
clean_data = pre_process_data(data_list)
import random
clean_data_shuffled = clean_data
random.shuffle(clean_data_shuffled)

TOTAL_RECORDS = len(clean_data)
TRAINING_SIZE = int(0.7 * TOTAL_RECORDS)
TESTING_SIZE = TOTAL_RECORDS - TRAINING_SIZE
print("TRAINING SIZE: ",TRAINING_SIZE, " TESTING SIZE : ",TESTING_SIZE)

#TESTING AND TRAINING DATA
training_data_list = clean_data_shuffled[0:TRAINING_SIZE]
testing_data_list = clean_data_shuffled[TRAINING_SIZE:TOTAL_RECORDS]
training_data = []
training_data_labels = []
for record in training_data_list:
    training_data.append(record[0:6])
    training_data_labels.append(record[6])
testing_data = []
testing_data_labels = []
for record in testing_data_list:
    testing_data.append(record[0:6])
    testing_data_labels.append(record[6])

error_matrix = []
k = 1
correct_classified = 0
incorrect_classified = 0
error = 0
for record,label in zip(testing_data,testing_data_labels):
    nearest_neighbours,labels = k_nearest_neighbours(record,k,training_data,training_data_labels)
    if(modified_knn_predict(record,nearest_neighbours,labels) == label):
        correct_classified = correct_classified + 1
        #print("S")
    else:
        incorrect_classified = incorrect_classified + 1
        #print("F")
error = incorrect_classified / (correct_classified + incorrect_classified)
error_matrix.append(error)
#print(k,error)

print("\nAccuracy with MODIFIED KNN on CAR EVALUATION DATASET : ",1-error)

