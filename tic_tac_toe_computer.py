from tkinter import *
import time
import random

window= Tk()
window.geometry("150x100")
window.config(bg= "sky blue")

turn = "player"  

def g():
    global turn
    button_1.configure(text= "")
    button_2.configure(text= "")
    button_3.configure(text= "")
    button_4.configure(text= "")
    button_5.configure(text= "")
    button_6.configure(text= "")
    button_7.configure(text= "")
    button_8.configure(text= "")
    button_9.configure(text= "")
    l.configure(text= "")
    turn = "player"

def win():
    global turn
    if button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        
        
    elif button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)

    elif button_4.cget("text") == button_5.cget("text") == button_6.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_4.cget("text") == button_5.cget("text") == button_6.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_1.cget("text") == button_2.cget("text") == button_3.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_7.cget("text") == button_8.cget("text") == button_9.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_7.cget("text") == button_8.cget("text") == button_9.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_1.cget("text") == button_4.cget("text") == button_7.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_1.cget("text") == button_4.cget("text") == button_7.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_2.cget("text") == button_5.cget("text") == button_8.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_2.cget("text") == button_5.cget("text") == button_8.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_3.cget("text") == button_6.cget("text") == button_9.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_3.cget("text") == button_6.cget("text") == button_9.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
    
    elif button_1.cget("text") == button_5.cget("text") == button_9.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)
        
    elif button_1.cget("text") == button_5.cget("text") == button_9.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
    
        
    elif button_3.cget("text") == button_5.cget("text") == button_7.cget("text") == "X":
        turn = "player"
        l.configure(text= turn + " wins")
        window.after(1000,g)

    elif button_3.cget("text") == button_5.cget("text") == button_7.cget("text") == "O":
        turn = "computer"
        l.configure(text= turn + " wins")
        window.after(1000,g)
    
def tie():
    global turn 
    b = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]

    for buton in b:
        if buton.cget != "":
            l.configure(text= "tie")
    

def computer_move():
    global turn
    buttons =[button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]
    empty = []

    for button in buttons:
        if button.cget("text") == "":
            empty.append(button)

    if empty and len(empty) != 9:
        c = random.choice(empty)
        c.configure(text="O")
        turn = "player"
    win()
         

def b1():
    global turn
    b = button_1.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_1.configure(text= "X")
            win()
            window.after(1000,computer_move)

def b2():
    global turn
    b = button_2.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_2.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass


def b3():
    global turn
    b = button_3.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_3.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass

def b4():
    global turn
    b = button_4.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_4.configure(text= "X")
            win()
            window.after(1000,computer_move)
            
            pass

def b5():
    global turn
    b = button_5.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_5.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass

def b6():
    global turn
    b = button_6.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_6.configure(text= "X")
            win()
            window.after(1000,computer_move)
            
            pass

def b7():
    global turn
    b = button_7.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_7.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass


def b8():
    global turn
    b = button_8.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_8.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass

def b9():
    global turn
    b = button_9.cget("text")
    if b == "":
        if turn == "player":
            turn= "computer"
            button_9.configure(text= "X")
            win()
            window.after(1000,computer_move)
            turn = "player"
            pass

button_1 = Button(window,text= "", width= 5,background="black", foreground= "white",command= b1)
button_1.grid(column= 0, row= 0)

button_2 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b2)
button_2.grid(column= 1, row= 0)

button_3= Button(window,text= "", width= 5,background="black", foreground= "white", command= b3)
button_3.grid(column= 2, row= 0)

button_4 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b4)
button_4.grid(column= 0, row= 1)

button_5 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b5)
button_5.grid(column= 1, row= 1)

button_6 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b6)
button_6.grid(column= 2, row= 1)

button_7 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b7)
button_7.grid(column= 0, row= 2)

button_8 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b8)
button_8.grid(column= 1, row= 2)

button_9 = Button(window,text= "", width= 5,background="black", foreground= "white", command= b9)
button_9.grid(column= 2, row= 2)

l = Label(window, background= "black", foreground= "white")
l.grid(columnspan=3, row= 3)

window.mainloop()