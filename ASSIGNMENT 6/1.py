class Password_Manager:
    

    def __init__(self,initial_password):
        self.old_passwords=["vishu123","krish123",initial_password]
    

    def get_password(self):
        return self.old_passwords[-1]
    
    

    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        
        else:
            print("this password already matches the previous passwords.")
    
    def is_correct(self,string):
        return string==self.get_password()
    
c1=Password_Manager(input("enter password you initially want : "))
print("your current password is : ")
print(c1.get_password())

c1.set_password(input("enter the new password that you want to set : "))
print(f"now your new password is set as : {c1.get_password()}")

print('''
      
    you should verfiy your new password ,
    for the that enter the new password again 
    if it returns True then it is verified and if it returns 
    False then you entered wrong password : ''')

print(c1.is_correct(input()))