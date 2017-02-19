def is_pallindrome(string1):
    if(len(string1) == 0 or len(string1) == 1):
        return True
    else :
        if(string1[0] == string1[-1] and is_pallindrome(string1[1:-1])):
            return True
        else:
            return False

string1 = input("Enter any String : ")
print(is_pallindrome(string1))
