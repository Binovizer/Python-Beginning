class Dog:
    
    #tricks = []
    
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_tricks(self, trick):
        self.tricks.append(trick)
        
fido = Dog("Fido")
buddy = Dog("Buddy")
fido.add_tricks("Play Dead")
buddy.add_tricks("Roll Over")
print(fido.tricks)
print(buddy.tricks)