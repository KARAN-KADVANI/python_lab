'''You are given a number N, you need to print the number of positions where digits exactly
divides N.
Input format
The first line contains T (number of test cases followed by T lines each containing N).
Constraints
1 <= T <= 15
0 <= N <= 1010
Output Format
For each test case print the number of positions in N where digits in that number exactly
divides the number N in separate line.
Input
2
12
13
Output
2
1
Explanation

Test case 1:
2 digits in the number 12 divides the number exactly.
Test case 2:
Only 1 digit in the number 13 divides the number exactly.'''

T=int(input("enter number of test cases : "))#for inputting number of test cases
if T<=15 and T>=1 :#condition for test cases

    while T!=0:#for running loop T times 


        N=int(input("enter any number : "))#N is the number that a user enters 

        count=0#insitialising count with 0 bracause initially there is no digit which can divide it completely.

        n=N#storing N in n for further use of original value of N due to some changes.

        while N!=0 :#condition for while loop
            K=N%10#accessing each digit from last
            if K!=0 and n%K==0:#condition if digit completely divides number and digit should not be 0 
                count=count+1#increment in count.
            N=N//10#integer division of N.
        T=T-1#decrement in T
        print(f"total count of digits which on division to N lead to complete division is '{count}'")#printing the output 



    
    
    