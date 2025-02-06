def utopianTree(N):#defining function with N=number of years.
    #2 cycles every year 
    #monsoon -- 2*height , summer -- height+1
    height=1#initial height of that sapling is 1 meter.

    for i in range(1,N+1,):#loop starting from 1 upto N
        height_M=2*height#height in monsoon=2*height 
        height_S=height_M+1#height in summer = height in monsoon +1
        height=height_S#for next year height =height in summer 
        
    return height#return final height of sapling after N YEARS . 
t=int(input("enter the number of test cases : "))#for number of test cases 
for i in range(t):#looping 
    num=int(input("enter the number of years after which you want to see the height-->"))#input of number of years i.e.N
    print(utopianTree(num))#printing final height of tree .
    