# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:29:39 2018

@author: Student
Assignment 5
1. Find a suitable value of k for a given dataset " CAR EVALUATION DATASET". Use the obtained K-value for developing KNN Classifier.
Report the classification accuracy.
"""

import csv #for importing csv data file
import helper_functions

#Read the CSV file into the python environment
data_list = []
with open('../test/data.txt', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    #field_headings = data_list[0]
    #data_list.remove(data_list[0])
#print("Attribute headings are : ",field_headings)
complete_data = data_list

#PREPROCESSING DATA AND SHUFFLING
clean_data,dsum = pre_process_data(data_list)
#clean_data = data_list
import random
clean_data_shuffled = clean_data
random.shuffle(clean_data_shuffled)

print(clean_data[2])


TOTAL_RECORDS = len(clean_data)
TRAINING_SIZE = int(0.05 * TOTAL_RECORDS)
TESTING_SIZE = TOTAL_RECORDS - TRAINING_SIZE
print("TRAINING SIZE: ",TRAINING_SIZE, " TESTING SIZE : ",TESTING_SIZE)

#TESTING AND TRAINING DATA
training_data_list = clean_data_shuffled[0:TRAINING_SIZE]
testing_data_list = clean_data_shuffled[TRAINING_SIZE:TOTAL_RECORDS]
training_data = []
training_data_labels = []
for record in training_data_list:
    training_data.append(record[0:4])
    training_data_labels.append(record[4])
testing_data = []
testing_data_labels = []
for record in testing_data_list:
    testing_data.append(record[0:4])
    testing_data_labels.append(record[4])

#CALCULATING k
error_matrix = []
for k in range(1,2):
    k = 5 #found 
    correct_classified = 0
    incorrect_classified = 0
    error = 0
    for record,label in zip(testing_data,testing_data_labels):
        nearest_neighbours,labels = k_nearest_neighbours(record,k,training_data,training_data_labels)
        pred_label = predict(record,nearest_neighbours,labels)
        if(pred_label == label):
            correct_classified = correct_classified + 1
            #print("S")
        else:
            incorrect_classified = incorrect_classified + 1
            #print("F")
        #print(pred_label,label)
    error = incorrect_classified / (correct_classified + incorrect_classified)
    error_matrix.append(error)
    print(k,error)
    #print("k:",k," Correct:",correct_classified," Incorrect:",incorrect_classified," Error:",error," Accuracy:",1-error)
    
    
#print(error_matrix)

#import matplotlib.pylot as plt
#plt.xlabel("k")
#plt.ylabel("error")
#plt.plot(error_matrix)


