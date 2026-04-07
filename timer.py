from tkinter import *
import time
window = Tk()
window.geometry("400x200")


def counter():
    s = int(seconds.get())
    m = int(minutes.get())
    h = int(hours.get())

    total_time = (3600 * h) + (60 * m) + s 

    while total_time >- 1:
        s -= 1
        if s == 0:
            m -= 1
            s = 60
        elif m == 0 and s == 0 :
            m = 59
            s = 59
            h -=1

        sec_var.set(s)
        hr_var.set(h)
        min_var.set(m)
        window.update()
        time.sleep(1)
        total_time -= 1


sec_var = StringVar()

hr_var = StringVar()

min_var = StringVar()

seconds = Entry(window,bg = "black", width = 5, foreground = "white")
seconds.place(x = 300, y = 50)

sec = Label(window, textvariable= sec_var)
sec.place(x = 240, y = 50)

minutes = Entry(window, bg = "black", width = 5,foreground = "white")
minutes.place(x = 200, y = 50)

min = Label(window, textvariable= min_var)
min.place(x = 140, y = 50)

hours = Entry(window, bg = "black", width = 5, foreground = "white")
hours.place(x = 100, y = 50)

hrs = Label(window, textvariable= hr_var)
hrs.place(x = 40, y = 50)

start = Button(window, text = "Start", command = counter)
start.place(x =200, y = 100)

window.mainloop()