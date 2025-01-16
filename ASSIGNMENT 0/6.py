#write a program to to reverse the number given by the user 

number=int(input("enter the number that you want it reverse : "))
sum=0
while number>0:
    remainder=number%10
    sum=sum+remainder
    sum=sum*10
    number=number//10

sum=sum//10

print("the reverse of the number you have given is : ",sum)