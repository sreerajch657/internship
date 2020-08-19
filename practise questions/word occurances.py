#Python Program to Count the Occurrences of Each Word in a Given String Sentence

str_string=input("enter a string : ")

length=int(len(str_string))

for i in range(length) :
        if str_string[i].isalpha():
            item=str_string[i]
            count=int(str_string.count(item))
            print("the occurance of %s in the string is : % d " %(item,count))
        else:
            i=i+1
        
   
