from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("500x450")

d = {}
def delete_information():
    select = entry_box.curselection()
    if select:
        entry_box.delete(select[0])

def enter_info():
    g= age_entry.get()
    j= name_entry.get()
    h= class_entry.get()
    entry_box.insert(END,f"           {j:35} {g:25}{h}")
    d[j] = g
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    class_entry.delete(0,END)

def process():
    res = max(d, key= d.get)
    num= d[res]
    txt = f"{res} is the winner with a score of {num}%"
    messagebox.showinfo("Winner",txt)

title= Label(window, text= "The Day !!", font= ("arial", 15, "bold"))
title.grid(column= 0, row= 0)

names= Label(window, text= "Names")
names.grid(column= 0, row= 1 )
ages= Label(window, text= "Marks")
ages.grid(column= 1, row= 1 )
classes= Label(window, text= "Classes")
classes.grid(column= 2, row= 1 )

entry_box= Listbox(window, width= 50)
entry_box.grid(column= 0, row= 2, rowspan= 3, columnspan= 3)

name_label= Label(window, text= "Name : ")
name_label.grid(column= 3, row= 2)
age_label= Label(window, text= "Mark : ")
age_label.grid(column= 3, row= 3)
class_label= Label(window, text= " Class : ")
class_label.grid(column= 3, row= 4)

name_entry= Entry(window)
name_entry.grid(column= 4, row= 2)
age_entry= Entry(window)
age_entry.grid(column= 4, row= 3)
class_entry= Entry(window)
class_entry.grid(column= 4, row= 4)

enter_button= Button(window, text= "Enter info", command= enter_info)
enter_button.grid(column= 0, row= 5)

delete_button= Button(window, text= "delete info", command= delete_information)
delete_button.grid(column= 1, row= 5)

process_button= Button(window, text= "process info", command= process)
process_button.grid(column= 2, row= 5)

window.mainloop()