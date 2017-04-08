class myClass:
    def __init__(self):
        myClass.x = 10
        self.x = 30
obj = myClass();
print(obj.x)
myClass.x += 1
print(myClass.x)