#Python Program to Put Even and Odd elements in a List into Two Different Lists

even_elements=[]
odd_elements=[]

n=int(input("enter the limit of array : "))
for i in range(0,n) :
    x=int(input("enter the element to list : "))
    
    if x % 2 == 0 :
        even_elements.append(x)
        
    else :
        odd_elements.append(x)
        
        
print("the even elements are : ")
print(even_elements)
print("the odd elements are : ")
print(odd_elements)
