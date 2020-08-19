#Python Program to Swap the First and Last Value of a List

lst_1=[]

temp=0
n=int(input("enter the limit of   list : "))

for i in range(0,n) :
    x=int(input("enter the element to 1st list : "))
    lst_1.append(x)

print("the list before swapping fist and last element in list :")
print(lst_1)

print("the list after swapping fist and last element in list :")
temp=lst_1[0]
lst_1[0]=lst_1[-1]
lst_1[-1]=temp
print(lst_1)
