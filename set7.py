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
'''
Consider a trial of tossing an unbiased coin n (a large value) times. 
Use random.random() [generates a random float number between 0 and 1] to simulate the observation after each coin toss as follows: 
if the random number is <0.5, assume that H has occurred, tail otherwise.
Count the number of heads and compute the fraction of heads generated after each coin toss. 
This is basically to estimate the probability of head (that is 0.5).
Plot the estimated probability (using matplotlib.pyplot.plot) along the y-axis, while the trial numbers are plotted along the x-axis. 
Note that plot() also works with lists.'''

'''
import numpy as np
import matplotlib.pyplot as plt
import random
n=int(input("no of trials:"))

prob_head_list=[]
trial_no=[]

for j in range(1,n+1):
    h=[]
    
    for i in range(j):
        random_number=random.random()
        if random_number<0.5:
            h.append(random_number) 
    prob_of_heads=len(h)/j
    prob_head_list.append(prob_of_heads)
    trial_no.append(j)
#print(trial_no)
print(prob_head_list)
plt.plot(trial_no,prob_head_list)'''






