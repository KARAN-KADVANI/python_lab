'''
3. Pangrams

Roy wanted to increase his typing speed for programming contests so, his friend advised him to
type the sentence “The quick brown for jumps over the lazy dog” repeatedly because it is a
pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)
After typing the sentence several times, Roy became bored with is. So he started to look for other
pangrams.
Given a sentence s, tell Roy if it is a pangram or not.

Input Format:
Input consists of a line containing s.
Output Format:
Output a line containing pangram if s is a pangram, otherwise output not pangram
Sample Input #00
we promptly judged antique ivory buckles for the next prize
Sample Output #00
pangram
Sample Input #01
we promptly judged antique ivory buckles for the prize
Sample Output #01
not pangram
Explanation
In the first test case the answer is pangram because the sentence contains all the letters.

'''
s=input("enter the sentence that you want to check : ")
flag=0
for i in range(97,123,1):
    for j in range(0,len(s),1):
        if(s[j]==" "):
            j=j-1
            continue
        elif(ord(s[j])==i):
            flag=1

            break
        else:
             flag=0

    
    if(flag==0):
        print("it is not a pangram")
        break
if(flag==1):
        print("it is a pangram")   