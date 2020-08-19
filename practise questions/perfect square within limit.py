# Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10




n1=int(input("enter the lower limit of   list : "))
n2=int(input("enter the upper limit of   list : "))
print("the perfect square within limit %d and %d : " %(n1,n2))
for i in range(n1,n2+1) :
    if i**0.5 == int( i**0.5) :
        print(i)
sum=0   
for i in range(n1,n2+1) :
    if i<=10:
        sum=sum+i
print("the of numbers less than 10 is : %d" %sum)
