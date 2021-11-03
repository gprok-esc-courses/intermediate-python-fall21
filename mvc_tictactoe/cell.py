from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class Cell(QPushButton):
    def __init__(self, parent, controller, row, col):
        super().__init__(parent)
        self.row = row
        self.col = col
        self.clicked.connect(lambda: controller.control.play(self.row, self.col))
        self.setGeometry(90*col+20, 90*row+20, 80, 80)
        self.setStyleSheet("Cell {border: 3px dotted blue;}")
        self.setFont(QFont("Arial", 25))
        self.setText("-")

    def set_symbol(self, symbol):
        self.setText(symbol)


