#1
import matplotlib.pyplot as plt
import numpy as np
'''
months=input("Give months: ").split(',')
listm=[int(i) for i in months]
m=np.array(listm)
print(type(m[0]))



rainfall=input("rainfall in each month: ").split(',')
lrainfall=[int(i) for i in rainfall]
r=np.array(lrainfall)
temperature=input("Give temp.: ").split(',')
ltemp=[int(i) for i in rainfall]             #for converting elements of list from str to int
t=np.array(ltemp)
plt.plot(m,r)






#q2&3

plt.xlabel('Months')



#q4
plt.subplot(2,1,1)
plt.title('rainfall')
plt.xlabel('months')
plt.ylabel('rainfall')
plt.pie(r,labels=m)


plt.subplot(2,1,2)
plt.title('temp.')
plt.xlabel('months')
plt.ylabel('temp.')
plt.pie(t,labels=m)

plt.show()'''

#q8
import random
n=int(input("times:"))
a=[]
l=[]
for i in range(n):
    random_number=random.random()
    if random_number<0.5:
       l.append(random_number)
    no_of_heads=len(l) 
    prob_heads=len(l)/n
    a.append(prob_heads)
print(l)





