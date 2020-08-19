#Python Program to Find the Largest Number in a List
y=[]
n=int(input("enter the limit of array : "))
for i in range(0,n) :
    x=int(input("enter the element to list : "))
    y.append(x)

y.sort()
    
print("the largest number among list is : %d "%(y[-1]))
