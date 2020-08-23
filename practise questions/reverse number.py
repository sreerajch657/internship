#Python Program to Reverse a Given Number

n=int(input("enter a number : "))
temp=n
rev=0
while n>0 :
    rem=int(n%10)
    rev=rev*10+rem
    n=int(n/10 )
    


print("the reverese of %d is %d " %(temp,rev))
