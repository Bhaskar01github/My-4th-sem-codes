#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:37:13 2023

@author: bb21ms147
"""

n = 5
x = [1994,1999,2006,2009,2018]

y = [7.8,6.5,7.7,7.6,6.0]

#as the relative difference of x- values are different we are using lagrange interpolation

   
value = 2017

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
	"is", round(result,1))  
