#Python Program to Check if a Number is a Palindrome

n=int(input("enter a number : "))
temp=n
rev=0
while n>0 :
    rem=n%10
    rev=rev*10+rem
    n=n//10


if temp==rev :
    print(" the number is palindrome ")
else:
    print("the number is not palindrome ")
