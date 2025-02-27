alphabets="abcdefghijklmnopqrstuvwxyz"
strings=input("enter the string : ")
flag=1
for char in alphabets:
    if char not in strings:
        flag=0

if(flag==1):
    print("pangram")

else:
    print("not pangram")