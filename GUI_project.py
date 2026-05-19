from tkinter import *

window= Tk()
window.geometry("300x400")

first= ""
second= ""
operator= ""

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
     global first, second, operator

        if operator == "":
            first += "2"
            a.configure(text=first)
        else:
            second += "2"
            a.configure(text=second)
    pass
def number3():
     global first, second, operator

        if operator == "":
            first += "3"
            a.configure(text=first)
        else:
            second += "3"
            a.configure(text=second)
    pass
def number4():
     global first, second, operator

        if operator == "":
            first += "4"
            a.configure(text=first)
        else:
            second += "4"
            a.configure(text=second)
    pass
def number5():
     global first, second, operator

        if operator == "":
            first += "5"
            a.configure(text=first)
        else:
            second += "5"
            a.configure(text=second)
    pass
def number6():
     global first, second, operator

        if operator == "":
            first += "6"
            a.configure(text=first)
        else:
            second += "6"
            a.configure(text=second)
    pass
def number7():
     global first, second, operator

        if operator == "":
            first += "7"
            a.configure(text=first)
        else:
            second += "7"
            a.configure(text=second)
    pass
def number8():
     global first, second, operator

        if operator == "":
            first += "8"
            a.configure(text=first)
        else:
            second += "8"
            a.configure(text=second)
    pass
def number9():
     global first, second, operator

        if operator == "":
            first += "9"
            a.configure(text=first)
        else:
            second += "9"
            a.configure(text=second)
    pass
def number0():
     global first, second, operator

        if operator == "":
            first += "0"
            a.configure(text=first)
        else:
            second += "0"
            a.configure(text=second)
    pass
def add():
    global operator
    operator = "+"
    pass
def subtract():
    global operator
    operator = "-"
    pass
def divide():
    global operator
    operator = "/"
    pass
def multiply():
    global operator
    operator = "*"
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

divide_button = Button(window, text = "/", width= 5, height= 2, command= divide)
divide_button.grid(column= 3, row= 2)

multiply_button = Button(window, text = "x", width= 5, height= 2, command= multiply)
multiply_button.grid(column= 3, row= 3)

subtract_button = Button(window, text = "-", width= 5, height= 2, command= subtract)
subtract_button.grid(column= 3, row= 4)

equal_button = Button(window, text = "=", width= 5, height= 2, command= equal)
equal_button.grid(column= 2, row= 4)

window.mainloop()
