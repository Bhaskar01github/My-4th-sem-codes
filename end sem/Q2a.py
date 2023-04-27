#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:33:39 2023

@author: bb21ms147
"""
import pandas as p
m1=[int(i) for i in input(f"Enter the scores of match 1:").split(',')]  #Here for all inputs you are asked to give coma separated four inputs 
m2=[int(i) for i in input(f"Enter the scores of match 2:").split(',')]
m3=[int(i) for i in input(f"Enter the scores of match 3:").split(',')]
names =[str(i) for i in input(f"Enter the names of four batsmen:").split(',')]


batdatabase = {}                          # Defining a empty dictionary
batdatabase['m1'] = m1
batdatabase['m3'] = m3
batdatabase['m2'] = m2
batdatabase['names'] = names


print(batdatabase)

bat = p.DataFrame(batdatabase , index = ['b1', 'b2', 'b3', 'b4'])
print(bat)


