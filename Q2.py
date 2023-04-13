# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:05:03 2023

@author: Shibashis
"""

#Q2.
import numpy as np
import math
#Let's define two arbitary vector ,we could take user input also. But, the perocess would be fairly simple like this also.
A=np.array([1,2,3,4,5,6])
B=np.array([2,3,4,7,8,9])
def dot(C,D):
    if len(C)==len(D):
        return sum(C*D)
    else:
        return "The two vectors arenot the part of same vector spaces."
print("A.B=",dot(A,B))    
def cosine(C,D):
    if len(C)==len(D):
        return dot(C,D)/math.sqrt(sum(A**2)*sum(B**2))
    else:
        return "The vectors arenot part of the same vector spaces."
print("COS(A,B)=",cosine(A,B))   