# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:18:27 2018

@author: 115CS0242
"""
import pandas as pd
import numpy as np
from sklearn import datasets
from scipy.cluster.hierarchy import linkage 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt  
from sklearn.cluster import KMeans 

#function for finding the centroid
def centroid(data):
    return np.mean(data, 0)
#function for calculating sse
def sse(data):
    u = centroid(data)
    return np.sum(np.linalg.norm(data - u, 2, 1))

#loading the iris dataset from sklearn
iris = datasets.load_iris()
#print(iris.data)
#separating the file into features 
X = iris.data
y = iris.target
#print(X)
plt.scatter(X[:,0],X[:,1], label='True Position')
#initiating the 1st split
X1, X2, y1, y2 = train_test_split(X, y,test_size=0.2)
#X2=X2.reshape(120,1)
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X2)  
X2_sse=sse(X2)
print(X2_sse)
print(len(X1))
print(len(X2))
#print(kmeans.cluster_centers_)  
#print(kmeans.labels_) 
#plt.scatter(X2[:,0],X2[:,1], c=kmeans.labels_) 
#X1, X2, y1, y1 = train_test_split(X, y,test_size=0.25 ,random_state = 1000)
#print(X1)
#print(X2)
X3, X4, y3, y4 = train_test_split(X1, y1,test_size=0.2 )
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X4)  
X4_sse=sse(X4)
print(X4_sse)
print(len(X3))
print(len(X4))

X5, X6, y5, y6 = train_test_split(X3, y3,test_size=0.2 )
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X4)  
X4_sse=sse(X4)
print(X4_sse)
print(len(X3))
print(len(X4))

X7, X8, y, y6 = train_test_split(X5, y5,test_size=0.2 )
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X4)  
X4_sse=sse(X4)
print(X4_sse)
print(len(X3))
print(len(X4))

X5, X6, y5, y6 = train_test_split(X3, y3,test_size=0.2 )
kmeans = KMeans(n_clusters=2)  
kmeans.fit(X4)  
X4_sse=sse(X4)
print(X4_sse)
print(len(X3))
print(len(X4))
