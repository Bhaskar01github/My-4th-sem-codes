#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:03:11 2023

@author: bb21ms147
"""
#We have copy pasted the previous question code so that we can work on the updated dataset (which is updated in Q2b)
import pandas as p

batdatabase = {'m1': [5, 20, 25, 40], 'm3': [15, 66, 50, 75], 'm2': [10, 40, 45, 50], 'names': ['rohit', 'rahul', 'virat', 'dinesh']}
bat = p.DataFrame(batdatabase , index = ['b1', 'b2', 'b3', 'b4'])
print(bat)

nrow = p.Series(data=[1,2,3,'Dhoni'], index=bat.columns, name='b5')   # here we are adding new row b5
bat = bat.append(nrow)
bat = bat.drop(labels=['b1'])
print(bat)

#Q2c starts here

bat['total'] = bat['m1'] + bat['m2']+bat['m3']
print(bat)
print("The column wise mean for acolumn 'm1' is given below:")
print(bat['m1'].mean())
print(f"The correlation between column 'm2' and column 'm3' is {bat['m2'].corr(bat['m3'])} ")

