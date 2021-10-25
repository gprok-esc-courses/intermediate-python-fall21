from tkinter import *


class Cell(Button):
    def __init__(self, container, row, col):
        super().__init__(container)
        self.row = row
        self.col = col
        # self.configure(text="-", command=container.control.play(self.row, self.col))
        self.configure(text="-", command=lambda: container.control.play(self.row, self.col))

    def set_symbol(self, symbol):
        self.configure(text=symbol)


