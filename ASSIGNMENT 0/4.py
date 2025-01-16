#write a program to swap to variables without using third variable.

var_1=int(input("enter the first number :- "))
var_2=int(input("enter the second number :- "))

print("before swapping the value of first variable is ",var_1," and value of second variable is ",var_2)

var_1=var_1+var_2
var_2=var_1-var_2
var_1=var_1-var_2


print("after swapping the value of first variable is ",var_1," and value of second variable is ",var_2)



