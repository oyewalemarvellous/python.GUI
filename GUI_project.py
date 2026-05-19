from tkinter import *

window= Tk()
window.geometry("300x400")

first= ""
second= ""
third= ""

def number1():
    global first, second, operator

    if operator == "":
        first += "1"
        a.configure(text=first)
    else:
        second += "1"
        a.configure(text=second)
    pass
def number2():
    w= num2.cget("text")
    a.configure(text= w)
    pass
def number3():
    pass
def number4():
    pass
def number5():
    pass
def number6():
    pass
def number7():
    pass
def number8():
    pass
def number9():
    pass
def number0():
    pass
def add():
    pass
def subtract():
    global operator
    operator = "-"
    pass
def divide():
    pass
def multiply():
    pass
def equal():
    global first, second, operator

    if operator == "+":
        answer = int(first) + int(second)

    elif operator == "-":
        answer = int(first) - int(second)

    elif operator == "*":
        answer = int(first) * int(second)

    elif operator == "/":
        answer = int(first) / int(second)

    a.configure(text=str(answer))
    pass

a= Label(window, text= "0", font= ("arial",23,"bold"))
a.grid(column= 0,row= 0)

num1= Button(window, text= "1", width= 5, height= 2, command= number1)
num1.grid(column= 0, row= 1)

num2= Button(window, text= "2", width= 5, height= 2, command= number2)
num2.grid(column= 1, row= 1)

num3= Button(window, text= "3", width= 5, height= 2, command= number3)
num3.grid(column= 2, row= 1)

num4= Button(window, text= "4", width= 5, height= 2, command= number4)
num4.grid(column= 0, row= 2)

num5= Button(window, text= "5", width= 5, height= 2, command= number5)
num5.grid(column= 1, row= 2)

num6= Button(window, text= "6", width= 5, height= 2, command= number6)
num6.grid(column= 2, row= 2)

num7= Button(window, text= "7", width= 5, height= 2, command= number7)
num7.grid(column= 0, row= 3)

num8= Button(window, text= "8", width= 5, height= 2, command= number8)
num8.grid(column= 1, row= 3)

num9= Button(window, text= "9", width= 5, height= 2, command= number9)
num9.grid(column= 2, row= 3)

num0= Button(window, text= "0", width= 5, height= 2, command= number0)
num0.grid(column= 0, row= 4, columnspan= 3)

add_button = Button(window, text = "+", width= 5, height= 2, command= add)
add_button.grid(column= 3, row= 1)

divide_button = Button(window, text = "/", width= 5, height= 2, command= subtract)
divide_button.grid(column= 3, row= 2)

multiply_button = Button(window, text = "x", width= 5, height= 2, command= multiply)
multiply_button.grid(column= 3, row= 3)

subtract_button = Button(window, text = "-", width= 5, height= 2, command= subtract)
subtract_button.grid(column= 3, row= 4)

equal_button = Button(window, text = "=", width= 5, height= 2, command= equal)
equal_button.grid(column= 2, row= 4)

window.mainloop()
