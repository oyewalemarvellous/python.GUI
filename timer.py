from tkinter import *
import time
window = Tk()
window.geometry("400x200")
window.configure(bg = "black")

total_time = ""
h = 0 
m = 0 
s = 0
def counter():
    global total_time,h,m,s

    s = int(seconds.get())
    m = int(minutes.get())
    h = int(hours.get())

    seconds.config(text="")
    hours.config(text= "")
    minutes.config(text= "")
    total_time = (3600 * h) + (60 * m) + s

    while total_time >- 1:
        if s > 0:
            s -=1

        if h > 0  and m ==0 and s ==0:
            h -= 1
            m = 60
        elif m > 0 and s == 0:
            m -= 1
            s = 59 
    
        elif h == 0 and m == 0 and s == 0:
            total_time = -1

        sec_var.set(s)
        hr_var.set(f"{h} :")
        min_var.set(f"{m} :")
        window.update()
        time.sleep(1)
        total_time -= 1

def stopper():
    global total_time
    total_time = -1

def resume():
    global h,s,m
    global total_time
    total_time = (3600 * h) + (60 * m) + s
    print(total_time)
    while total_time >- 1:
        if s > 0:
            s -=1

        if h > 0  and m ==0 and s ==0:
            h -= 1
            m = 60
        elif m > 0 and s == 0:
            m -= 1
            s = 59 
    
        elif h == 0 and m == 0 and s == 0:
            total_time = -1
            
    

        sec_var.set(s)
        hr_var.set(f"{h} :")
        min_var.set(f"{m} :")
        window.update()
        time.sleep(1)
        total_time -= 1 

sec_var = StringVar()

hr_var = StringVar()

min_var = StringVar()



seconds = Entry(window,bg = "black", width = 5, foreground = "white")
seconds.place(x = 300, y = 50)

sec = Label(window,bg = "black", foreground = "white", textvariable= sec_var)
sec.place(x = 220, y = 100)

minutes = Entry(window, bg = "black", width = 5,foreground = "white")
minutes.place(x = 200, y = 50)

min = Label(window,bg = "black", foreground = "white", textvariable= min_var)
min.place(x = 200, y = 100)

hours = Entry(window, bg = "black", width = 5, foreground = "white")
hours.place(x = 100, y = 50)

hrs = Label(window,bg = "black", foreground = "white", textvariable= hr_var)
hrs.place(x = 180, y = 100)

start = Button(window, text = "Start", width = 10, command = counter)
start.place(x =50, y = 160)

stop = Button(window, text = "Stop",width= 10, command = stopper )
stop.place(x = 150, y = 160)

res = Button(window, text ="Resume", width = 10,command = resume)
res.place(x = 250, y = 160)
window.mainloop()