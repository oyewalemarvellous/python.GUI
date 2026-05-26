from tkinter import *
from tkinter import messagebox

window= Tk()
window.geometry("530x400")

d= {"water":1.20, "bread": 2.90, "biscuit":2.10}
total= 0

def clear():
    error.config(text= "")
def add():
    global total
    g= Item.get()
    j= Quantity.get()
    if g in d:
        x = round(d[g] * int(j),2)
        reciept.insert(END,f"           {g:35} {j:25}{x}")
        Item.delete(0,END)
        Quantity.delete(0,END)
        
        total += x 
        current_total.config(text= str(total))      

    else:
        error.config(text= "item is currently out of stock")
        window.after(2000,clear)

def delete_reciept():
    select = reciept.curselection()
    if select:
        reciept.delete(select[0])

def buy():
    global total
    h= reciept.get(0, END)
    txt= ""
    t= ""
    for i in h:
        txt += i + "\n" 
    txt += " \n         total : " + str(total)
    messagebox.showinfo("reciept",txt)

title= Label(window, text= "Ezekiels Shop", font= ("arial", 15, "bold"))
title.grid(column= 0, row= 0, columnspan=3)

items= Label(window, text="         Items            Prices(€)", font= ("arial", 10, "bold"))
items.grid(column= 0, row= 1, rowspan= 2)

goods = Label(window, text= f"water{d['water']:25}\nbiscuit{d['biscuit']:25}\nbread{d['bread']:25}")
goods.grid(column= 0, row=3, rowspan= 2)

item_title= Label(window, text= "item")
item_title.grid(column= 4, row= 0)
quantity_title= Label(window, text= "quantity")
quantity_title.grid(column= 5, row= 0)
price_title= Label(window, text= "Price")
price_title.grid(column= 6, row= 0)
reciept= Listbox(window, height= 15, width=50)
reciept.grid(column= 4, row= 1, rowspan= 10, columnspan= 3)

item_label= Label(window, text="Item ")
item_label.grid(column= 0, row= 5, rowspan= 2)
Item= Entry(window)
Item.grid(column= 0, row= 6, rowspan= 2)

quantity_label= Label(window, text= "Quantity")
quantity_label.grid(column= 0, row= 8 )
Quantity= Entry(window)
Quantity.grid(column= 0, row= 9, rowspan= 2)

Enter_button= Button(window, text= "Enter", width= 15,command= add)
Enter_button.grid(column= 0, row= 11)
delete_button= Button(window, text= "Clear", width= 15, command= delete_reciept)
delete_button.grid(column= 0, row= 12)
pay_button= Button(window, text= "pay", width= 15, command= buy)
pay_button.grid(column= 0, row= 13)

current_label= Label(window, text= "Total : ")
current_label.grid(column= 5, row= 12)
current_total= Label(window, text= 0)
current_total.grid(column= 6, row=12)
error= Label(window, text="")
error.grid(column= 2, row= 13, columnspan= 4)
window.mainloop()