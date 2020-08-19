#Python Program to Calculate the Number of Digits and Letters in a String

str_string=input("enter a string : ")

length=int(len(str_string))
letter_count=0
digit_count=0

for i in range(length) :
        if str_string[i].isalpha():
            letter_count=letter_count+1
        elif str_string[i].isalnum():
            digit_count=digit_count+1
        else:
            i=i+1
            
        
   
print("the number of letters in %s is : %d" %(str_string,letter_count))
print("the number of digits in %s is : %d" %(str_string,digit_count))
