products={}#initialising empty dictionary.

while True : #loop will always run until break statement is excuted.

    key=input("enter the product name (or exit if you want to end ): \n")#key variable for input of products.

    if key.lower()=="exit":#condition if exit string exist then the loop will break.
        break#for breaking of loop.

    value=float(input("enter the amount of product : "))#for storing price of a product as its value .

    products[key]=value#storing it in dictionary as a key value pair .


while True:#loop
#here , we have to give some message if customer enters a product which is not present in the list 
#so , we added an exception handler which is try : and excpet : keyword due to which program will not break 
#in middle and conitnue till exit by just giving a message on entering wrong products .
    try :

        key = input("enter the product name to get its corresponding value (or exit if you want to end ): ")

        if key.lower()=="exit":
            break

        print(f"price of {key} is : ",products[key])#print price of product entered.
    except: 

        print("product entered by you is not valid or unavailable currently.")
        





    
