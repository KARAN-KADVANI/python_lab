word=input("enter a word or any string : ")#for input of a word 

a=""# initialising empty string.


for i in range(len(word)):#loop for traverse through all characters 
    if i%2==0:#for even index charaters 
        a+=word[i].lower()#lower case letter 
    else:
        a+=word[i].upper()#upper case letter 

print(a)#printing the string.
    
