from tkinter import *

root = Tk()

one = Label(root, text='One', fg='black', bg="red")
two = Label(root, text='Two', fg='red', bg='yellow')
three = Label(root, text='Three', fg='red', bg='blue')

one.pack()
two.pack(fill=X)
three.pack(fill=BOTH, expand=TRUE)

root.mainloop()