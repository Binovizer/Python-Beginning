import string
 
string1 = input("Enter any string : ")
  
def removeCapitals(str1):
    for char in string1 : 
        for c in string.ascii_lowercase :
            if (char == c) : 
                print(char, end="")
  
removeCapitals(string1)

str2 = input("\nEnter any string to check pallindrome : ")
 
def isPallindrome(str2):
    if list(str2) == list(reversed(str2)) :
        print("A Pallindrome")    
    else :
        print("Not a Pallindrome")
         
isPallindrome(str2)

str3 =input("Enter any string : ")
 
def countVowels(str3):
    count = 0
    for char in str3.casefold() : 
        if char in ("aeiou"):
            count += 1;
    return count
 
print(countVowels(str3))

str4 = input("Enter any string with punctuation : ")

def removePunctuation(str4):
    for char in str4 :
        if char not in "!()-[]{}::,/\<>'.?@#$%^&*_~"+'"' :
            print(char,end="")
            
removePunctuation(str4)

