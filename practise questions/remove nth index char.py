#Python Program to Remove the nth Index Character from a Non-Empty String

str_string=input("enter the string : ")
length=int(len(str_string))
index=int(input("enter the index between 0 and %d : "%(length)))


for i in range(length) :
    if i == index :
        str_string=str_string.replace(str_string[i],"",1)
        
        



print(str_string)
