list_size = 5
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
        print("Sorry! Stack is already full")
    else:
        s.append(element)

def pop():
    if(is_empty()):
        print("Sorry! Stack is already empty")
    else:
        item =  s.pop()
        return item
    
def display_elements():
    if(is_empty()):
        print("Stack is empty")
    else:
        print("Elements are : ",s)
        
push(10)
push(20)
display_elements()
print(pop())
display_elements()
push(30)
push(40)
display_elements()
print(pop())
display_elements()
push(50)
push(60)
display_elements()