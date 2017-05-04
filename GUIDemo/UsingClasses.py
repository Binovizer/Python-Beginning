from tkinter import *

class MyButtons:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(master, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(master, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
        
    def printMessage(self):
        print("Hello, My Name is Nadeem") 


root = Tk()
b = MyButtons(root)
root.mainloop()