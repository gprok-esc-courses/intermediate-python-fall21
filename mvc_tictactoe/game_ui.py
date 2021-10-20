from tkinter import *
from cell import Cell

class GameUI(Tk):
    def __init__(self, control):
        super().__init__()
        self.control = control
        self.geometry('300x300')
        self.title("Tic Tac Toe MVC")
        self.add_cells()
        self.mainloop()

    def add_cells(self):
        self.cells = [
            [Cell(self,0,0), Cell(self,0,1), Cell(self,0,2)],
            [Cell(self,1,0), Cell(self,1,1), Cell(self,1,2)],
            [Cell(self,2,0), Cell(self,2,1), Cell(self,2,2)]
        ]
        for row in range(0, 3):
            for col in range(0, 3):
                self.cells[row][col].grid(column=col, row=row)


# just for testing
if __name__ == '__main__':
    game = GameUI()
