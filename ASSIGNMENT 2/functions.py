# rindex
# rsplit
# rfind
# replace 
# count 

#function for rindex 
string=input("enter the string : ")#taking input string 
substring=input("enter the substring : ")#taking input substring 



def L_occur(string,substring,start=0, stop=len(string)):#defining function 
        
        index=0#starting from 0 index inside string 
        check=""#initialising empty string.

        for i in range(0,len(string),1):#for loop for checking whole string till end 
              if(string[i]==" "):#checking if there is space then we will reinitialise check string to empty.
                    #because space will lead to new substring.
                    check=""#reinitialise check.
                    continue#skipping 
              
              else:
                    check=check+string[i]#combining characters till space through iterations 
                    if(check==substring):#checking for presence 
                          index=i#storing index value.
                    
    
        if substring not in string:#
            print("\nsubstring entered by you is not present in the string.\n")

        else:
              print("\nindex of last occurence of the substring is : ",index)


#for rfind fucntion:
def sub_find(string,substring,start=0, stop=len(string)):
      
        index=0#starting from 0 index inside string 
        check=""#initialising empty string.

        for i in range(start,stop,1):#for loop for checking whole string till end 
            if(string[i]==" "):#checking if there is space then we will reinitialise check string to empty.
                    #because space will lead to new substring.
                    check=""#reinitialise check.
                    continue#skipping 
            
            else:
                    check=check+string[i]#combining characters till space through iterations 
                    if(check==substring):#checking for presence 
                        index=i#storing index value.
                    

        if substring not in string:#
            print(-1)

        else:
            print("\nindex of last occurence of the substring is : ",index)

#for rsplit function.

def string_split(string,start=len(string),stop=0):
      
      split_list=[]
      check=""

      for i in range(start,stop,-1):
            if(string[i]==" "):
                  if(i!=0):
                    split_list.append(check)
                  check=""
                  continue
            
            else :
                  check=check+string[i]


#for count function.


def occur_count(string,substring,start=0,stop=len(string)):
      
        count=0#starting from 0 index inside string 
        check=""#initialising empty string.

        for i in range(0,len(string),1):#for loop for checking whole string till end 
              if(string[i]==" "):#checking if there is space then we will reinitialise check string to empty.
                    #because space will lead to new substring.
                    check=""#reinitialise check.
                    continue#skipping 
              
              else:
                    check=check+string[i]#combining characters till space through iterations 
                    if(check==substring):#checking for presence 
                          count+=1#storing index value.

              if(count==0):
                    print(0)      
      
#for replace function.

def string_replace(string,substring,replace,start=0,stop=len(string)):
      
      if substring in string:
        substring=replace     



      
      

      
      
    


      
      

      
      





# L_occur(string,substring)#calling function
# sub_find(string,substring)
# string_split(string,start=len(string))


              