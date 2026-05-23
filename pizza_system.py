from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("315x300")
window.title("Pizza Machine")

def reciept():
    Type= type_2.get()
    extras= type_3.get()
    pizza= f"""
    Pizza type : {Type}
    Drinks : {extras}
    extra cheese : """

    if plain_cheese.get() == 1:
        pizza += "Plain cheese,"
    if mozarella.get() == 1:
        pizza += " Mozarella cheese," 
    if gauda.get() == 1:
        pizza += " Gauda cheese" 

    pizza += "\n    Your Order is ready !!!"
    messagebox.showinfo("Order", pizza)

title= Label(window, text= "PIZZA MACHINE", font= ("arial", 15, "bold"))
title.grid(column= 0, row= 0, columnspan= 2)

type= StringVar()
type.set("None")
take_out= Radiobutton(window, text= "Take out", variable= type, value= "Take out")
take_out.grid(column= 0, row=1 )
eat_in= Radiobutton(window, text= "Eat in", variable= type, value= "Eat in")
eat_in.grid(column= 1, row= 1)

type_2= StringVar()
type_2.set("None")
pizza_type= Label(window, text= "Type of Pizza : ")
pizza_type.grid(column= 0, row= 2)
cheese= Radiobutton(window, text="Cheese pizza", variable= type_2, value= "Cheese pizza")
cheese.grid(column=0, row= 3)
pepperonni= Radiobutton(window, text="pepperonni pizza", variable= type_2, value= "pepperonni pizza")
pepperonni.grid(column=1, row= 3)
chicken= Radiobutton(window, text="chicken pizza", variable= type_2, value= "chicken pizza")
chicken.grid(column=0, row= 4)

type_3= StringVar()
type_3.set("None")
drink_option= Label(window, text= "Drink options : ")
drink_option.grid(column= 0, row= 6 )
water= Radiobutton(window, text="water", variable= type_3, value= "water")
water.grid(column=0, row= 7)
coke= Radiobutton(window, text="coke", variable= type_3, value= "coke")
coke.grid(column=1, row= 7)
sprite= Radiobutton(window, text="sprite", variable= type_3, value= "sprite")
sprite.grid(column=2, row= 7)

plain_cheese= IntVar()
mozarella= IntVar()
gauda= IntVar()
toppings= Label(window, text= "Extra toppings")
toppings.grid(column= 0, row= 8)
extra_cheese1=Checkbutton(window,text= "cheese", variable= plain_cheese)
extra_cheese1.grid(column= 0, row= 9)

extra_cheese2= Checkbutton(window, text= "Mozarella cheese", variable= mozarella)
extra_cheese2.grid(column= 1, row= 9)

extra_cheese3= Checkbutton(window, text= "gauda cheese", variable= gauda)
extra_cheese3.grid(column= 2, row= 9)

check_box= Button(window, text= "Place Order", command= reciept)
check_box.grid(column= 1, row= 10) 


"""

pizza_size= Label(window, text= "Select Pizza Size : ")
pizza_size.grid(column= 0, row= 5)

size= Spinbox(window,)"""

window.mainloop()