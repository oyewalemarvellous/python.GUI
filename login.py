from tkinter import *

window = Tk()
window.geometry("200x200")

def login():
    username = input_1.get()
    password = input_2.get()

    if username == "Ezekiel" and password == "1234":
        label_3.config(text = "login succeful")
    else:
        label_3.config(text = "login invalid")

label_1 = Label(window, text = "Userame : ")
label_1.grid(row = 0, column = 0)
input_1 = Entry(window, width = 20)
input_1.grid(row = 0, column = 1)

label_2 = Label(window, text = "Password : ")
label_2.grid(row = 1, column = 0)
input_2 = Entry(window, width = 20)
input_2.grid(row = 1, column = 1)

sign_in_button = Button(window, text = "login", command = login)
sign_in_button.grid(row =2, column = 0, columnspan= 2)

label_3 = Label(window)
label_3.grid(row = 3, column = 0, columnspan= 2)

window.mainloop()