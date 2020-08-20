# Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.

lst=[]
n=int(input("enter the limit of list : "))

for i in range(0,n) :
    x=int(input("enter the elements into list : "))
    lst.append(x)

item=int(input("enter the element to be searched : "))
index=0
count=0
for i in range(0,n):
    if lst[i]==item:
        index=i
        count=count+1

if count==0 :
    print("the element %d is not found in the list  " %item)
else:
    print("the element %d is found at %d position in list  " %(item,index+1))
