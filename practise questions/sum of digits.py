#Python Program to Find the Sum of Digits in a Number

n=int(input("enter a number : "))
sum_digit=0
temp=n
while n>0:
    rem=n%10
    sum_digit=sum_digit+rem
    n=n/10

print("the sum of digits of %d is %d " %(temp,sum_digit))
