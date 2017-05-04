from tkinter import * 
 
def doNothing():
    print("This started Working")
 
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
 
root.mainloop()



# from tkinter import *
# 
# def doNothing():
#     print("Ok, ok I won't!")
# 
# root = Tk()
# 
# menu = Menu(root, tearoff = False) # Creates menu object
# root.config(menu = menu) # Configuring menu object to be a menu
# 
# subMenu = Menu(menu, tearoff = False) # Creating a menu inside a menu
# 
# menu.add_cascade(label = "File",
#                  menu = subMenu) # Creates file button with dropdown, sub menu is the drop
# 
# subMenu.add_command(label = "New project",
#                     command = doNothing)
# subMenu.add_command(label = "New...",
#                     command = doNothing) # 2 commands in the sub menu now
# 
# subMenu.add_separator() # Creates seperator in the drop
# 
# subMenu.add_command(label = "Exit",
#                     command = root.destroy) # Another sub menu item
# 
# editMenu = Menu(menu, tearoff = False) # Create another item in main menu
# 
# menu.add_cascade(label = "Edit",
#                  menu = editMenu)
# 
# editMenu.add_command(label = "Redo",
#                     command = doNothing)
# 
# root.mainloop()