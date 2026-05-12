from tkinter import *
from tkinter.filedialog import *


window = Tk()
window.geometry("300x300")

def add_file():
    b = g.get()
    file.insert(END,b)
    g.delete(0,END)

def delete_file():
    select = file.curselection()
    if select:
        file.delete(select[0])

def delete_all_file():
    file.delete(0,END)

def save_file():
    output = asksaveasfile(defaultextension= ".txt")
    if output is not None:
        for i in file.get(0,END):
            print(i,file= output)
    file.delete(0,END)

def open_file():
    input = askopenfile(title="open file")
    if input is not None:
        file.delete(0,END)
        item= input.readlines()
        for i in item:
            file.insert(END,i)

g = Entry(window)
g.grid(column= 0, row= 0)

add_button = Button(window,text= "add", width= 10, height= 1, command= add_file)
add_button.grid(column= 1, row= 0)

delete_button = Button(window, text= "delete", width= 10, height= 1, command= delete_file)
delete_button.grid(column= 1, row= 1)

save_button= Button(window, text= "save", width= 10, height= 1, command= save_file)
save_button.grid(column= 2, row= 1)

open_button = Button(window, text= "open", width= 10, height= 1, command= open_file)
open_button.grid(column= 2, row= 0)

delete_all = Button(window, text= "delete all", width= 15, height= 1, command= delete_all_file)
delete_all.grid(column= 0, row= 1)

file = Listbox(window, height=10, width= 48)
file.grid (columnspan= 3, row= 3)

window.mainloop()