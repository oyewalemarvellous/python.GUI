from tkinter import *

window = Tk()
window.geometry("400x400")
window.configure(bg = "black")

def red():
    window.configure(bg = "red")

def yellow():
    window.configure(bg = "yellow")

def green():
    window.configure(bg = "green")


b1 = Button(window, text = "go", command = green)
b1.place(x = 200, y = 100)
b2 = Button(window, text = "slow down", command = yellow)
b2.place(x = 180 , y = 150)
b3 = Button(window, text = "stop", command = red )
b3.place(x = 195, y = 200)

l1 = Label(window, text = "TRAFFIC LIGHT")
l1.pack(side = "top")

window.mainloop()