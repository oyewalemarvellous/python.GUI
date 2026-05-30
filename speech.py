from tkinter import *
from gtts import gTTS
import os

window= Tk()
window.geometry("300x300")

def get_entry():
    g= enter_word.get()
    language = "en"
    h= gTTS(text= g, lang= language, slow= False)
    h.save("sound.wav")
    os.system("sound.wav")

label= Label(window, text = "Text to speech")
label.pack()

enter_word= Entry(window)
enter_word.pack()

interprete= Button(window, text= "interprete", command= get_entry)
interprete.pack()

window.mainloop()