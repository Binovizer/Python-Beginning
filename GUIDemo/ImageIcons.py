from tkinter import *

root = Tk()

photo = PhotoImage(file='abc.png')
label = Label(root, image = photo)
label.pack()

root.mainloop()