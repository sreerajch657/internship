#Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.

print("the numbers between 1 &50 that are not divisble by 2 and 3 are : ")
for i in range(1,50):
    temp=i
    sum_no=0
    while i>0:
       rem=i%10
       sum_no=sum_no+rem
       #print(" sum : %d "%sum_no)
       i=i//10

    if sum_no %3 !=0 and temp%2!=0 :
        print(temp)
     
         
      

    
        
