#Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists.
n=int(input("enter the limit of the list : "))
lst=[]

for i in range(0,n):
    x=int(input("enter the elements to list : "))
    lst.append(x)

middle=int(n/2)
print("the array after spliting : ")
print(lst[ :middle])
print(lst[middle : n+1])
