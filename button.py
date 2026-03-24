from tkinter import *
import random

window = Tk()
window.geometry("500x500")
window.configure(bg= "blue")

colours = ["green","blue","red","black","grey","orange"]
def change_colour():
    window.configure(bg = random.choice(colours))
b1 = Button(window, text= "click me",command = change_colour)
b1.pack(side= "top")

l1 = Label(window, text= "Hello World")
l1.place(x = 5, y= 10)

window.mainloop()