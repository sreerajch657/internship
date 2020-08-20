#Write a program to find the sum and product of all elements of a list.

n=int(input("enter the limit of the list : "))
lst=[]
product=1
for i in range(0,n):
    x=int(input("enter the elements to list : "))
    lst.append(x)
    product=product*x

sum_lst=sum(lst)


print("the sum of list : %d " %sum_lst)
print("the product of list : %d " %product)
