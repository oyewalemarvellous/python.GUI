from tkinter import *
import tkinter.font as font 
import random 
import time 

window = Tk()
window.geometry("400x200")
window.configure(bg = "light blue")


num = random.randint(1,35)
def number():
    global num
    i1 = int(input.get())
    if i1 == num :
        out.config(text = f"correct the answer is {num}")
        num = random.randint(1,35)
        out.after(2000,empty)
    else:
        if num > i1 :
            out.config(text = "guess a bigger number ")
        elif num < i1:
            out.config(text = "guess a smaller number")
        out.after (2000,hint)
        


def hint():
    if num % 2 == 0:
        out.config(text = "its an even number")
    else:
        out.config(text = "its a odd number")

def empty():
    out.config(text = "")


l1= Label(window, text = "Guess the number = ??",bg = "light blue" )
l1.place(x = 100 , y = 40)

name = Label(window, text = "Number Guessing Game", font = font.Font (size = 20), bg = "light blue")
name.pack(side = "top")

input = Entry(window, bg = "light blue")
input.place(x = 100, y = 70)

process= Button(window, text = "enter", bg = "light grey", command = number)
process.place(x = 150, y = 120)

out = Label(window, bg = "light blue")
out.place(x = 150, y = 100)

hints = Label(window, text = "hints :",bg = "light blue")
hints.place(x = 100, y = 100)

window.mainloop()