#Python Program to Calculate the Average of Numbers in a Given List

lst=[]

n=int(input(" enter the limit of the list : "))

for i in range(0,n):
    x=int(input("enter the element into the list : "))
    lst.append(x)


avg=int(sum(lst)/n )

print(" the average of the list is : %d " %avg)
