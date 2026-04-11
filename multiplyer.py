from tkinter import *

window = Tk()
window.title("Times table")
window.geometry("300x400")

def multiplyer():
    n = int(input.get())

    num = ""

    for i in range(1,13):
        j = i * n
        
        num += f"{n} X {i} = {j}\n"

    output.config(text = num )

input = Entry(window,width = 5)
input.place(x = 50, y= 15)

enter = Button(window, text= "Enter", command= multiplyer)
enter.place(x= 100, y= 10)

output = Label(window, font= ("arial",15,"bold"))
output.place(x = 100, y= 50)


window.mainloop()