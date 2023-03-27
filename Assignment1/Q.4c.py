# Here I have done this problem for general case i.e. for n number of inputs
n=int(input("how many names and ages you want to give?"))     
L=[]    #initializing empty list
t=[] 

for i in range(n):           #loop for taking input iteratively upto given number of times              
    name=input("Tell me your name:")                       
    age=int(input("Tell your age:"))
    t.append(name)    #adding name to list t
    t.append(age)     #adding age to list t
    L.append(tuple(t))  #adding tuple(list t has been converted to tuple which contains name,age) to list L
    t =[]                #setting list t as empty so that  the inputs of next iterations only add in that list
                                        
print(L)   #printing list of tuples, each of tuple contains name,age  

nm=input("Give me your name:") 
for i in L:          #loop for each tuple inside of the big list L
    if nm in i:       #if the name is present in that tuple it will follow the next code
        x=list(i).copy()     #Here I am creating a copy of tuple as a list so that after removing a particular element, the main tuple remain intact 
        x.remove(nm)           #Now I remove that name from list x
        print(f"The age of {nm} is {x[0]}")    # Here I am printing age to corresponding name.here The x[0] will give the age value as in the previous line after removing the name element from list the list will have just one element i.e. age