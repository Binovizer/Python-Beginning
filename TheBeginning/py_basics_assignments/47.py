list_size = 3
s = []

def is_empty():
    if(len(s) == 0):
        return True
    else:
        return False
    
def is_full():
    if(len(s) == list_size):
        return True
    else:
        return False
    
def push(element):
    if(is_full()):
        print("Sorry! Stack is already full.Can't Push",element)
    else:
        s.append(element)

def pop():
    print("Popping : ",end="")
    if(is_empty()):
        print("Sorry! Stack is already empty.Can't Pop")
    else:
        item =  s.pop()
        return item
    
def display_elements():
    if(is_empty()):
        print("Stack is empty")
    else:
        print("Elements are : ",s)
        
push(30)
push(45)
push(15)
display_elements()
push(35)
print(pop())
print(pop())
display_elements()