def rev(string1):
    if(len(string1) == 0 or len(string1) == 1):
        return string1
    else:
        return rev(string1[1:]) + string1[0]
 
string1 = input("Enter any string : ")
print(rev(string1))