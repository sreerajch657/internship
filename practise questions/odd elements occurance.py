#Python Program to Find Element Occurring Odd Number of Times in a List

n=int(input("enter the limit of   list : "))
lst=[]
count=[]
for i in range(0,n) :
    x=int(input("enter element to list : "))
    lst.append(x)
print("elements occuring odd number of times : ")
for i in range(0,n) :
  y=lst.count(lst[i])
  if y % 2 != 0:
      print(lst[i])
      
