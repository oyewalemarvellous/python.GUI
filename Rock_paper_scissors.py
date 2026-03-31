from tkinter import *
import tkinter.font as font 
import random

window = Tk()
window.geometry("500x400")

players_choice = " "
choices = ["Rock","Paper","Scissors"]

def winning():
    computer_choice = random.choice(choices)
    
    winner = ""
    
    if players_choice == "Paper" and computer_choice == "Rock":
        winner = "YOU WON"
    elif players_choice == "Paper" and computer_choice == "Scissors":
        winner = "COMPUTER WON"
    elif players_choice == "Rock" and computer_choice == "Paper":
        winner = "COMPUTER WON"
    elif players_choice == "Rock" and computer_choice == "Scissors":
        winner = "YOU WON"
    elif players_choice == "Scissors" and computer_choice == "Rock":
        winner = "COMPUTER WON"
    elif players_choice == "Scissors" and computer_choice == "Paper":
        winner = "YOU WON"
    elif players_choice == computer_choice:
        winner = "ITS A TIE"

    winner_display.config(text = winner )
    player_input.config(text = f"you selected : {players_choice}") 
    computer_input.config(text = f"computer selected : {computer_choice}")

def rock():
    global players_choice
    players_choice = "Rock"
    winning()

def scissors():
    global players_choice
    players_choice = "Scissors"
    winning()

def paper():
    global players_choice
    players_choice = "Paper"
    winning()



game_name = Label(window, text = "Rock Paper Scissors !!", font = font.Font(size = 20))
game_name.place(x = 120, y = 20)

winner_display = Label(window, text = " Winner is :", font = font.Font(size = 15))
winner_display.place(x = 150, y = 100)

rock_button = Button(window, text = "Rock", command = rock)
rock_button.place(x = 120, y = 170)

paper_button = Button(window, text = "Paper", command = paper )
paper_button.place(x = 200, y = 170)

scissors_button =  Button(window, text = "Scissors", command = scissors)
scissors_button.place(x = 280, y = 170)

player_input = Label(window, text = "you selected : ")
player_input.place(x = 120, y = 250)

computer_input = Label(window, text = "computer selected : ")
computer_input.place(x = 120, y = 280)


window.mainloop()