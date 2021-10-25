from mvc_tictactoe.game_ui import GameUI
from mvc_tictactoe.game import Game


class Controller:
    def __init__(self):
        self.ui = GameUI(self)
        self.game = Game()
        self.ui.start()

    def play(self, row, col):
        print("button clicked at ", row, col)
        symbol = self.game.current_player.symbol
        if self.game.play(row, col):
            self.ui.set_cell_symbol(row, col, symbol)
            # check winner
            # if no winner check tie


app = Controller()