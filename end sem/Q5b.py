#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:42:28 2023

@author: bb21ms147
"""

def cen(a):
    b=len(a)
    su=0
    c=[]
    for x in range(0,2):
     su=0
     for i in range(0,b):
        su=su+a[i][x]
     c.append(su/b)  
    return c
def distance(a,b):
    import math
    c=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return c
import matplotlib.pyplot as plt


x =[4,1.5,8.2,1.5,7.0,8.0,0.5,4.2,0.4]
y=[3.5,0.7,7.8,0.5,4.0,5.0,0.3,3.0,0.3]
plt.scatter(x, y)
plt.show()
from sklearn.cluster import KMeans

data = list(zip(x, y))
print(data)
location={data[0]:"Khan",data[1]:"Gonsalves",data[2]:"Lakhani",data[3]:"Adhikari",data[4]:"Asrani",data[5]:"Siddiqui",data[6]:"Ray",data[7]:"Gupta",data[8]:"Iyer"}
inertias = []
for i in range(1,9):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,9), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3)                  # from the elbow method we could see that the after x=3 the inertia is tending to constant so the proper no. of clusters will be 4
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()
labels=kmeans.predict(data)
print(labels)
dictionary={}
for i in range(len(labels)):
    if labels[i] in dictionary:
        dictionary[labels[i]].append(data[i])
    else:
        dictionary[labels[i]]=[data[i]]
print(dictionary) 
centroid={}
for i in range(3):
   centroid[i]=cen(dictionary[i])
print(centroid) 

#Q5b starts here      
new=input("enter the Customer name,his/her annual income and annual expenditure: ").split(",")
a=[float(new[1]),float(new[2])]
dis={}
for i in range(3):
    dis[i]=distance(centroid[i],a)
print("this is dis ",dis)    
find=0
for i in range(len(dis)):
    if dis[find]>dis[i]:
        find=i
    else:
        find=find  

         
for i in range(len(dictionary[find])):
    print(location[dictionary[find][i]])
    

