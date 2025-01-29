import random

random_number=[random.randint(0,1) for _ in range(100)]

print(random_number)

#now we have to find longest run of zero

maxcount=0
count=0



for i in range(0,100,1):
    if random_number[i]==0:
        count=count+1

    else:
        if count > maxcount:
            maxcount = count
        count = 0

if count > maxcount:
    maxcount = count
    
    



        
    
print(maxcount)
