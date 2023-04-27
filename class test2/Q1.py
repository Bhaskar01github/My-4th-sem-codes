#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:30:31 2023

@author: bb21ms147
"""
#j+c+a=612
#2j+3c-5a=144
#5j-4c-3a=0
import numpy as np 
A=np.array([[1,1,1],[2,3,-5],[5,-4,-3]])
B=np.array([612,144,0])
print(np.linalg.solve(A,B))