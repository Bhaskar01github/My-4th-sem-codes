# Here I have done this problem for general case i.e. for n number of inputs and if we put n=10 it will follow our question's instruction

n=int(input("how many names and ages you want to give?"))     
L=[]    #initializing empty list
t=[] 

for i in range(n):                  #loop for taking input iteratively upto given number of times              
    name=input("Tell me your name:")                       
    age=input("Tell your age:")
    t.append(name) #adding name to list t
    t.append(age)  #adding age to list t
    L.append(tuple(t))  #adding tuple(list t has been converted to tuple which contains name,age) to list L
    t =[]                #setting list t as empty so that  the inputs of next iterations only add in that list
                                        
print(L)   #printing list of tuples, each of tuple contains name,age  

