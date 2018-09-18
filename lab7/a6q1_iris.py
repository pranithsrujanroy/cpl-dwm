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
    3> To understand modified CNN (used to understand representative pattern) : https://www.ripublication.com/ijcir17/ijcirv13n2_13.pdf
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
with open('iris/iris.csv', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    field_headings = data_list[0]
    data_list.remove(data_list[0])
#convert data from string to float
for i in range(len(data_list)):
    for j in range(4):
        data_list[i][j] = float(data_list[i][j])
def numify(a):
    if a == 'Iris-virginica':
        return 1
    if a == 'Iris-versicolor':
        return 2
    if a == 'Iris-setosa':
        return 3
def norm_min_max(X):
    a = 0
    b = 1
    X_min = min(X)
    X_max = max(X)
    if(X_min == X_max):
        return X
    X_minmax = []
    for i in X:
        norm_x = a + ((i - X_min) * (b - a)) / (X_max - X_min)
        X_minmax.append(norm_x)
    return X_minmax
col1 = [x[0] for x in data_list]
col2 = [x[1] for x in data_list]
col3 = [x[2] for x in data_list]
col4 = [x[3] for x in data_list]
col5 = [x[4] for x in data_list]
col1 = norm_min_max(col1)
col2 = norm_min_max(col2)
col3 = norm_min_max(col3)
col4 = norm_min_max(col4)
data_list = []
for c1,c2,c3,c4,c5 in zip(col1,col2,col3,col4,col5):
    data_list.append([c1,c2,c3,c4,c5])

#SHUFFLE DATA
import random
random.shuffle(data_list)

"""
Observation:
    If data is not shuffled, accuracy achieved is 100%
Note: comment out random.shuffle(data_list) to use unshuffled data.
"""
X1 = [x[0:4] for x in data_list[0:35]]
X2 = [x[0:4] for x in data_list[50:85]]
X3 = [x[0:4] for x in data_list[100:135]]
X = X1 + X2 + X3
Y1 = [numify(x[4]) for x in data_list[0:35]]
Y2 = [numify(x[4]) for x in data_list[50:85]]
Y3 = [numify(x[4]) for x in data_list[100:135]]
Y = Y1 + Y2 + Y3
#testing set of 15 samples unseen from each class
X1 = [x[0:4] for x in data_list[35:50]]
X2 = [x[0:4] for x in data_list[85:100]]
X3 = [x[0:4] for x in data_list[135:150]]
X_test = X1 + X2 + X3
Y1 = [numify(x[4]) for x in data_list[35:50]]
Y2 = [numify(x[4]) for x in data_list[85:100]]
Y3 = [numify(x[4]) for x in data_list[135:150]]
Y_test = Y1 + Y2 + Y3

print("TRAINING SIZE: ",len(X), " TESTING SIZE : ",len(X_test))

training_data = X
training_data_labels = Y
testing_data = X_test
testing_data_labels = Y_test

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

print("Accuracy with CNN on IRIS DATASET : ",1-error)