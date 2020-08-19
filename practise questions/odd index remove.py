#Python Program to Remove the Characters of Odd Index Values in a String

str_string=input("enter a string : ")
str_string2=""
length=int(len(str_string))

for i in range(length) :
        if i % 2 == 0 :
            str_string2=str_string2+str_string[i]
        
   
print(str_string2)
