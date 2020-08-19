# Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
str_string=input("enter a string : ")
str_string2=""
length=int(len(str_string))

item=str_string[0]
str_string2=str_string2+item
item=str_string[1]
str_string2=str_string2+item

index=0
i=-1
while index!=2 :
    if str_string[i].isalpha():
        item=str_string[i]
        str_string2=str_string2+item
        index=index+1
        i=i-1
    else:
        i=i-1 

print("the string with first 2 and last 2 characters is : %s" %(str_string2))

