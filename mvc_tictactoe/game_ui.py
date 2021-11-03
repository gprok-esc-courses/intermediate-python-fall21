from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

from mvc_tictactoe.cell import Cell


class GameUI:
    def __init__(self, control):
        self.app = QApplication(sys.argv)
        self.window = Window(control)

    def start(self):
        sys.exit(self.app.exec_())

    def set_cell_symbol(self, row, col, symbol):
        self.window.cells[row][col].set_symbol(symbol)

    def display_message(self, message):
        self.window.message.setText(message)

    def clear_message(self):
        self.window.message.setText("-")

    def game_over(self):
        for row in range(0, 3):
            for col in range(0, 3):
                self.window.cells[row][col].setEnabled(False)

    def play_again(self):
        self.clear_message()
        for row in range(0, 3):
            for col in range(0, 3):
                self.window.cells[row][col].setEnabled(True)
                self.window.cells[row][col].set_symbol("-")


class Window(QMainWindow):
    def __init__(self, control):
        super().__init__()
        self.control = control
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle("Tic Tac Toe MVC")
        self.add_cells()
        self.add_message_area()
        self.show()

    def add_cells(self):
        self.cells = [
            [Cell(self,self,0,0), Cell(self,self,0,1), Cell(self,self,0,2)],
            [Cell(self,self,1,0), Cell(self,self,1,1), Cell(self,self,1,2)],
            [Cell(self,self,2,0), Cell(self,self,2,1), Cell(self,self,2,2)]
        ]

    def add_message_area(self):
        self.message = QLabel(self)
        self.message.setStyleSheet("QLabel {border: 2px solid red;}")
        self.message.setText("-")
        self.message.setGeometry(40, 280, 150, 40)
        self.play_again = QPushButton(self)
        self.play_again.clicked.connect(self.control.play_again)
        self.play_again.setGeometry(40, 340, 150, 40)
        self.play_again.setText("Play Again")




