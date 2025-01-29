length=float(input("enter a length in feet : " ))

measurements=[length*12,length/3,length/5280,length*304.8,length*30.48,length*0.3048,length/3280]

option=0

while 1: 
    print("""enter 1 for conversion of length from feet into inches
          "enter 2 for conversion of length from feet into yards"
          "enter 3 for conversion of length from feet into miles"
          "enter 4 for conversion of length from feet into millimeters"
          "enter 5 for conversion of length from feet into centimeters"
          "enter 6 for conversion of length from feet into meters"
          "enter 7 for conversion of length from feet into kilometers"
          "enter 9 to exit" """)
    
    option=int(input("enter the option number for conversion : "))


    if option==9:
        print("exiting the loop")
        break
    if option>=1 and option<=8:
        print(f"conversion of feet is : ",measurements[option-1])

    else:
        print("invalid input.")




