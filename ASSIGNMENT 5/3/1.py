t=int(input("enter the number of cases you want : "))
case=1
while case<=t:

    L=int(input("enter 1st integer :"))
    R=int(input("enter 2st integer :"))

    max=-1
    for i in range(L,R+1):
        for j in range(L,R+1):
            xor=i^j
            if(xor>=max):
                max=xor

    print("max value of xor is : ",max)

    case+=1