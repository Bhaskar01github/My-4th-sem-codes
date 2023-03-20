#3.Take your full name as input and make an abbreviation of your name based on the initials of the names.

'''name=input("Enter your name:").split()
print(name)
s1=''
for i in name:
  s1+=i[0]
  
print("Your abbreviation is",s1) '''


#Write a program that prints the first 10 elements of a Fibonacci series 1, 1, 2, 3,5, 8, 13,....., where each element is the sum of the two previous elements (the first two numbers are defined to be 1).

'''
l=[1,1]
for i in range(8):
  y=int(l[i])+int(l[i+1])
  l.append(y)
print(l)  '''
#5

'''rows=input("How many rows you want to print?:"  )

for i in range(1,int(rows)+1):
   l=[]
   for j in range(1,i+1):   
       l.append(j)
  
   k=' '.join(str(elm) for elm in l )
   print(k)'''

#6
'''rows=input("How many rows you want to print?:"  )

for i in range(1,int(rows)+5,2):
   l=[]
   for j in range(1,i+2,2):   
       l.append(j)         #another way is just append odd no. terms i.e. l.append(2*j-1)
  
   k=' '.join(str(elm) for elm in l )
   print(k)'''
#7
'''rows=input("How many rows you want to print?:"  )

for i in range(1,int(rows)+1):
   l=[]
   for j in range(1,int(rows)+1-(i-1)):   
       l.append(j)
  
   k=' '.join(str(elm) for elm in l )
   print(k)'''
#8
rows=input("How many rows you want to print?:"  )

for i in range(1,int(rows)+1):
   for j in range(1,i):
       print(end=' ')
   for j in range(i,int(rows)+1):   
       print(j,end='')
   for j in range(
   print(end='\n')
  
 






