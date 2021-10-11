from tkinter import *
from game import Game


def play_again():
    game.select_value()
    button['state'] = "active"
    play_again_btn['state'] = "disabled"


def check():
    try:
        value = int(field.get())
        result = game.check_value(value)
        if result == -1:
            feedback.configure(text=str(value) + " go up")
        elif result == 1:
            feedback.configure(text=str(value) + " go down")
        else:
            feedback.configure(text="Found! " + str(game.steps) + " steps")
            button['state'] = "disabled"
            play_again_btn['state'] = "active"
        field.delete(0,END)
    except ValueError:
        print("Invalid input")


window = Tk()
game = Game()
game.select_value()

title = Label(window, text="Guess Number")
title.grid(column=0, row=0)

field = Entry(window)
field.grid(column=0, row=1)

button = Button(window, text="Check", command=check)
button.grid(column=1, row=1)

feedback = Label(window, text="")
feedback.grid(column=0, row=2)

play_again_btn = Button(window, text="Play again", command=play_again)
play_again_btn.grid(column=1, row=2)
play_again_btn['state'] = "disabled"

window.mainloop()