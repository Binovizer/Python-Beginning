import random
x = int(input("Enter the no of sides you want in your dice: "))
f = True
while(f):
    marks = random.randint(1,x)
    print(marks)
    choice = input("Wanna Role Again? 'Y' or 'N'")
    if(choice == 'N' or choice == 'n'):
        f = False