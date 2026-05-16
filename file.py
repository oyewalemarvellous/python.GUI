from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("550x500")

def add_file():
    b= name_entry.get()
    g= age_entry.get()
    r= address_entry.get()
    j= number_entry.get()


    if b != "" and  g != "" and r != "" and j != "":
        main_file.insert(END,f"{b:25} {g:10} {r:20} {j:10}")
        name_entry.delete(0,END)
        age_entry.delete(0,END)
        address_entry.delete(0,END)
        number_entry.delete(0,END)

def delete_file():
    select = main_file.curselection()
    if select:
        main_file.delete(select[0])
    pass

def delete_all_file():
    main_file.delete(0,END)
    pass

def save_file():
    output = asksaveasfile(defaultextension= ".txt")
    if output is not None:
        for i in main_file.get(0,END):
            print(i,file= output)
    main_file.delete(0,END)
    pass

def open_file():
    input = askopenfile(title="open file")
    if input is not None:
        main_file.delete(0,END)
        item= input.readlines()
        for i in item:
            main_file.insert(END,i)
    pass

main_file= Listbox(window, height= 20, width= 50)
main_file.grid(column= 0, row=1, rowspan= 8, columnspan=4 )

name_label = Label(window, text= "Name : ")
name_label.grid (column= 4, row= 1 , rowspan=2)

name_entry = Entry(window)
name_entry.grid(column= 5, row= 1, rowspan=2 )

age_label= Label(window, text= "Age : ")
age_label.grid(column=4 , row=3, rowspan= 2 )

age_entry= Entry(window)
age_entry.grid(column= 5, row= 3, rowspan=2)

address_label= Label(window, text= "Address : ")
address_label.grid(column= 4, row= 5, rowspan=2)

address_entry= Entry(window)
address_entry.grid(column=5, row=5, rowspan=2)

number_label= Label(window, text= "Number : ")
number_label.grid(column=4 , row= 7, rowspan=2)

number_entry = Entry(window)
number_entry.grid(column= 5, row= 7, rowspan=2)

add_button= Button(window, text= "Add", width= 22, command= add_file)
add_button.grid(column= 0, row= 9, columnspan=2)

delete_button= Button(window, text= "delete", width= 22, command= delete_file)
delete_button.grid(column= 2, row= 9, columnspan=2)

save_button= Button(window, text= "Save", width= 25, command= save_file)
save_button.grid(column= 4, row= 9, columnspan=2)

open_button= Button(window, text= "open", width= 35, command= open_file)
open_button.grid(column=0 , row= 10, columnspan= 3)

delete_all_file_button= Button(window, text= "delete all",width= 35, command= delete_all_file)
delete_all_file_button.grid(column= 3, row= 10, columnspan=3 )

name_title = Label(window,text= "Name" )
name_title.grid(column= 0, row= 0)

age_title = Label(window,text= "Age" )
age_title.grid(column= 1, row= 0)

address_title= Label(window, text= "Address")
address_title.grid(column=2, row= 0)

number_title = Label(window,text= "Number" )
number_title.grid(column= 3, row= 0)


window.mainloop()