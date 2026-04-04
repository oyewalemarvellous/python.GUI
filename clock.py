from tkinter import *
from time import  strftime

window = Tk()
window.title("Clock")
window.geometry("230x70")
window.configure(bg ="black")


def timer():
    t = strftime("%H:%M:%S")
    label.config(text = t)
    label.after(1000,timer)
label = Label(window, text = "hello", font = ("arial",30,"bold"),background= "black",foreground="white",)
label.pack(anchor = "center")
timer()
window.mainloop()