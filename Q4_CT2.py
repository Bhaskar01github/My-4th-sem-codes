# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:14:55 2023

@author: Shibashis
"""
Lo=[1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
Lt=[1, 3, 4, 4,  5, 7, 9, 10]
Lcs=[]
#Note that as the given lists are already sorted , so we don't have to think about the order of elements in each list to get acommon subsquence , i.e. The common subsequence boils down to be the list containing the common elements in the list (including multiplicity of each element taken to be in  consideration.)
for i in Lo:
    if i in Lt:
        Lt.remove(i)#removing  the common element from Lt in order to take care about  multiplicity of common elements.
        Lcs.append(i)
print(Lcs)       
