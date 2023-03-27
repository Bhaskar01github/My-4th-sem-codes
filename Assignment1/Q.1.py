import math                 
def g(x):         #defining function g(x)
    return math.log(x)+0.5

x0=0.1
x1=1

while True:
    r=x1-(g(x1)*((x1-x0)/(g(x1)-g(x0))))
    x0=x1            #setting initial value of x co-ordinate to next value where the tangent drawn intersect x axis
    x1=r
    if abs(g(r))<0.0001:     #if the accuracy is less than 0.0001 the loop breaks
        break
    
print("The root of the equation",round(r,4),"with accuracy of 10^-4.")


