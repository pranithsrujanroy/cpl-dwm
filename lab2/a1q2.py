# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:32:18 2018

@author: kirito

Assignment 1
Question 2
Implement the similarity measures betweent wo arrays X and Y :
    a. Euclidean Distance
    b. Manhattan Distance
    c. Minkowski Distance
    
"""

import math


#X and Y are n-dimensional vectors. n = 5
X = [ 1 , 3 , 6 , 7 , 1]
Y = [0 , 1 , 6 , 8 , 9]

X = [ 1 , 1 , 10 , 1 , 1]
Y = [0 , 1 , 1 , 1 , 1]


def euclidean_dist(X, Y):
    if(len(X) != len(Y)):
        print("Vectors of different dimensions. Cannot compute distances")
        return -1
    square_sum = 0
    for i,j in zip(X,Y):
        square_sum = square_sum + (i-j)**2
    return math.sqrt(square_sum)

def manhattan_dist(X, Y):
    if(len(X) != len(Y)):
        print("Vectors of different dimensions. Cannot compute distances")
        return -1
    manhattan_sum = 0
    for i,j in zip(X,Y):
        manhattan_sum = manhattan_sum + math.fabs(i-j)
    return (manhattan_sum)


def minkowski_dist(X, Y, p):
    if(len(X) != len(Y)):
        print("Vectors of different dimensions. Cannot compute distances")
        return -1
    p_power_sum = 0
    for i,j in zip(X,Y):
        p_power_sum = p_power_sum + (i-j)**p
    return p_power_sum**(1/p)

print(euclidean_dist(X,Y))
print(manhattan_dist(X,Y))
print(minkowski_dist(X,Y,3))


