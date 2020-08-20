# number of positive,negative ,odd and even numbers

lst=[]
neg_lst=[]
pos_lst=[]
even_lst=[]
odd_lst=[]
lower=int(input(" enter the lower limit : "))
upper=int(input("enter the upper limit : "))

for i in range(lower,upper):
    if  i > 0:
        pos_lst.append(i)
        if i%2==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    else:
        neg_lst.append(i)
        if i%2==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

print("the positive list : ")
print(pos_lst)
print("the negative list : ")
print(neg_lst)
print("the even list : ")
print(even_lst)
print("the odd list : ")
print(odd_lst)
