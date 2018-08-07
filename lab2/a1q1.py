# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:31:48 2018

@author: kirito

Assignment 1
Question 1

Create a CSV file with 5 features (PatientID, Age, Gender, TumorSize, HasCancer) and add information about 10 patients.
Note: Age in integer, Gender is Male/Female/ TumorSize is float, HasCancer is Boolean (TRUE/FALSE)
    a. Read the CSV file into the python environment
    b. Display the first 5 entries 
    c. Replace Male with 0 and Female with 1
    d. Replace True with 1 and False with 0 for 'HasCancer' feature
    e. Fill the missing values for 'Age' with average age.
    f. Replace missing value for 'TumorSize' with same tumor size as that of the 'mean' of the patients having same age.
    g. Save the new file basck to the disk with a new name.
"""
import csv 

def valid_age(age):
    if(age != ''):
        return True
    else:
        return False

def average(valid_ages):
    sum = 0
    for i in valid_ages:
        sum = sum + int(i)
    avg = sum//len(valid_ages)
    return avg

# a. Read the CSV file into the python environment
data_list = []
with open('data.csv', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    field_headings = data_list[0]
    data_list.remove(data_list[0])
    
    #b. Display first five entries
    for i in range(5):
        print(data_list[i])
    
    #c and d. Replace Male/Female with 0/1 and TRUE/FALSE with 1/0. Assumption: Structure of csv is known.
    for record in data_list:
        if(record[2].lower() == 'male'):
            record[2] = 0
        elif(record[2].lower() == 'female'):
            record[2] = 1
        
        if(record[4].lower() == 'true'):
            record[4] = 1
        elif(record[4].lower() == 'false'):
            record[4] = 0
         
    #e. Fill missing ages with avg ages
    valid_ages = []
    for record in data_list:
        if(valid_age(record[1])):
            valid_ages.append(record[1])
    avg_age = average(valid_ages)
    for record in data_list:
        if(not valid_age(record[1])):
            record[1] = str(avg_age)
    
    for row in data_list:
        print(row)
        
#f. write back
with open('data_clean.csv', 'wt',newline = '') as csvfile:
    write_obj = csv.writer(csvfile, delimiter = ',')
    write_obj.writerow(field_headings)
    for row in data_list:
        write_obj.writerow(row)