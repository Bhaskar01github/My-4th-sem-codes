# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 19:41:26 2023

@author: Shibashis

def first(n):
    a=''
    b=['$','<','$']
    for i in range(n-2):
        a=a+b[int(i%3)]+" "
    return '>'+" "+ a+ '>'
m=int(input("Length of the sequence."))
print(first(m))  
t=first(m).split(" ")  
for i in range(1,m):
    if i%3==1:
        del t[1]
        c=" ".join(t)
    elif i%3==2:
        del t[-2]
        c= " ".join(t)
    elif i%3==0:
        del t[-2]
        t.reverse()
        c=" ".join(t)
    print(c)
"""
#Q4.
a=[1,3,6,5,8,7,3,4,8,10] 
t=0
p=0
for i in a:
    if i%2==0:
        print(i)
        if i>t:
            p=t
            t=i
        elif p<i<t:
            p=i
print("The Second largest element of the list will be =",p )
#Q1.
#If you multiply the number of dark avored toes by 3,
'''deduct twice the number of white 
avored to
ees from it and add the number of hazelnut 
avored
to
ees to it, you get 17. The sum of the number of dark, white and hazelnut to
ees is 16. Finally, if you
consider the number of dark 
avored to
ees, deduct the number of white 
avored to
ees from it and
add the number of hazelnut 
avored to
ees to it, you get 6.'''
import numpy as np
a=np.array([[3,-2,1],[1,1,1],[1,-1,1]])
print(np.linalg.solve(a,np.array([17,16,6])))
#
n = 6
x = [2009 ,2010,2011,2012,2013,2015 ]

y = [166.6,473.2,426.7,318.3,389.5,458.5]


import math

#for v in x:
#    y.append(math.sin(math.radians(v)))

print(y)    
value = 2014

result = 0.0
for i in range(n):

	# Compute individual terms of above formula
	term = y[i]
	for j in range(n):
		if j != i:
			term = term * (value - x[j]) / (x[i] - x[j])

	# Add current term to result
	result += term

print("\nValue at", value,
	"is", round(result, 6))    
     

        
        
