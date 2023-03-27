
import numpy as np
a=input("Give the elements of the array:").split(',')      #this separates inputs(type string)in commas and areate list out of them
lA=[float(i) for i in a]             #elements of list become float
b=input("Give the elements of the array:").split(',')
lB=[float(i) for i in b]
A=np.array(lA)        #making numpy array from the list as we can consider a vector as array
B=np.array(lB)
s=0             #initializing the summation value as 0
if len(A)==len(B):      #dot product will happen if the length if two arrays are same
    for i in range(len(A)):
        s+=A[i]*B[i]     #dot product i.e. element wise multiplication of same position for the arrays
        i+=1              
    print(s) 
else:
    print("The arrays are not of same length.")    



    