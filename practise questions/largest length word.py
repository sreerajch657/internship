#Python Program to Read a List of Words and Return the Length of the Longest One

str_string=input("enter a string : ")

length=[]
str_string=str_string.split()
length_string=int(len(str_string))
for i in range(0,length_string) :
    item=str_string[i]
    x=int(len(item))
    length.append(x)   

length.sort()

print("the higesht word length is : %d " %length[-1])
   
