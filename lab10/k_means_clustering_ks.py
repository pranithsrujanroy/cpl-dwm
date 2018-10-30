'''
apply kmeans clustering for iris dataset

'''

import numpy as np
from sklearn.datasets import load_iris
from random import randint

def dist(x1, x2):
    return np.sqrt(np.sum(((x1-x2)*(x1-x2))))
    
def cluster(X, k1,k2):
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
     
def findcentroid(c):
    return np.sum(np.asarray(c),axis=0)/len(c)
    
def kmeans(X,k):
    k1 = randint(1,len(X))
    k2 = randint(1,len(X))
    #k3 = randint(1,len(X))
    print(k1,k2)
    kn1,kn2 = X[k1], X[k2]
    while(True):
        n1,n2 = cluster(X,kn1,kn2);
        if n1.all()==kn1.all() and n2.all()==kn2.all():
            break
        kn1,kn2=n1,n2
    print("c1:", kn1)
    print(len(c1))
    print("c2:", kn2)
    print(len(c2))
    
iris = load_iris()
X = iris.data

y= iris.target
c1=[]
c2=[]

k=2

kmeans(X,k)

