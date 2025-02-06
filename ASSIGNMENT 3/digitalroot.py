
def digital_root(n):
    sum=0
    fsum=0
    while(n!=0):
        
        q=n%10
        sum+=q
        n=n//10

        
    if(sum>9):
        return digital_root(sum)
    else:

        return sum
num=int(input("enter the number whose digital root you want to find : "))
print(digital_root(num))
                
            
        
