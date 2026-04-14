from tkinter import *

window= Tk()
window.geometry("300x400")
window.title("Survey")


title= Label(window, text= "Personal Survey", font= ("arial",15,"bold"))
title.place(x= 10, y= 10 )

def display():
    j = n.get()
    h = num.get()
    k = a.get()
    l = add.get()

    dis.config(text= f"name : {j}\nphone : {h}\nage : {k}\naddress : {l}")


name = Label(window,text= "name : ")
name.place(x= 10, y= 40)

n = Entry(window)
n.place (x= 70, y = 40)

number = Label(window,text= "number : ")
number.place(x= 10, y= 80)

num = Entry(window)
num.place(x= 70, y= 80)

age = Label(window,text= "age : ")
age.place(x= 10, y= 120)

a = Entry(window)
a.place(x= 70, y= 120)

address = Label(window,text= "address : ")
address.place(x= 10, y= 160)

add= Entry(window)
add.place(x= 70, y= 160)

enter = Button(window,text= "enter", command = display )
enter.place(x= 150,y = 200)

dis = Label(window)
dis.place(x= 10, y = 240)

window.mainloop()