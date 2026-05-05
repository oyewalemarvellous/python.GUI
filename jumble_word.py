from tkinter import *
import random

window = Tk()
window.geometry("300x200")

def jumble():
    w = ["banana","apple","orange","grapes"]
    p = random.choice(w)
    converter = list(p) 
    random.shuffle(converter)
    replace = "".join(converter)
    words.config(text= replace)
    
def check():
    pass


words = Label(window)
words.place(x=130, y= 50)

title = Label(window, text= "JUMBLE WORDS", font=("arial",20,"bold"))
title.place(x = 50, y = 10 )
jumble()

typer = Entry(window, text= "hello")
typer.place(x= 80, y= 100)

check_button= Button(window,text= "check", command= check)
check_button.place(x= 120, y = 150)

window.mainloop()