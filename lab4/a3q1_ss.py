# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:19:47 2018

@author: Student
"""
import math
from operator import itemgetter, attrgetter
import csv
attributes = [];
rows = [];
#writerow = [];

def odds_ratio(f11,f10,f01,f00):
    return (f11*f00)/(f10*f01)
    
def corelation(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (n*f11 - ((f11+f10)*(f01+f11)))/(((f11+f10)*(f01+f11)*(f00+f01)*(f00+f10))**(0.5))

def kappa(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (n*f11+n*f00-(f10+f11)*(f11+f01)-(f00+f01)*(f00+f10))/(n*n-(f11+f10)*(f11+f01)-(f00+f01)*(f00+f10))

def interest(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (n*f11)/((f10+f11)*(f11+f01))

def cosine(f11,f10,f01,f00):
    return (f11)/(((f11+f10)*(f01+f11))**(0.5))

def piatetsky(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (f11/n) - (((f10+f11)*(f01+f11))/(n*n))
    
def collective(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    a = (f11+f00)/((f10+f11)*(f01+f11)+(f00+f10)*(f00+f01))
    b = (n - (f10+f11)*(f01+f11) - (f00+f10)*(f00+f01))/(n-f11-f00)
    return a*b

def jaccard(f11,f10,f01,f00):
    return f11/((f10+f11)+(f01+f11)-f11)
    
def all_confidence(f11,f10,f01,f00):
    return min((f11/(f11+f10)),(f11/(f11+f01)))
    
def goodman(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (max(f00,f10)+max(f01,f11)-max((f10+f00),(f01+f11)))/(n - max((f10+f00),(f01+f11)))
    
def laplace(f11,f10,f01,f00):
    return (f11+1)/((f10+f11)+2)
    
def conviction(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return ((f11+f10)*(f00+f10))/(n*f10)    
    
def certainty(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return ((f11/(f10+f11))-((f01+f11)/n))/(1-((f01+f11)/n))

def added(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return((f11/(f10+f11))-((f01+f11)/n))

def jmeasure(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return ((f11/n)*math.log10((n*f11)/((f10+f11)*(f01+f11)))) + ((f10/n)*math.log10((n*f10)/((f10+f11)*(f00+f10))))
    
def gini(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return (((f10+f11)/n)*((f11/(f11+f10))**2 + (f10/(f11+f10))**2)) -((f01+f11)/n)**2 + (((f01+f00)/n)*((f01/(f01+f00))**2 + (f00/(f01+f00))**2)) -((f00+f10)/n)**2

def mi(f11,f10,f01,f00):
    n = f00+f01+f10+f11
    return ((f00/n)*math.log10)    
    
with open('database.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',');
    attributes = next(readCSV);
    print(("Attributes are: ", attributes));
    for row in readCSV:
        f11 = float(row[1])
        f10 = float(row[2])
        f01 = float(row[3])
        f00 = float(row[4])
        row.append(odds_ratio(f11,f10,f01,f00))
        row.append(corelation(f11,f10,f01,f00))
        row.append(kappa(f11,f10,f01,f00))
        row.append(interest(f11,f10,f01,f00))
        row.append(cosine(f11,f10,f01,f00))
        row.append(piatetsky(f11,f10,f01,f00))
        row.append(collective(f11,f10,f01,f00))
        row.append(jaccard(f11,f10,f01,f00))
        row.append(all_confidence(f11,f10,f01,f00))
        row.append(goodman(f11,f10,f01,f00))
        row.append(laplace(f11,f10,f01,f00))
        row.append(conviction(f11,f10,f01,f00))
        row.append(certainty(f11,f10,f01,f00))
        row.append(added(f11,f10,f01,f00))
        row.append(jmeasure(f11,f10,f01,f00))
        row.append(gini(f11,f10,f01,f00))
        rows.append(row)
    print(("Total number of rows: ", readCSV.line_num));

def ranking(db,b):
    new_table = sorted(db,key = itemgetter(b))
    ranklist = []
    for row in new_table:
        ranklist.append(row[0])
    return ranklist
    
print("`Symmetric Measures")  
print("Odds Ratio Rank List")
print(ranking(rows,5))
print("Corelation Rank List")
print(ranking(rows,6))
print("Kappa Rank List")
print(ranking(rows,7))
print("Interest Rank List")
print(ranking(rows,8))
print("Cosine Rank List")
print(ranking(rows,9))
print("Piatetsky-Sapiro Rank List")
print(ranking(rows,10))
print("Collective Strength Rank List")
print(ranking(rows,11))
print("Jaccard Rank List")
print(ranking(rows,12))
print("All-confidence Rank List")
print(ranking(rows,13))
print("")
print("")
print("Assymetric Measures")
print("Goodman-Kruskal Rank List")
print(ranking(rows,14))
print("Laplace Rank List")
print(ranking(rows,15))
print("Conviction Rank List")
print(ranking(rows,16))
print("Certainty Factor Rank List")
print(ranking(rows,17))
print("Added Value Rank List")
print(ranking(rows,18))
print("J-measure Rank List")
print(ranking(rows,19))
print("Gini-index Rank List")
print(ranking(rows,20))
