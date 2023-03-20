'''Q.1)
L=[1,3,5,7]
M=[2,4,6]
for i in range(len(M)):
   L.insert(2*i+1,M[i])
   print(L)   '''
   
'''Q.3)[Q3 – Q6 are on Stack] Stack is a data structure where you can add or delete elements at one end only. That is why it is called Last In First Out (LIFO) data structure. That is, the element that is inserted last is deleted first. Let us try to construct a stack using a list L. Write a function Push(L, e) that adds an element to the list L so that L follows the LIFO property. Use this Push() function to add the elements 1, 2, 3, 4, 5 (in this order) to a list L and display the list.'''

def Push(l,e):
   l.append(e)
'''L=[]
lt=[]  
for i in range(len(L)):
   Push(lt,L[i])
print(lt) '''
      
'''Q.4)  Write a Pop(L) function that removes the last element in a List L and returns the deleted element. Apply this Pop() function on list L to remove the last element.'''

def Pop(L):
   return L.pop()
      
'''print(Pop(L))
print(L)  '''
'''Q.5)
Use Push() in Q3 to add five names to a list Name and using Pop() in Q4 display the names in the reverse order.'''

'''Q.5)
L=['a','b','c','d','e']
lt=[]

for i in range(len(L)):
    Push(lt,L[i])
print(lt)
revlst=[]
for j in range(len(lt)):
    revlst.append(Pop(lt))
print(revlst)'''


'''Q.6)
strg=input("enter:")
M=list(strg)
revl=[]
for i in range(len(M)):
     revl.append(Pop(M))
srevl=''.join(revl)
if srevl==strg:
     print('palindrome')
else:
     print('not')   ''' 
     
'''Q.7)
L=[1,2,2,3,4,5,5,6,2,7,1,8,8]
print(list(set(L)))
'''
''' Q.8  
Lst=[1,2,3,4,5]
evL=[i for i in Lst if i%2==0]
print(evL)'''





















    
   














   
   
   

   
   
