from tkinter import *
from game import Game


class GameUI:
    def __init__(self):
        self.window = Tk()
        self.game = Game()
        self.game.select_value()

        title = Label(self.window, text="Guess Number")
        title.grid(column=0, row=0)

        self.field = Entry(self.window)
        self.field.grid(column=0, row=1)

        self.button = Button(self.window, text="Check", command=self.check)
        self.button.grid(column=1, row=1)

        self.feedback = Label(self.window, text="")
        self.feedback.grid(column=0, row=2)

        self.play_again_btn = Button(self.window, text="Play again", command=self.play_again)
        self.play_again_btn.grid(column=1, row=2)
        self.play_again_btn['state'] = "disabled"

        self.window.mainloop()

    def play_again(self):
        self.game.select_value()
        self.button['state'] = "active"
        self.play_again_btn['state'] = "disabled"

    def check(self):
        try:
            value = int(self.field.get())
            result = self.game.check_value(value)
            if result == -1:
                self.feedback.configure(text=str(value) + " go up")
            elif result == 1:
                self.feedback.configure(text=str(value) + " go down")
            else:
                self.feedback.configure(text="Found! " + str(self.game.steps) + " steps")
                self.button['state'] = "disabled"
                self.play_again_btn['state'] = "active"
            self.field.delete(0, END)
        except ValueError:
            self.feedback.configure(text="Invalid input")


ui = GameUI()
