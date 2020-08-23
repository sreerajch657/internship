
#Python Program to Read a Number n and Compute n+nn+nnn

n=int(input(" enter a number "))

sum_no=0

i=1
while i<=3 :
    sum_no=sum_no+n**i
    i=i+1


print("the sum =%d " %sum_no)
