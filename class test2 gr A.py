#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
#3d-2w+h=17
#d+w+h=16
#d-w+h=6
d=np.array([[3,-2,1],[1,1,1],[1,-1,1]])
k=np.array([17,16,6])
print(np.linalg.solve(d,k))
print(d.ndim)
D=int(np.linalg.det(d))
a_0=np.array([[[17,-2,1],[16,1,1],[6,-1,1]]])
a_1=d=np.array([[[3,17,1],[1,16,1],[1,6,1]]])
a_2=d=np.array([[[3,-2,17],[1,1,16],[1,-1,6]]])
a=np.linalg.det(a_0)
b=np.linalg.det(a_1)
c=np.linalg.det(a_2)
print(int(a/D),round(float(b/D)),int(c/D))


# In[52]:


d=np.array([[3,-2,1],[1,1,1],[1,-1,1]])
k=np.array([17,16,6])
print(d.shape)
print(k.shape)

m=np.linalg.solve(d,k)
print(m)


# In[51]:


arr3d = np.array([[[1, 2], [4, 5]], [[6, 7], [8, 9]]])
print(arr3d)


# In[ ]:


for i in range(10):
    for j in range(i):


# In[45]:


import numpy as np
arr1 = np.array([[1, 2], [3, 5]])
arr2 = np.array([1, 2])
print("\nResult...\n",np.linalg.solve(arr1, arr2))


# In[77]:


s="< $ $ "
n=int(input("enter:"))

S=(n//6+1)*s

for i in range(n+1):
    if i==0:
        print(">")
    elif i==1:
        print("> >")
    elif i%3==0:
        print("> $",S[:2*i-4],"\b>")
    else:
        print(">",S[:2*i-2],"\b>")


# In[ ]:





# In[ ]:


s='@ # * # @ *'
st=s*


n=int(input("enter:"))
for i in range(n):
    


# In[73]:


def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i
    return f

# Number of values given
n = 5;
x = [ 2000, 2005, 2010, 2015, 2020 ]

# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)] for j in range(n)]

import math


# Displaying the forward difference table

y[0][0] = 600
y[1][0] = 650
y[2][0] = 665
y[3][0] = 600
y[4][0] = 585



# Calculating the forward difference
# table

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]


# Displaying the forward difference table
for i in range(n):
    print(x[i], end = "\t")
    for j in range(n - i):
        print(y[i][j], end = "\t")
    print("");


# Value to interpolate at
value = 2001

# initializing u and sum
yout = []
sum = y[0][0]
yout.append(sum)
u = (value - x[0]) / (x[1] - x[0])
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)

print("\nValue at", value,"is", round(sum, 6))


# In[76]:


n = 5;
x = [2000,2005,2010,2015,2020];

y = [600,650,665,600,585]



   
value = 2001

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
	"is", round(result, 6))  


# In[79]:


*
* *
& * &
* * * &
* & * * *
& * & * * *
& * & * * * &
* & * * * & * &
* * * & * & * * *
& * & * * * & * & *


# In[80]:


pattern = ["*", "* *", "& * &", "* * *", "* & * *", "& * & * *", "& * & * * *", "* & * * * & *", "* * * & * & * *", "& * & * * * & * & *"]

for p in pattern:
    print(p)

    


# In[81]:


for i in range(1, 10):
    for j in range(i):
        if i % 2 == 0:
            print("&", end=" ")
        else:
            print("*", end=" ")
    print()


# In[105]:


n=int(input('enter:'))
s='* * * & * & * * * '
S=s*n

for i in range(1,n+1):
    for j in  range(i):
        print(S[j])
    
    
    
         
      
      
           


# In[96]:


s="< $ $ "
n=int(input("enter:"))

S=(n//6+1)*s

for i in range(n+1):
    if i==0:
        print(">")
    elif i==1:
        print("> >")
    elif i%3==0:
        print("> $",S[:2*i-4],"\b>")
    else:
        print(">",S[:2*i-2],"\b>")


# In[87]:


s="bacd"
print(s[1:3])


# In[ ]:


s='abcdefghi'
from this string i want output like
a
bc
cde
fghi
write a code for this
    


# In[106]:


import numpy as np
a="*$*$"
b=int(input("enter the no of lines you want "))
c=b*a
c=list(c)
print(c)
m=0
for i in range(b+1):
    for j in range(0,i):
        print(c[m],end=" ")
        m+=1
    print("\n")


# In[109]:


import numpy as np
a="***$*$"
b=int(input("enter the no of lines you want "))
c=b*a
c=list(c)
print(c)
m=0
for i in range(b+1):
    for j in range(0,i):
        print(c[m],end=" ")
        m+=1
    print("\n")


# In[ ]:




