import string
string1 = input("Enter string 1 : ")
string2 = input("Enter string 2 : ")

for char in string1:
    if (char in string.ascii_uppercase):
        print(char,end="")
    
for char in string2:
    if (char in string.ascii_uppercase):
        print(char,end="")
    
