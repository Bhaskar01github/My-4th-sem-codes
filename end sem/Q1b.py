#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:16:00 2023

@author: bb21ms147
"""
 #newton raphson method for root finding
 #from Q1a we get that the root of the equation lies in between 0.5 and 0.6000000000000001
 
import math
def f(x):
  return math.sin(x)-1+x
def df(x):
  return math.cos(x)+1
a=float(input("enter the intital guess of the root :"))
i=(f(a)/df(a))
x=a
while i>0.001:
    x=x-i
    i=(f(x)/df(x))
print("Root with better approximation:"+"%0.3f"%x)

