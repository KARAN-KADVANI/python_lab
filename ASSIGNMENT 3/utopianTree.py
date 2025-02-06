def utopianTree(N):
    #2 cycles every year 
    #monsoon -- 2*height , summer -- height+1
    height=1

    for i in range(1,N+1,):
        height_M=2*height
        height_S=height_M+1
        height=height_S
        
    return height
t=int(input("enter the number of test cases : "))
for i in range(t):
    num=int(input("enter the number of years after which you want to see the height-->"))
    print(utopianTree(num))
    