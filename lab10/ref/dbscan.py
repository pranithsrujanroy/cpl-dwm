# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:00:11 2018

@author: Student

DBSCAN algorithm on IRIS dataset

STATUS: INCOMPLETE
"""


import csv #for importing csv data file
import helper

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
X = [x[0:4] for x in data_list[0:150]]
Y = [numify(x[4]) for x in data_list[0:150]]
X_labelled = []
for x,y in zip(X,Y):
    X_labelled.append(x + [y])

#find distance between points
distance_matrix = []
NUM_POINTS = len(X)
print(NUM_POINTS)
for i in range(0,NUM_POINTS):
	row = []
	for j in range(0,NUM_POINTS):
		row.append([0])
	distance_matrix.append(row)

for i in range(0,NUM_POINTS):
	for j in range(0,NUM_POINTS):
			distance_matrix[i][j] = record_distance(X[i],X[j])

print(distance_matrix)


