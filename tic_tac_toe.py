from tkinter import *

window= Tk()
window.geometry("130x90") 


turn = "X"
t= "win"

def win():
    if button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "X":
        l.configure(text= turn + "wins")\
    if button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "O":
        l.configure(text= turn + "wins")
    if (button_4.cget("text") == button_5.cget("text") == button_6.cget("text")) != "":
        l.configure(text= turn + "wins")
    if button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "X":
        l.configure(text= turn + "wins")
    if (button_7.cget("text") == button_8.cget("text") == button_9.cget("text")) != "":
        l.configure(text= turn + "wins")
    if (button_1.cget("text") == button_4.cget("text") == button_7.cget("text")) != "":
        l.configure(text= turn + "wins")
    if (button_2.cget("text") == button_5.cget("text") == button_8.cget("text")) != "":
        l.configure(text= turn + "wins")
    if (button_3.cget("text") == button_6.cget("text") == button_9.cget("text")) != "":
        l.configure(text= turn + "wins")
    if (button_1.cget("text") == button_5.cget("text") == button_9.cget("text")) != "":
        l.configure(text= turn + "wins")
    if (button_3.cget("text") == button_5.cget("text") == button_7.cget("text")) != "":
        l.configure(text= turn + "wins")

    


def b1():
    global turn
    b = button_1.cget("text")
    if b == "":
        button_1.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()

def b2():
    global turn
    b = button_2.cget("text")

    if b == "":
        button_2.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()

def b3():
    global turn
    b = button_3.cget("text")

    if b == "":
        button_3.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()

def b4():
    global turn
    b = button_4.cget("text")

    if b == "":
        button_4.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()
def b5():
    global turn
    b= button_5.cget("text")

    if b == "":
        button_5.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()
def b6():
    global turn
    b= button_6.cget("text")

    if b == "":
        button_6.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()
def b7():
    global turn
    b= button_7.cget("text")

    if b == "":
        button_7.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()

def b8():
    global turn
    b= button_8.cget("text")

    if b == "":
        button_8.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()
def b9():
    global turn
    b= button_9.cget("text")

    if b == "":
        button_9.configure(text= turn)
        if turn == "X":
            turn= "O"
        elif turn == "O":
            turn= "X"
    win()


button_1 = Button(window,text= "", width= 5, command= b1)
button_1.grid(column= 0, row= 0)

button_2 = Button(window,text= "", width= 5, command= b2)
button_2.grid(column= 1, row= 0)

button_3= Button(window,text= "", width= 5, command= b3)
button_3.grid(column= 2, row= 0)

button_4 = Button(window,text= "", width= 5, command= b4)
button_4.grid(column= 0, row= 1)

button_5 = Button(window,text= "", width= 5, command= b5)
button_5.grid(column= 1, row= 1)

button_6 = Button(window,text= "", width= 5, command = b6)
button_6.grid(column= 2, row= 1)

button_7 = Button(window,text= "", width= 5, command = b7)
button_7.grid(column= 0, row= 2)

button_8 = Button(window,text= "", width= 5, command= b8)
button_8.grid(column= 1, row= 2)

button_9 = Button(window,text= "", width= 5, command= b9)
button_9.grid(column= 2, row= 2)

l = Label(window)
l.grid(columnspan=3, row= 3)

window.mainloop()