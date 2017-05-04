from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', "You should work much harder")
answer = tkinter.messagebox.askquestion('Question 1', "Are you a silly person?")

if(answer == 'no'):
    print("Of Course you are!")
else:
    print("You surely are!")

root.mainloop()