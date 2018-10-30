# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 13:35:44 2018

@author: Student

Assignment 7
Implement k means clustering algorithm on IRIS dataset.
k = 3

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

#SHUFFLE DATA
import random
#random.shuffle(data_list)


X = [x[0:4] for x in data_list[0:150]]
Y = [numify(x[4]) for x in data_list[0:150]]
X_labelled = []
for x,y in zip(X,Y):
    X_labelled.append(x + [y])
    
    
print(len(X_labelled[0]))
#print(X)
c1 = []
c2 = []
c3 = []
center = [c1, c2, c3]
for i in range(3):
    for j in range(len(X[0])):
        center[i].append(random.random())

def closest_center(record,centers):
    dist_list = []
    for center in centers:
        dist_list.append(record_distance(record,center))
    return dist_list.index(min(dist_list))

def k_means_cluster(X,centers,iter_count,X_labelled):
    clusters = [[],[],[]]
    for record,known_record in zip(X,X_labelled):
        cluster_num = closest_center(record,centers)
        clusters[cluster_num].append(known_record)
    
        
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    for cluster,i in zip(clusters,range(len(clusters))):
        for record in cluster:
            matrix[i][record[4]-1] = matrix[i][record[4]-1] + 1 
                
    print("confusion matrix: ",matrix)
    
    previous_centers = [[],[],[]]
    previous_centers = centers[:]
    #print("BEFORE LOOP",previous_centers)
    #print("\n\n")
    for i in (range(3)):
            #print(len(cluster))
            #print(" LOOP",previous_centers)
            #print("b",centers[i])
            centers[i] = centroid(clusters[i])
            #print("a",centers[i])

    #print("AFTER ", previous_centers)
    #print("\n\n")            
    sum_error = 0
    for p_c,c in zip(previous_centers, centers):
        sum_error = sum_error + euclidean_dist(p_c,c)
    avg_error = sum_error /3
    
    print("Iteration ",iter_count," Avg error: ",avg_error)
    
    if(avg_error < 0.00001):
        return clusters
    else:
        return k_means_cluster(X,centers,iter_count+1,X_labelled)
    
        #print(p_c,c)

clusters = k_means_cluster(X,center,0,X_labelled)

import matplotlib.pyplot as plt

matrix = [[0,0,0],[0,0,0],[0,0,0]]
for cluster,i in zip(clusters,range(len(clusters))):
    for record in cluster:
        matrix[i][record[4]-1] = matrix[i][record[4]-1] + 1 
            
print("confusion matrix: ",matrix)