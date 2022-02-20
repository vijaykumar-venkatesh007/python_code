def isNumber(s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
 
    return True
    
str = input()
 
   
if isNumber(str):
        print("yes")
else:
        print("no")