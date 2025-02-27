K=int(input("enter the number of times he wants to cut cake : "))

if(K%2==0):
    quantity=(((K+2)/2)-1)**2

else:
    quantity=(((K+2)/2)-1)**2 -(K+1)

print(quantity)