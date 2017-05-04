from tkinter import * 
 
def doNothing():
    print("This started Working")

#******** Main Menu *******

root = Tk()
 
menu = Menu(root, tearoff = False)
root.config(menu = menu)
 
submenu = Menu(menu, tearoff = False)
menu.add_cascade(label='File', menu = submenu)
submenu.add_command(label='New Project', command = doNothing)
submenu.add_command(label='New...', command=doNothing)
submenu.add_separator()
submenu.add_command(label='Quit', command=root.destroy)
 
editMenu = Menu(menu, tearoff = False)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)
 

#******** Tool Bar *******

toolbar = Frame(root, bg='blue')

insertButt = Button(toolbar, text='Insert Image', command=doNothing)
insertButt.pack(side=LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text='Print Message', command=doNothing)
printButt.pack(side=LEFT, padx = 2, pady = 2)

toolbar.pack(side=TOP, fill=X)


#******** Status Bar *******

status = Label(text='Preparing to do nothing', bd=1, relief=SUNKEN, anchor='w')
status.pack(side=BOTTOM, fill=X)












root.mainloop()
