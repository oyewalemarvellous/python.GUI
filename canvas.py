from tkinter import *
from tkinter.colorchooser import askcolor

window= Tk()
window.geometry("650x700")

def activate_button(button, eraser_mode= False):
    global eraser_on, active_button
    active_button.config(relief= RAISED)
    button.config(relief= SUNKEN)
    active_button= button
    eraser_on= eraser_mode

def pen():
    activate_button(pen_button) 

def brush():
    activate_button(brush_button)   

def eraser():
    activate_button(eraser_button, eraser_mode= True)

def choosecolour():
    global eraser
    global colour
    eraser=False
    colour= askcolor(color= colour)[1]

def paint(event):
    global old_x, old_y
    if eraser == True:
        paint_colour= "white"
    else:
        paint_colour= colour
    
    if old_x and old_y:
        screen.create_line(old_x,old_y,event.x,event.y, fill= paint_colour, capstyle= ROUND, smooth= TRUE, splinesteps= 36)
    old_x= event.x
    old_y= event.y

def reset():
    global old_x, old_y
    old_x = None
    old_y = None     

old_x= None
old_y= None

line_width= 1

colour= "black"

eraser_on= False

screen= Canvas(window, bg= "white", width= 650, height= 600)
screen.grid(column= 0, row= 1, columnspan= 4)

screen.bind("<B1-Motion>", paint)

screen.bind("<ButtonRelease-1>", reset)

pen_button= Button(window, text= "pen", width= 20, command=pen)
pen_button.grid(column= 0, row= 0)

active_button= pen_button

eraser_button= Button(window, text= "Eraser", width= 20,command= eraser)
eraser_button.grid(column= 1, row= 0)

brush_button= Button(window, text= "brush", width= 20, command= brush)
brush_button.grid(column= 2, row= 0)

color_button= Button(window, text= "color", width= 20, command= choosecolour)
color_button.grid(column= 3, row= 0)

window.mainloop()