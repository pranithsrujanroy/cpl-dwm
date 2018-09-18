# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:37:18 2018

@author: Student
Assignment 6
1. Implement Condensed Nearest Neighbour.
Input : IRIS and Car Evaluation Dataset
Output : Classification Accuracy

ref : 
    1> Professor website : https://sites.google.com/site/patrabidyutkr/teaching/data-warehousing-and-mining-cs-425-1
    2> To understand basics of CNN : https://drive.google.com/file/d/0B6267cu1Rvu8SWtCVjJIOWc4TlE/view
    3> To understand modified CNN (used to understand representative pattern) : 
        https://www.ripublication.com/ijcir17/ijcirv13n2_13.pdf ;having reference#[12] which is this one:
            https://sci2s.ugr.es/keel/pdf/specific/articulo/Devi02.pdf
"""

""" 
CNN (Condensed Nearest Neighbour Algorithm)
T : Training Set
Each element of training set is a tuple of values of attributes and a associated class label.
1. S = {x}
2. For each x belonging to T - S :
    Classifiy x using Nearest Neighbour (simple with k = 1) with S as the training set.
    If x is misclassified, S = S + {x},
    else pass.
3. Repeat this step until no more changes in S
4. Use this S to predict class for testing samples.

S has two properties:
    1. It is a subset of original training set.
    2. It ensures 100% accuracy over the training set which is the source for deriving the
condensed set. 
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


x_condensed_set_length = []
y_accuracy = []

for i in range(10):
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
    
    #CREATE CONDENSED SET
    condensed_training_data = [training_data[1]]
    condensed_training_data_labels = [training_data_labels[1]]
    prev_batch_len = 0
    this_batch_len = 1
    while prev_batch_len != this_batch_len:    
        prev_batch_len = len(condensed_training_data)
        for record,record_class in zip(training_data,training_data_labels):
            nearest_neighbour,predicted_label = k_nearest_neighbours(record,1,condensed_training_data,condensed_training_data_labels)
            if(predict(record,nearest_neighbour,predicted_label) == record_class):
                pass
            else:
                condensed_training_data = condensed_training_data + [record]
                condensed_training_data_labels = condensed_training_data_labels + [record_class]
        this_batch_len = len(condensed_training_data)
        #print(prev_batch_len,this_batch_len)
    #print("\nLength of condensed set : ", this_batch_len)
    
    error_matrix = []
    k = 1
    correct_classified = 0
    incorrect_classified = 0
    error = 0
    for record,label in zip(testing_data,testing_data_labels):
        nearest_neighbours,labels = k_nearest_neighbours(record,k,condensed_training_data,condensed_training_data_labels)
        if(predict(record,nearest_neighbours,labels) == label):
            correct_classified = correct_classified + 1
            #print("S")
        else:
            incorrect_classified = incorrect_classified + 1
            #print("F")
    error = incorrect_classified / (correct_classified + incorrect_classified)
    error_matrix.append(error)
    #print(k,error)
    
    #print("Accuracy with CNN on CAR EVALUATION DATASET : ",1-error)
    
    x_condensed_set_length.append(this_batch_len)
    y_accuracy.append(1-error)

import matplotlib.pyplot as plt
import matplotlib

plt.ylim([0,1])
plt.xlim([0,500])
plt.scatter(x_condensed_set_length,y_accuracy)
print(y_accuracy)
