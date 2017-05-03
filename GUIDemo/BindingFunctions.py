from tkinter import *

def printMyName(event):
    print("Hello My Name is Khan")

root = Tk()

#button1 = Button(root, text="Print My Name", command=printMyName)

button1 = Button(root, text="Print My Name")
button1.bind('<Button-1>', printMyName)
button1.pack()

root.mainloop()