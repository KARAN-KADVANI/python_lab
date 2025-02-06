'''Q2.IsFibo
   
You are given a integer, N. Write a program to determine if N is an element of the Fibonacci
Sequence.
The first few elements of Fibonacci sequence are 0,1,1,2,3,5,8,13...... A Fibonacci sequence is one
where every element is a sum of the previous two elements in the sequence. The first two elements
are 0 and 1.
Formally:
Fib0 = 0
Fib1 = 1
Fibn = Fibn-1 + Fibn-2 for all n > 1
Input Format:
The first lines contains T, number of test cases.
T lines follows. Each line contains an integer N.
Output Format:
Display IsFibo if N is a fibonacci number and IsNotFibo if it is not a fibonacci number. The output
for each test case should be displayed on a new line.
Constraints:
1 <= T <= 105
1 <= N <= 1010
Sample Input:
3
5
7

8
Sample Output
IsFibo
IsNotFibo
IsFibo
5 is a fibonacci number given by Fib5 = 3 + 2
7 is not a fibonacci number
8 is a fibonacci number given by Fib6 = 5 + 3'''

def fibonacci(n):#defining function.
    if n==1:#condition
        return 1
    if n==0:#conditon 2
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)#recursive approach 
    
t=int(input("enter the number of test cases : "))#input of number of test cases.

for i in range(t):#loop for input 
    n=int(input("enter the number that you want to check : "))#input of the number that you want to check 
    flag=0#taking an extra variable flag so that to mark whether condition inside the loop was satisfied or not 
    for i in range(0,10**10):#loop for checking 

        if(n==fibonacci(i)):#matching each fibonacci number with n
            print("IsFibo")
            flag=1
            break

        elif(n<fibonacci(i)):
            break#if function exceeds the value than the entered number than  break it because after that it will not satisfied.
    

    if(flag==0):#if it is not the part of fibonacci series than print isnotfibo
        print("IsNotFibo")    

    
    




