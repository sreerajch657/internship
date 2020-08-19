#Python Program to Find the Second Largest Number in a List Using Bubble Sort

lst=[]

n=int(input("enter the limit of list : "))

for i in range(0,n):
    x=int(input("enter the elements into list : "))
    lst.append(x)
temp=0
for i in range(0,n-1) :
    for j in range (0,n-i-1):
        if lst[j] > lst[j+1] :
            temp=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=temp
print(lst)   
print("the second largest element is : %d " %(lst[-2]))        
