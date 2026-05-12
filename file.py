from tkinter import *

window = Tk()
window.geometry("500x500")

main_file= Listbox(window, height= 20, width= 50)
main_file.grid(column= 0, row=0, rowspan= 10 )

name_label = Label(window, text= "Name : ")
name_label.grid (column= 1, row= 0 )

name_entry = Entry(window)
name_entry.grid(column= 2, row= 0)

age_label= Label(window, text= "Age : ")
age_label.grid(column=1 , row=1 )

age_entry= Entry(window)
age_entry.grid(column= 2, row=1 )

address_label= Label(window, text= "Address : ")
address_label.grid(column= 1, row= 2)

address_entry= Entry(window)
address_entry.grid(column=2, row=2)

add_button= Button(window, text= "Add")
add_button.place()
window.mainloop()