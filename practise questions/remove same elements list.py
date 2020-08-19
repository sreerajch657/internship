#Python Program to Remove the Duplicate Items from a List

lst_1=[]

n=int(input("enter the limit of   list : "))

for i in range(0,n) :
    x=int(input("enter the element to  list : "))
    lst_1.append(x)


print("the list after removing duplicate items : ")
print(list(set(lst_1)))
        
    

