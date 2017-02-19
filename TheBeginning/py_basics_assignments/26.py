string1 = input("Enter any string : ")

string1 = string1.lower();

print(string1)

chars = "abcdefghijklmnopqrstuvwxyz";
for char in chars :
    count = string1.count(char)
    if (count >= 1):
        print(char,count)
        
# count = {}
# for s in string1:
#     if count.has_key(s):
#         count[s] += 1
#     else:
#         count[s] = 1
# 
# for key in count:
#     if count[key] > 1:
#         print(key, count[key])