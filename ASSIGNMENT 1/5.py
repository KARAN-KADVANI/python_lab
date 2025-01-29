students=[]
for i in range(0,10,1):
    name=input(f"enter the name of the student {i+1}: ")
    if len("students[i]")<=15 :
        students.append(name)
       
    
    else :
         print("length of student should be less than or equal to 15")
         break
 

for i in range(0,10,1):
    print(f"name of the student {i+1} is {students[i][::-1]}")
    