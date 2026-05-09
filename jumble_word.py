from tkinter import *
import random
import time

window = Tk()
window.geometry("300x200")

checker = ""
point = 0

def jugler(x):
    converter = list(x) 
    random.shuffle(converter)
    replace = "".join(converter)
    words.config(text= f"guess the word : {replace}")
    
def jumble():
    global checker
    fruits = ["banana","apple","orange","grape","pineapple"]
    names = ["luke","james", "ezekiel", "marvelous", "emily"]
    place = ["pacific", "wellington"]
    science = ["photosynthesis", "hydrochloric_acid", "alkali", "hydrogen_peroxide"]
    l= [fruits,names,science,place]
    j= random.choice(l)
    p = random.choice(j)
    checker = p
    jugler(p)
    if j == names:
        hint_display.config(text= "it is a name of a person")
    elif j == fruits:
        hint_display.config(text= "it is a name of a fruit")
    elif j == place:
        hint_display.config(text= "it is a name of a place")
    elif j == science:
        hint_display.config(text= "associated with science")

            
def check():
    global checker, point
    if  typer.get() == checker:
        answer.config(text= "correct")
        window.update()
        time.sleep(1)
        typer.delete(0,END)
        answer.config(text= "")
        point += 1
        score.config(text= f"score : {point}",font= ("arial", 10, "bold"))
        jumble()
    else:
        answer.config(text= "wrong")
        window.update()
        time.sleep(1)
        typer.delete(0,END)
        answer.config(text= "")
        point -= 1
        score.config(text= f"score : {point}",font= ("arial", 10, "bold"))
        
title = Label(window, text= "JUMBLE WORDS", font=("arial",20,"bold"))
title.place(x = 30, y = 10 )

words = Label(window)
words.place(x=80, y= 50)

hint = Label(window, text= "hint : ")
hint.place(x=80, y = 70)

hint_display= Label(window)
hint_display.place(x= 110, y= 70)

answer = Label(window)
answer.place(x= 120, y= 120)

typer = Entry(window)
typer.place(x= 80, y= 100)

check_button= Button(window, text= "check", command= check)
check_button.place(x= 120, y = 150)

score = Label(window, text="score : ", font= ("arial", 10, "bold"))
score.place(x=10, y=  170)

jumble()

window.mainloop()