# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:47:15 2018

@author: Student
"""
import math
import random

MISSING_FRACTION = 0.2
def missing(value):
    #returning 0 increases error - baseline
    return 0

    #returning exact value gives least error
    #return value
    
    #using average value
    
    
    
    #if no technique used just return the value
    return value

def pre_process_data(string_data):
    clean_data = []
    
    for record in string_data:
        clean_record = []
        for attribute in record:
            #clean_record.append(convertor[attribute])
            #clean_record.append(float(attribute))
            
            #simulate missing data
            if(random.random()< MISSING_FRACTION):
                clean_record.append(missing(float(attribute)))
            else:
                clean_record.append(float(attribute))
        clean_record[4] = int(clean_record[4])
        clean_data.append(clean_record)

    col0 = [x[0] for x in clean_data]
    col1 = [x[1] for x in clean_data]
    col2 = [x[2] for x in clean_data]
    col3 = [x[3] for x in clean_data]
    DATASET_SUM = sum(col0) + sum(col1) + sum(col2) + sum(col3)
    
    col0_max = max(col0)
    col0_min = min(col0)
    col1_max = max(col1)
    col1_min = min(col1)
    col2_max = max(col2)
    col2_min = min(col2)
    col3_max = max(col3)
    col3_min = min(col3)
    
    #print(col1.index(max(col1)))
    #print(max(col1))
    return clean_data,DATASET_SUM


def euclidean_dist(X, Y):
    if(len(X) != len(Y)):
        print("Vectors of different dimensions. Cannot compute distances")
        return -1
    square_sum = 0
    for i,j in zip(X,Y):
        square_sum = square_sum + (i-j)**2
    return math.sqrt(square_sum)

def record_distance(x1,x2):
    return euclidean_dist(x1,x2)

def k_nearest_neighbours(record,k,training_data,training_data_labels):
    distance_list = []
    for comp_record,label in zip(training_data,training_data_labels):
        distance_list.append([comp_record,record_distance(record,comp_record),label])
    distance_list.sort(key=lambda x : x[1],reverse=False)
    k_neighbours = []
    k_neighbours_label = []
    for i in range(k):
        d = distance_list[i]
        k_neighbours.append(d[0])
        k_neighbours_label.append(d[2])
    
    return k_neighbours,k_neighbours_label

def predict(record,nearest_neighbours,labels):
    #print(nearest_neighbours)
    #nearest_neighbours = testing_data[1:40]
    #labels = testing_data_labels[1:40]
    k_distance_list = []
    for neighbour in nearest_neighbours:
        k_distance_list.append(record_distance(record,neighbour))
    k_dist_max = max(k_distance_list)
    k_dist_min = min(k_distance_list)
    values = [0.0,0.0,0.0,0.0,0.0]
    for neighbour,label in zip(nearest_neighbours,labels):
        values[label] = values[label] + 1
        if(k_dist_max == k_dist_min):
            values[label] = values[label] + 1
        else:
            values[label] = values[label] + (k_dist_max - record_distance(record,neighbour) ) / (k_dist_max - k_dist_min)
    #print(values)
    pred_label = values.index(max(values))
    #print(pred_label)
    return pred_label
