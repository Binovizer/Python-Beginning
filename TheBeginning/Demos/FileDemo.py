fileObj = open("abc.txt", "w")

fileObj.write("Hello this is just a demo\nThis should be in new line");
print(fileObj.closed)
print(fileObj.mode)

fileObj.close();

fileObj1 = open("abc.txt", "r+");

sentence = fileObj1.read();

print(sentence)