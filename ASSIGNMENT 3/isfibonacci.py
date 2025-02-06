def fibonacci(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
t=int(input("enter the number of test cases : "))

for i in range(t):
    n=int(input("enter the number that you want to check : "))
    flag=0
    for i in range(0,10**10):

        if(n==fibonacci(i)):
            print("IsFibo")
            flag=1
            break

        elif(n<fibonacci(i)):
            break
    

    if(flag==0):
        print("IsNotFibo")    

    
    




