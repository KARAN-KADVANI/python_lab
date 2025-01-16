#write a program to print table of any number

number=int(input("enter a number whose table you want : "))

i=1


while i<=10 :
    table=number*i
    print(number," * ",i,"=",table)
    i=i+1