string1 = input("Enter any string : ")

i = 0
str1_list = ""
while (i < len(string1) ):
    if (i % 2 == 0):
        str1_list += string1[i]
    i += 1
        
print("".join(reversed(str1_list)))