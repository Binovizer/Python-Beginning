from random import randint
x = randint(1,100)
print("Here We Go...")
n = int(input("Guess the number: "))
while(True):
    if(x == n):
        print("Yippeee! You Guessed It Right.")
        break
    elif(x > n):
        print("Too Low")
    else:
        print("Too High")
    n = int(input("Guess Again: "))