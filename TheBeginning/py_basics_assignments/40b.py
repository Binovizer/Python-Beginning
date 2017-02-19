def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter any number : "))
if (num < 0):
    print("Sorry! You have entered a negative number")
else:
    for i in range(num):
        print(fib(i))