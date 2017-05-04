from tkinter import *

root = Tk()

canvas = Canvas(root, width=520, height=520)
canvas.pack()

redline = canvas.create_line(10, 10, 500, 260, fill='red')
blueline = canvas.create_line(10, 510, 500, 260, fill='blue')
greenline = canvas.create_line(10, 10, 10, 510, fill='green')

# canvas.delete(greenline)
# canvas.delete(ALL)

root.mainloop()