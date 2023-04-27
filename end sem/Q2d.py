#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:19:07 2023

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
#Q2d starts here
import matplotlib.pyplot as plt
bat.plot(kind='scatter', x='m1', y='m2')
plt.title("Plot of scores in match 2(m2) vs match 1(m1)")
plt.xlabel("scores in match 1(m1)")
plt.ylabel("scores in match 2(m2)")
plt.show()