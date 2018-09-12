# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:55:52 2018

@author: Student
"""

import csv
import random
import math
import operator
# importing the required module 
import matplotlib.pyplot as plt

change = {'vhigh': 1,'high': 2,'med':3,'low':4,'small': 5,'big':6,'more':7,'5more':8}

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(6):
                if(dataset[x][y] in change):
                    dataset[x][y] = float(change[dataset[x][y]])
                else:
                    try:
                        dataset[x][y] = float(dataset[x][y])
                    except ValueError:
                        pass
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset('car.data', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    # generate predictions
    acc = []
    k_val = []
    max_acc = 0
    max_k = 0
    for k in range(1,25):
        predictions=[]
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            #print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '% for k-value: ',k)
        if(max_acc < accuracy):
            max_acc = accuracy
            max_k = k
        acc.append(100-accuracy)
        k_val.append(k)
    plt.plot(k_val,acc)
    plt.plot(max_k,100-max_acc,'X')
    plt.show()
    print("Accuracy is",max_acc,"% for K-Value:",max_k)
	
main()