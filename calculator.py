from tkinter import *

w = Tk()
w.geometry("100x100")

def addition():
    n1= int(num_1.get())
    n2 = int(num_2.get())
    
    added_num = n1 + n2
    label.config(text = added_num)

def subtraction():
    n1 = int(num_1.get())
    n2 = int(num_2.get())

    subtracted_num = n1 - n2
    label.config(text = subtracted_num)


def multiplication():
    n1 = int(num_1.get())
    n2 = int(num_2.get())

    multiplied_num = n1 * n2
    label.config(text = multiplied_num)

def division():
    n1 = int(num_1.get())
    n2 = int(num_2.get())

    divided_num = n1 / n2
    label.config(text = divided_num)

num_1 = Entry(w, width = 10)
num_2 = Entry(w, width = 10)

add_button = Button(w, text = "+", command = addition)
divide_button = Button(w, text = "/", command = division)
multiply_button = Button(w, text = "x", command = multiplication)
subtract_button = Button(w, text = "-", command = subtraction)

num_1.grid (row = 1, column = 1)
num_2.grid(row = 1, column = 2 )

add_button.grid (row = 2, column = 1)
divide_button.grid(row = 2, column = 2)
multiply_button.grid(row = 3, column = 1)
subtract_button.grid(row = 3, column = 2)

label = Label(w)

label.grid(row = 4, column = 1 , columnspan= 2)
w.mainloop()