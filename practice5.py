import numpy as np
'''arr=np.array([[1,2,3], [4, 5, 6]] )
for i in range(len(arr[0])):
   print(arr[:,i])'''
   
'''Define a function calc_area (using def) that takes a radius (r) and returns the area of a circle (use math.pi). Take a list radius_list containing five radii values and use calc_area to store the corresponding areas in another list area_list.'''
from math import pi   
def calc_area(r):
   return pi*r**2
   '''
#print(calc_area(2)) 
radius_list=[2,4,5,6,7]  
area_list=[]
for e in radius_list:
    area_list.append(calc_area(e))
print(area_list)    '''
   
''' Repeat the problem in (2) using a numpy array radius_np containing five radii values (same as in radius_list) to store the corresponding areas in another numpy array area_np.'''
'''area_list=[]
radius_np=np.array([2,4,5,6,7]) 
area_list.append(calc_area(radius_np))
print(area_list) '''
   
'''Input (using input()) a list of alternating names and ages e.g. [‘kripa’, ‘37’, ‘arun’, ‘45’, ‘dipa’, ‘40’] and create a dictionary such the (i, i+1)th elements 
(i = 0, 2, …) form the key value pairs. For the mentioned example, the dictionary will be  {‘kripa’: ‘37’, ‘arun’: ‘45’, ‘dipa’: ‘40’}'''
   
l=['kripa', '37', 'arun', '45', 'dipa', '40']  
l1=l[::2]
l2=l[1::2] 
print(l1,l2)
print(dict(zip(l1,l2)))
'''For the same input of (4), create a list of tuples of the (i, i+1)th elements (i = 0, 2, …) of the input list. For the mentioned example, the output list will be [('kripa', ‘37’), ('arun', ‘32’), ('dipa', ‘40)]'''

'''
tl=[]
for i in range(len(l1)):
   tl.append((l1[i],l2[i]))
print(tl)'''

'''Input (use input()) the roll number and marks of three courses for 5 students and store it in a dictionary (d) such that the roll number is the key and the marks are stored in a numpy array of type float64 (the type of a numpy array A can be changed to float64 type by A.astype(‘float64’)). For example, for a student with roll number ‘ms1901’ and marks 70, 80, 90, the dictionary entry will look like ‘ms1901’: array([70., 80., 90.])'''
for j in range(5):
   rollj=input("Your rollno:")
   l=[]
   for i in range(3):
      m=input("enter marks:")
      l.append(m)
      marr=np.array(l)
   thisdict=dict(rollj=marr)
print(thisdict)    

























   
   
   
   
   
   
   
   
