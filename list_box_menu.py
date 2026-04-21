from tkinter import *

window = Tk()
window.geometry("350x400")

def add_item():
    b = box.get()

    list.insert(END,b)
    box.delete(0,END)

def remove_item():
    selection = list.curselection()
    if selection:
        list.delete(selection[0])

def remove_all_item():
    list.delete(0,END)

box= Entry(window)
box.place(x= 10,y= 10)

add= Button(window, text= "add", width = 5,command= add_item)
add.place(x= 150, y= 10)

remove= Button(window, text ="remove", width= 5, command = remove_item)
remove.place(x= 200, y= 10)

all = Button(window, text= "remove all", width = 10, command = remove_all_item)
all.place(x= 250 ,y = 10)

list = Listbox(window, height= 20, width= 50, bg ="sky blue")
list.place(x= 10, y= 50)
window.mainloop()