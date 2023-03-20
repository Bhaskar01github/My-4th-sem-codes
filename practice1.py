"""
     your name (e.g. Tintin), age (e.g. 20) and roll number (e.g.  20MS1234 ) in three variables and print them separately and also together like Hello! My name is Tintin . I am 20 years old. My roll number is 20MS1234 using these variables. Use string concatenation. Also, use formatted output.
 
x='Bhaskar'
y='18'
z='21ms147'
print('Hello! My name is',x,'.','I am',y,'years old.','My roll number is',z,'.')
print('Hello! My name is {}.I am {} years old.My roll number is {}'.format(x,y,z))
#d) Take two number strings as input and print their sum
print(int(list('12')[0])+int(list('12')[1]))
x=str(input("Enter a no:"))
y=list(x)
t=0
i=0
#or i in range(len(y)):
while i<len(y):
        t=t+int(y[i])
        i+=1
print(t)   
#h) Store an integer, floating point number and character in different variables and print the data type of each variable.
x=147
f=99.9
print(type(x),type(f))

     """
 
def f(x):
    return 10**x + x - 4
import numpy as np
i=0.0
l=1.0

for x in np.arange(i,l+0.1,0.1):
  if f(x)*f(x+0.1)<0.0:
      print(f(x),f(x+0.1))
      print(x,x+0.1)
     
     
     
      












 
