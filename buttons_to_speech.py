from tkinter import*
from gtts import gTTS
import os

window= Tk()
window.geometry("300x300")

def get_entry():
    g= hello.cget("text")
    language = "en"
    h= gTTS(text= g, lang= language, slow= False)
    h.save("sound.wav")
    os.system("sound.wav")

def get_entry_2():
    m= hey_there.cget("text")
    language = "en"
    h= gTTS(text= m, lang= language, slow= False)
    h.save("sound.wav")
    os.system("sound.wav")

def get_entry_3():
    i= how_are_you_doing.cget("text")
    language = "en"
    h= gTTS(text= i, lang= language, slow= False)
    h.save("sound.wav")
    os.system("sound.wav")

def get_entry_4():
    l= howdy.cget("text") 
    language = "en"
    h= gTTS(text= l, lang= language, slow= False)
    h.save("sound.wav")
    os.system("sound.wav")

t= Label(window, text= "Button to Speach",font= ("arial", 15, "bold"))
t.pack()

hello= Button(window, text= "hello", command= get_entry)
hello.pack()

hey_there= Button(window, text= "hey there", command= get_entry_2)
hey_there.pack()

how_are_you_doing= Button(window, text= "how are you doing", command= get_entry_3)
how_are_you_doing.pack()

howdy= Button(window, text= "howdy", command= get_entry_4)
hello.pack()

window.mainloop()