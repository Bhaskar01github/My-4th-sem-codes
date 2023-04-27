#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:48:13 2023

@author: bb21ms147
"""
l1=[]
l2=[]
str_1=input("Give me a bit string:")
str_2=input('Give me a bit string:')
for i in str_1:
    l1.append(int(i))
for i in str_2:
    l2.append(int(i))   
if len(str_1)!=len(str_2):
    print("They are not of same length,so Give string of same length")
else:
    L2=l2.copy()
    L1=l1.copy()
    p=int(input('tell me the place of crossover:'))
    del L1[p:len(l1)]
    del L2[p:len(l1)]
    ls1=L1
    ls2=L2
    for i in range(p,len(l2)):
        ls1.append(l2[i])
        ls2.append(l1[i])
    strls1=[str(i) for i in ls1] 
    strls2=[str(i) for i in ls2] 
    string1=''.join(strls1) 
    string2=''.join(strls2)
    print(string1)
    print(string2)
#    for i in range(p,len(l1)):
              
        