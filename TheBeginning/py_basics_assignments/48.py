q_size = 3
q = []
rear = -1
front = 0

def is_full():
    if(len(q) == q_size):
        return True
    else:
        return False

def is_empty():
    if(len(q) == 0):
        return True
    else:
        return False

def enquue(element):
    if(is_full()):
        print("Queue is Full.",element)
    else:
        global rear
        rear = rear + 1
        q.append(element)
        print("Inserted : ",element)
        
def dequeue():
    if(is_empty()):
        print("Queue is Empty.")
    else:
        q.remove(q[0])
        global front
        front = front + 1

def display_elements():
    print("Queue is : ",q)

enquue(10)
enquue(20)
enquue(30)
enquue(40)
display_elements()
dequeue()
display_elements()
