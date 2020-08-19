# Python Program to Merge Two Lists and Sort it
lst_1=[]
lst_2=[]
lst_3=[]

n1=int(input("enter the limit of  1st list : "))
n2=int(input("enter the limit of  2nd list : "))
for i in range(0,n1) :
    x=int(input("enter the element to 1st list : "))
    lst_1.append(x)
for j in range(0,n2) :
    y=int(input("enter the element to 2nd list : "))
    lst_2.append(y)

lst_3=lst_1+lst_2
lst_3.sort()
    
print("the merged and sorted list is : " )
print(lst_3)
