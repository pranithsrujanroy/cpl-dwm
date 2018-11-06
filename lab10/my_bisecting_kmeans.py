'''
apply kmeans clustering for iris dataset
status: incorrect implementation
'number of trials' is not implemented!

'''

import numpy as np
from sklearn.datasets import load_iris
from random import randint

def dist(x1, x2):
    return np.sqrt(np.sum(((x1-x2)*(x1-x2))))

def findcentroid(c):
    return np.sum(np.asarray(c),axis=0)/len(c)

def cluster(X, k1,k2,c1,c2):
    m=X.shape[0]
    for i in range(0,m):
       d1 = dist(X[i],k1)
       d2 = dist(X[i],k2)
       d = min(d1,d2)
       if(d==d1):
           c1.append(X[i])
       elif(d==d2):
           c2.append(X[i])
    kn1 = findcentroid(c1)
    kn2 = findcentroid(c2)
    return kn1,kn2
     
def kmeans(X,k):
    upper_limit = len(X) - 1
    if upper_limit <= 1:
        upper_limit = 0
    k1 = randint(0,upper_limit)
    k2 = randint(0,upper_limit)
    #k3 = randint(1,len(X))
    #print(k1,k2)
    c1 = []
    c2 = []
    kn1,kn2 = X[k1], X[k2]
    while(True):
        n1,n2 = cluster(X,kn1,kn2,c1,c2);
        if n1.all()==kn1.all() and n2.all()==kn2.all():
            break
        kn1,kn2=n1,n2
    #print("c1:", kn1)
    print(len(c1),len(c2))
    #print("c2:", kn2)
    #print(len(c2),"\n")
    
    return [c1,c2]

def cluster_se(cluster):
    centroid = findcentroid(cluster)
    sum = 0
    for point in cluster:
        sum = sum + dist(point,centroid)
    return sum

def calc_sse(clusters):
    sse = 0
    for c in clusters:
        error = cluster_se(c)
        sse = sse + error
    return sse
    
iris = load_iris()
X_all = iris.data
y= iris.target
k=2
NUM_CLUSTERS = 3
l = 2
u = l+1

X_1 = [x[l] for x in X_all]
X_2 = [x[u] for x in X_all]
X_input = [x[l:u+1] for x in X_all]   #input only first two columns

clusters = kmeans(np.array(X_input),k)

for counter in range(0,NUM_CLUSTERS-2):
    print("clusters:",len(clusters))
    sse = []
    for c in clusters:
        new_clusters = kmeans(np.array(c),k)
        sse.append(calc_sse(np.array(new_clusters)))
        
    
    print(sse)
    print(np.argmax(sse))
    index_of_cluster_to_break = np.argmax(sse)
    cluster_to_break = clusters[index_of_cluster_to_break]
    clusters.remove(cluster_to_break)
    new_clusters = kmeans(np.array(cluster_to_break),k)
    clusters.append(new_clusters[0])
    clusters.append(new_clusters[1])
    
def cluster_num(point):
    index = 0
    for c in clusters:
        index = index + 1
        list_c = []
        for p in c:
            list_c.append(list(p))
        #print(list_c)
        if list(point) in list_c:
            return index
print("\nNumber of clustesrs:",len(clusters))

for i in clusters:
    print(len(i))

color_array = []
for point in X_input:
    color_array.append(cluster_num(point))
import matplotlib.pyplot as plt
plt.scatter(X_1,X_2,c=color_array)
plt.title("using bisecting kmeans")
plt.show()
plt.scatter(X_1,X_2,c=y)
plt.title("actual")

print("cluster colors",set(color_array))