import sys
locls  = locals()['__builtins__'] #List of all built in exceptions
try :
    div = 1 / int(input("Enter a number : "));
    print("Division is: ",div)
except:
    print("Error ",sys.exc_info()[0])
    
