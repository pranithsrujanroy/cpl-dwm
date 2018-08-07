# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:33:08 2018

@author: kirito

Assignment 1
Question 3

Normalise the dataset using min max, z-score, decimal scaling normalization to the range (0-1).
"""
import math #for ceil in decimal scaling
import numpy as np  #for random list sample date generation

#dataset: array X with n values. n = 100 (LIST_SIZE)
MIN = -100
MAX = +100
LIST_SIZE = 100
X = np.random.randint(MIN,MAX,LIST_SIZE)

# min-max normalisation (feature scaling)
# X' = a + ((X - X_min) * (b - a)) / (X_max - X_min)
#source: https://en.wikipedia.org/wiki/Normalization_(statistics)
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

# z score normalisation
# ref: https://docs.tibco.com/pub/spotfire/6.5.1/doc/html/norm/norm_z_score.htm
def norm_z_score(X):
    len_x = len(X)
    avg = 0
    avg_sum = 0
    for i in X:
        avg_sum = avg_sum + i 
    avg = avg_sum / len_x
    
    std = 0
    sqr_sum = 0
    for i in X:
        sqr_sum = sqr_sum + (i-avg)**2
    if(sqr_sum == 0):
        return X
    std = ((1/(len_x - 1)) * sqr_sum ) ** (1/2)
    
    X_norm_z_score = []
    for i in X:
        X_norm_z_score.append((i - avg) / std)
    return X_norm_z_score

# decimal scaling
# ref:https://www.cs.indiana.edu/~predrag/classes/2005springi400/lecture_notes_4_1.pdf
def norm_decimal_scaling(X):
    X_max = max(X)
    factor = 10**math.ceil(math.log10(X_max))
    X_dec_scale = []
    for i in X:
        X_dec_scale.append(i/factor)
    return X_dec_scale

print(X)
print(norm_min_max(X))
print(norm_z_score(X))
print(norm_decimal_scaling(X))