# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:42:59 2023

@author: Shibashis
"""

#They total have
#62 test wins. If you add the wins of Azhar and Sourav and deduct that of Dhoni from it, you get 8.
#However, if you add the wins of Sourav and Dhoni and deduct that of Azhar from it, you get 34.
import numpy as np
a=np.array([[1,1,1],[1,-1,1],[-1,1,1]])#Defining array of co.efficients of variables
b=np.array([62,8,34])#assigning RHS matrix
c=np.linalg.solve(a,b)
print("The matches win by Azhar  =%s  , Dhoni =%s  and Sourav is = %s "%(c[0],c[1],c[2]))
