#find factorial of the number given by user.

num=int(input("enter the number whose factorial you want to find : "))
i=1
factorial=1
while num>=i:

    factorial=factorial*i
    i=i+1

print("the factorial of a given number is : ",factorial)


