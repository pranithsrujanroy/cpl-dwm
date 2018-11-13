"""
HANDLING MISSING DATA 
"""
import csv #for importing csv data file
#import helper_functions
import math
import random

MISSING_FRACTION = 0.2
MISSING_PLACEHOLDER = 0
COL0_VALUE = 0
COL1_VALUE = 0
COL2_VALUE = 0
COL3_VALUE = 0

def missing(value):
    #returning 0 increases error - baseline
    
    #return MISSING_PLACEHOLDER

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
    col4 = [x[4] for x in clean_data]
    c0_sum = [0,0,0,0]
    c1_sum = [0,0,0,0]
    for record in clean_data:
        i2 = 0
        if record[4] == 0:
            for d in record[0:4]:
                c0_sum[i2] = c0_sum[i2] + d
                i2 = i2 + 1
        else:
            for d in record[0:4]:
                c1_sum[i2] = c1_sum[i2] + d
                i2 = i2 + 1
    DATASET_SUM = sum(col0) + sum(col1) + sum(col2) + sum(col3)
    COL0 = sum(col0)/len(col0)
    COL1 = sum(col1)/len(col1)
    COL2 = sum(col2)/len(col2)
    COL3 = sum(col3)/len(col3)
    l = len(col0)
    COL_REPLACE_0 = []
    COL_REPLACE_1 = []
    COL_REPLACE = [COL0,COL1,COL2,COL3]
    for ele1,ele2 in zip(c0_sum,c1_sum):
        COL_REPLACE_0.append(ele1/l)
        COL_REPLACE_1.append(ele2/l)
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
    return clean_data,DATASET_SUM,COL_REPLACE,COL_REPLACE_0,COL_REPLACE_1

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
    pred_label = values.index(max(values))
    return pred_label

#Read the CSV file into the python environment
data_list = []
with open('../test/data.txt', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
complete_data = data_list

#PREPROCESSING DATA AND SHUFFLING
clean_data,dsum,COL_REPLACE,COL_REPLACE_0,COL_REPLACE_1 = pre_process_data(data_list)



COL_REPLACE = COL_REPLACE + [0]
COL_REPLACE_0 = COL_REPLACE_0 + [0]
COL_REPLACE_1 = COL_REPLACE_1 + [0]
import random
clean_data_shuffled = clean_data
random.shuffle(clean_data_shuffled)

#handling missing data

def handle_missing(data):
    processed_data = []
    for record in data:
        clean_record = []
        i1 = 0
        for attribute in record:
            #simulate missing data
            if(attribute == MISSING_PLACEHOLDER):
                clean_record.append(COL_REPLACE[i1])
            else:
                clean_record.append(float(attribute))
            i1 = i1 + 1
        clean_record[4] = int(clean_record[4])
        processed_data.append(clean_record)
    return processed_data


def handle_missing_classwise(data):
    processed_data = []
    for record in data:
        clean_record = []
        i1 = 0
        for attribute in record:
            #simulate missing data
            if(attribute == MISSING_PLACEHOLDER):
                if(record[4] == 0):
                    clean_record.append(COL_REPLACE_0[i1])
                else:
                    clean_record.append(COL_REPLACE_1[i1])
            else:
                clean_record.append(float(attribute))
            i1 = i1 + 1
        clean_record[4] = int(clean_record[4])
        processed_data.append(clean_record)
    return processed_data

#clean_data = handle_missing(clean_data)
clean_data = handle_missing_classwise(clean_data)

TOTAL_RECORDS = len(clean_data)
TRAINING_SIZE = int(0.05 * TOTAL_RECORDS)
TESTING_SIZE = TOTAL_RECORDS - TRAINING_SIZE
#print("TRAINING SIZE: ",TRAINING_SIZE, " TESTING SIZE : ",TESTING_SIZE)

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
for k in range(1,10):
    #k = 5 #fix
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
    print("k:",k," error:",error)
    #print("k:",k," Correct:",correct_classified," Incorrect:",incorrect_classified," Error:",error," Accuracy:",1-error)
    
    
#print(error_matrix)

#import matplotlib.pylot as plt
#plt.xlabel("k")
#plt.ylabel("error")
#plt.plot(error_matrix)


