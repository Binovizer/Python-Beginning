import tkinter as tk
import string
from tkinter import messagebox
from tkinter.constants import GROOVE, SUNKEN, TOP, BOTTOM
import random

class App(tk.Frame):
    
    words = ['dracula','dragon','different', 'whale', 'Fjord', 'Gazebo'
         ,'flower','new','Awkward','Bagpipes','Banjo','Bungler'
         ,'Croquet','Crypt','Dwarves','Fervid','Fishhook', 'Gypsy'
         ,'Haiku','Haphazard','Hyphen','Ivory','Jazzy', 'Jiffy'
         ,'Jinx','Jukebox','Kayak','Kiosk', 'Klutz','Memento'
         ,'Mystify', 'Numbskull','Ostracize', 'Oxygen','Pajama'
         ,'Phelgm', 'Pixel', 'Quad', 'Quip', 'Rogue', 'Toady']
    
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)

        self.pack()
        self.master.title("Hangman : By Nadeem")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        self.master.protocol('WM_DELETE_WINDOW', self.do_quit)
        self.master.bind('<Escape>', self.do_quit)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 4
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 12
        self.master.geometry("+{}+{}".format(int(x), int(y)))

        self.master.config(menu=tk.Menu(self.master))
        
        self.dialog_frame = tk.Frame(self)
        self.dialog_frame.pack(padx=20, pady=15)

        tk.Label(self.dialog_frame, text="Welcome to Hangman", bd=0).pack()

        self.word = (App.words[random.randint(0,len(App.words)-1)]).lower()
        self.word_list = list(self.word)
        self.coded_word_list = list('-' * len(self.word))

        self.incorrect_count = 0
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(padx=15, pady=(0, 15), anchor='e')
        
        self.buttons = {}
        
        for e in list(string.ascii_lowercase):
            button = tk.Button(self.button_frame,
                               text=e,
                               command=lambda letter=e: self.analyse_guess(letter),
                               padx=5, 
                               pady=5, 
                               relief = GROOVE,
                               disabledforeground='red')
            button.config(font=('helvetica', 12, 'bold italic'))
            button.pack(side='left')
            self.buttons[e]  = button
            
        self.guessword_frame = tk.Frame(self)
        self.guessword_frame.pack(side=TOP, pady=(20,20))
        
        self.guessword = tk.Label(self.guessword_frame, text= ''.join(self.coded_word_list), bg='#c6c6c6', font=("Courier", 44))
        self.guessword.pack()    
        
        self.bona_canvas_frame = tk.Frame(self, relief=SUNKEN)
        self.bona_canvas_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.bona_canvas = tk.Canvas(self.bona_canvas_frame, width=300, height=250, bg='#c6c6c6')
        
        self.bona_canvas.create_line(50, 230, 120, 230, width=3)
        self.bona_canvas.create_line(85, 230, 85, 40, width=3)
        self.bona_canvas.create_line(85, 40, 200, 40, width=3)
        self.bona_canvas.create_line(85, 75, 130, 40, width=3)
        self.bona_canvas.create_line(200, 39, 200, 50, width=3)
        
        self.bona_head = self.bona_canvas.create_oval(200-25, 75-25, 200+25, 75+25, width=3, outline = '#c6c6c6')
        
        self.bona_body = self.bona_canvas.create_line(200, 100+3, 200, 150+3, width=3, fill='#c6c6c6')
        
        self.bona_left_foot = self.bona_canvas.create_line(200, 150+3, 160, 190+3,  width=3, fill='#c6c6c6')
        self.bona_right_foot = self.bona_canvas.create_line(200, 150+3, 240, 190+3, width=3, fill='#c6c6c6')
        
        self.bona_left_arm = self.bona_canvas.create_line(200-3, 115, 160, 150+3,  width=3, fill='#c6c6c6')
        self.bona_right_arm = self.bona_canvas.create_line(200+3,115, 240, 150+3, width=3, fill='#c6c6c6')
        
        
        self.bona_canvas.pack(side='left', padx = 20, pady=(20,0))
        
        self.tracker_frame = tk.Frame(self)
        self.tracker_frame.place(in_ = self.bona_canvas_frame, anchor="w", relx=.6, rely=.5)
        
        self.tracker_word = tk.Label(self.tracker_frame, text = '', font=("Courier", 12))
        self.tracker_word.pack()
        
        self.result_frame = tk.Frame(self)
        self.result_frame.pack(side='top',pady=20)
        
        self.result = None
        self.correctAnswer = None

    def do_quit(self):
        if(messagebox.askyesno('Quit', 'Are you sure you want to quit the game ?')):
            self.master.destroy()

    def analyse_guess(self, letter):
        self.buttons.get(letter).config(state="disabled") # Disabling the Current Button
        flag = False
        win = 2
        if(letter in self.word_list):
            flag = True
            while(letter in self.word_list):
                index = self.word_list.index(letter)
                self.coded_word_list[index] = letter
                self.word_list[index] = '0'
            if('-' not in self.coded_word_list):
                win = 1
            
            self.updateGuessword()
        else:
            self.incorrect_count += 1
            if(self.incorrect_count == 1):
                self.bona_canvas.itemconfig(self.bona_head, outline='black')
            if(self.incorrect_count == 2):
                self.bona_canvas.itemconfig(self.bona_body, fill='black')
            elif(self.incorrect_count == 3):
                self.bona_canvas.itemconfig(self.bona_left_arm, fill='black')
            elif(self.incorrect_count == 4):
                self.bona_canvas.itemconfig(self.bona_right_arm, fill='black')
            elif(self.incorrect_count == 5):
                self.bona_canvas.itemconfig(self.bona_left_foot, fill='black')
            elif(self.incorrect_count == 6):
                win = 0
                self.bona_canvas.itemconfig(self.bona_right_foot, fill='black')
                
        self.showTrackerWord(flag)
        self.showResult(win)

    def updateGuessword(self):
        self.guessword.destroy()
        self.guessword = tk.Label(self.guessword_frame, text= ''.join(self.coded_word_list), bg='#c6c6c6', font=("Courier", 44))
        self.guessword.pack()
    
    def showTrackerWord(self, flag):
        if(flag):
            word = "You're doing great"
        else:
            word = 'Wrong Guess. Keep Trying'
        
        self.tracker_word.destroy()
        self.tracker_word = tk.Label(self.tracker_frame, text = word, font=("Courier", 15))
        self.tracker_word.pack()
        
    def showResult(self, win):
        if(win == 2):
            return
        elif(win == 1):
            word = 'Yippee! You Guessed it Right.'
        elif(win == 0):
            word = 'Sorry! You Failed to guess it.'
            self.printCorrectAnswer();
            
        if(self.result != None):
            self.result.destroy()
        self.result = tk.Label(self.result_frame, text=word, font=("Courier", 14))
        self.result.pack()
        if tk.messagebox.askyesno("New Game", "New Game?"):
            self.master.destroy()
            root = tk.Tk()
            app = App(root)
            app.mainloop()
        else:
            self.master.destroy()
    
    def printCorrectAnswer(self):
        self.correctAnswer = tk.Label(self.result_frame, text='Correct Answer: ' + self.word, font=("helvetica", 16, 'italic'))
        self.correctAnswer.pack(side=BOTTOM, pady=10)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()