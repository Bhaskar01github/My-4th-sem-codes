no_of_pairs=int(input("how many pairs you want to give?"))
L=[]
while len(L)<no_of_pairs:             #it takes input repeatedly till no of given iterations
    pair=input("Give me the pair:").split(',')        #it splits two numbers of input in coma(,) and make a list out of that elements
    L.append(pair)               #it makes list of lists
print(L)
j=[]
for i in L:                #loop for each list inside of the big list L
    j+=i                #concatinating lists inside L
lst=list(set(j))        #removing duplicates by making it a set from list then again make it list.this finally gives us list of unique elements
lst.sort()            #'sort' function arranges elements in accesnding order
print(lst)           #printing a list(lst) of unique numbers which are in accesnding order from list of lists L,these are the key values of dictionary i.e. nodes of graph
V=[]           #initializing a empty list
d={}        #initializing a empty dictionary
for e in lst:         #loop for each element in lst                                   
    v=[]
    for k in L:       #loop for each list inside of the big list L
        if e in k:               #the motive behind this condition is that if a node is present in any list it will remove the node and append the other value to a empty list.This doing for all nodes will give us different nodes connected with a node  
            k_copy=k.copy()             #Here I am creating a copy of list so that after removing a particular element, the main list remain intact 
            k_copy.remove(e)           #removing the node for which the outermost loop is running
            v.append(int(k_copy[0]))        #appending the other element into empty list v
            
    d[int(e)]=v         #entering key values for each key e in empty diictionary d
print(d)                      #Here we are printing the dictionary of lists that will show us the nodes(represented as key) and its adjacency nodes(key values)
            

















