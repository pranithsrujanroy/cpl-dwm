# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:43:21 2018

@author: Student
"""

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data[:,:]
y = iris.target
#==============================================================================
# for i in range(0,100):
#     if y[i]==0:
#         y[i]=1
#     else:
#         y[i]=0
#==============================================================================

import scipy.cluster.hierarchy as shc  
import matplotlib.pyplot as plt  
plt.figure(figsize=(10, 7))  
plt.title("Iris Dendograms")  
dend = shc.dendrogram(shc.linkage(X, method='ward'),orientation='top',color_threshold=10,truncate_mode='lastp',p=10)
plt.axhline(y=10, c='k')
plt.plot(0,10,'r--')
plt.show()

from sklearn.cluster import AgglomerativeClustering

cluster = AgglomerativeClustering(n_clusters=3 , affinity='euclidean', linkage='ward')  
cluster.fit_predict(X) 
#print(cluster.labels_)

#==============================================================================
# plt.figure(figsize=(10, 7))  
# plt.scatter(X[:,2], X[:,3], c=cluster.labels_, cmap='rainbow')
#==============================================================================
#==============================================================================
# misclassified = 0
# for i in range(0,150):
#     if y[i]!=cluster.labels_[i]:
#         misclassified += 1
# accuracy = (150-misclassified)/150.0
# print(accuracy)
#==============================================================================
