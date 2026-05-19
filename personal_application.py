from tkinter import *
from tkinter.filedialog import * 

window= Tk()
window.geometry("300x300")

def submit():
    name= username_entry.get()
    password= password_entry.get()
    pass

    



title= Label(window, text= "Personal Application", font= ("arial", 20,"bold"))
title.grid (column= 0, row=0, columnspan= 3)

username_label= Label(window, text= "Username : ")
username_label.grid(column= 0, row=1)

username_entry= Entry(window)
username_entry.grid(column=1, row= 1, columnspan= 2)

password_label= Label(window, text= "Password : " )
password_label.grid(column= 0, row= 2)

password_entry= Entry(window, show="*")
password_entry.grid(column= 1, row= 2, columnspan= 2)

gender_label= Label(window, text= "Gender : ")
gender_label.grid(column= 0, row= 3)
gender= StringVar()
gender.set("None")

male_rb= Radiobutton(window, text= "Male", variable= gender, value= "male")
male_rb.grid(column= 1, row= 3)

female_rb= Radiobutton(window, text= "Female", variable= gender, value= "female")
female_rb.grid(column= 2, row= 3)

age_label= Label(window, text= "Age : " )
age_label.grid(column= 0, row= 4)

age_reciever= Spinbox(window, from_= 1, to = 100)
age_reciever.grid(column= 1, row= 4, columnspan= 2)

submit_button= Button(window, text= "Submit")
submit_button.grid(column= 0, row= 6, columnspan=2)

check_box= Checkbutton(window, text= "I Acknowledge")
check_box.grid(column= 1, row= 5, columnspan= 3) 

window.mainloop()