# -*- coding: utf-8 -*-
"""
DBSCAN clustering algorithm on IRIS dataset
Finds core samples of high density and expands clusters from them.
(modified with library of dbscan)
"""

"""
status : final
change DBSCAN parameters to adjust cluster numbers 
"""
print(__doc__)

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

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
X = X
labels_true = Y

db = DBSCAN(eps=0.2, min_samples=10,metric='euclidean').fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
# Plot result
import matplotlib.pyplot as plt

y_clusters = []
y_hs = []
x = []
eps_val = 0.05
for i in range(1,20):
    
    db = DBSCAN(eps=eps_val, min_samples=4,metric='euclidean').fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    hs = metrics.homogeneity_score(labels_true, labels)
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    
    eps_val = eps_val + 0.05
    y_clusters.append(n_clusters_)
    y_hs.append(hs)
    x.append(i)

plt.plot(x,y_clusters)
plt.plot(x,y_hs)
plt.title('DBSCAN')
plt.xlabel('iteration')
plt.ylabel('value')
plt.legend(['no of clusters','homogenity'])