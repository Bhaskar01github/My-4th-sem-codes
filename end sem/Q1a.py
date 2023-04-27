#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:03:56 2023

@author: bb21ms147
"""

#Tabular Method for function f(x)=sin(x)-1+x in interval [0,1]
import numpy as np
import math
def f(x):
    return math.sin(x)-1+x

partition= np.arange(0,1+0.1,0.1)   #Here  array starts from 0 with gap of 0.1 till 1


for i in range(len(partition)-1):
    if f(partition[i])*f(partition[i+1]) <= 0:         #we are checking whether the function at x=i and x=i+1 has different signs (here i is an index).if they have different signs then we can say that f(x)=0 lies in between them
        print(f"Root lies between {partition[i]} and {partition[i+1]}")
