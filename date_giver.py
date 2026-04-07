from tkinter import *
from time import strftime

window = Tk()
window.geometry("400x200")
window.configure(bg = "black")


window.title("Date and time")


def timer():
    t = strftime("%I:%M %p")
    time.config(text = t)
    time.after(1000,timer)

def dates():
    d = strftime("%a %d %b %y")
    date.config(text = d)
    date.after(1000,dates)

    
time = Label(window, font = ("arial",30,"bold"), background = "black", foreground = "white")
time.place(x = 120, y = 50)

date = Label(window, font = ("arial",20,), background= "black", foreground = "white")
date.place(x = 120, y = 100)
timer()
dates()
window.mainloop()