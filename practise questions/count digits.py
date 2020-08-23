#Python Program to Count the Number of Digits in a Number

n=int(input("enter a number : "))
temp=n
count=0
while n>0 :
    n=n//10
    count=count+1
    
print(" the number of digits in %d is %d " %(temp,count))   
