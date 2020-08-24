#Python Program to Print all Numbers in a Range Divisible by a Given Number

lower=int(input("enter the lower limit : "))
upper=int(input("enter the upper limit : "))

n=int(input("enter the number that need to be divided : "))

print("the numbers divisible by %d with the range %d and %d is : "%(n,lower,upper))

for i in range(lower,upper):
    if i%n==0 :
        print(i)
