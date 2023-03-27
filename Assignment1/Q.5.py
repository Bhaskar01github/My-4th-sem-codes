a=int(input("Give the integer:"))
L=[]             #initializing empty list                                          

for i in range(int(a**(1/3)+1)):                   #Here we take the range upto the number int(a^(1/3)) as after that number, cube of any number will be greater than the given input a 
    l=[]
    for j in range(int(a**(1/3))+1):
        if i**3+j**3==int(a) and i<j :            #Here we give i<j to maintain a order so that duplication of numbers do not occur[like for 1729,(1,12) and (12,1) both do not get appended to empty list ] 
            l.append(i)
            l.append(j)
            tl=tuple(l)                #tuple will contain two numbers
            L.append(tl)                #adding tuples to list L
            
if len(L)==2:                   #this condition will allow us to print the list which contains only two tuples and this tuples will contain two numbers which satisfy the given condition for hardy ramanujan number  
    print(L,f",So {a} is a hardy ramanujan number.")
else:
    print(f"{a} is not a hardy ramanujan number")
