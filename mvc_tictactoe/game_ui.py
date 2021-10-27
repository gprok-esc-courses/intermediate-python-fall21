from tkinter import *
from mvc_tictactoe.cell import Cell


class GameUI(Tk):
    def __init__(self, control):
        super().__init__()
        self.control = control
        self.geometry('300x300')
        self.title("Tic Tac Toe MVC")
        self.add_cells()
        self.message = Label(text="-")
        self.message.grid(column=0,row=1)
        self.play_again_btn = Button(text="Play again", command=control.play_again)
        self.play_again_btn.grid(column=0, row=2)

    def start(self):
        self.mainloop()

    def add_cells(self):
        frame = Frame()
        self.cells = [
            [Cell(frame,0,0), Cell(frame,0,1), Cell(frame,0,2)],
            [Cell(frame,1,0), Cell(frame,1,1), Cell(frame,1,2)],
            [Cell(frame,2,0), Cell(frame,2,1), Cell(frame,2,2)]
        ]
        for row in range(0, 3):
            for col in range(0, 3):
                self.cells[row][col].grid(column=col, row=row)
        frame.grid(column=0, row=0)

    def set_cell_symbol(self, row, col, symbol):
        self.cells[row][col].set_symbol(symbol)

    def display_message(self, message):
        self.message.configure(text=message)

    def clear_message(self):
        self.message.configure(text="-")

    def game_over(self):
        for row in range(0, 3):
            for col in range(0, 3):
                self.cells[row][col]['state'] = "disabled"

    def play_again(self):
        self.clear_message()
        for row in range(0, 3):
            for col in range(0, 3):
                self.cells[row][col]['state'] = "active"
                self.cells[row][col].configure(text="-")


# just for testing
if __name__ == '__main__':
    game = GameUI()
