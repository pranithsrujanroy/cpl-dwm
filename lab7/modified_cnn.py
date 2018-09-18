# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:24:07 2018

@author: Student
STATUS : INCOMPLETE
EXTRA :
    MODIFIED CNN
    
    ALGO:
        1. Start with condensed set S. S contains one pattern from each class.
        2. G = ∅
        3. For each x ∈ T
            1. Classify x using NN considering S as training set.
            2. if x is misclassified then G = G ∪ {x}
        4. Find a representative pattern from each class in G; Let representative set is R.
        5. S = S ∪ R
        6. G = ∅
        7. Repeat Step 2 to Step 6 until there is no misclassification.
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

#CREATE CONDENSED SET
# Start with condensed set S. S contains one pattern from each class. (TODO)
S = [training_data[1]]
S_labels = [training_data_labels[1]]

# G = ∅
G = []
G_labels = []

# For each x ∈ T
for record,record_class in zip(training_data,training_data_labels):
    # Classify x using NN considering S as training set.
    nearest_neighbour,predicted_label = k_nearest_neighbours(record,1,S,S_labels)
    # if x is misclassified then G = G ∪ {x}
    if(predict(record,nearest_neighbour,predictd_label) != record_class):
        G = G + [record]
        G_labels = G_labels + [record_class]
    # Find a representative pattern from each class in G; Let representative set is R.
    

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
print("\nLength of condensed set : ", this_batch_len)

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

print("Accuracy with CNN on CAR EVALUATION DATASET : ",1-error)

