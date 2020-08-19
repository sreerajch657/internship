#Python Program to Calculate the Number of Words and the Number of Characters Present in a String

str_string=input("enter a string : ")

length=int(len(str_string))
word_count=0;
char_count=0;

for i in range(length) :
        if str_string[i]== " " :
            word_count=word_count+1
        else :
            char_count=char_count+1
        
   
print('the word count in "%s" is : %d' %(str_string,word_count+1) )

print('the character count in "%s" is : %d' %(str_string,char_count) )
