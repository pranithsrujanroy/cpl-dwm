# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:54:10 2018

@author: Student
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

print("\nAccuracy with MODIFIED KNN on IRIS DATASET : ",1-error)