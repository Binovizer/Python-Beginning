from tkinter import *

root = Tk()

name = Label(root, text="Name")
password = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

name.grid(row=0, sticky=E+W+N+S)
password.grid(row=1, sticky=E+W+N+S)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()