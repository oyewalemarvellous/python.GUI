from tkinter import*
import speech_recognition as sr
from tkinter.ttk import *

window= Tk()
window.geometry("300x300")

def voice():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything")
        audio= r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            text= "sorry could not recognise your voice"
        txt.delete(1.0,END)
        txt.insert(END,text)
        

t= Label(window, text= "Voice recorder")
t.pack()

txt= Text(window, width= 30, height= 2)
txt.pack()

record= Button(window, text= "record", command= voice)
record.pack()

play= Button(window, text= "Play")
play.pack()


window.mainloop()