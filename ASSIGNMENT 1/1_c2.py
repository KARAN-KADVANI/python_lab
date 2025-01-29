#Create the following lists using a for loop.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

alphabets=[]
for i in range(0,26,1) : 

    alphabets.append(chr(i+97))

    for j in range(0,i,1) :

        alphabets[i]=alphabets[i]+chr(i+97)



print(alphabets)