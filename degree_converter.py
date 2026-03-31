from tkinter import * 

window = Tk()
window.geometry("200x200")

def conversion():
    n = int(input.get())

    convert = (n * 9/5) + 32
    
    output.config(text =  f"{convert}°")

label_1 = Label(window, text ="°C(celsius): ")
label_1.grid(row = 0, column = 0)
input  = Entry(window, width = 20 )
input.grid(row = 0, column = 1  )

label_2 = Label(window, text ="°F(fahrenheit ): ")
label_2.grid(row = 2, column = 0)
button = Button(window, text = "convert", command = conversion)
button.grid(row = 1, column = 0, columnspan = 2)

output = Label(window)
output.grid(row = 2,column = 1)

window.mainloop()