from mvc_tictactoe.game_ui import GameUI
from mvc_tictactoe.game import Game


class Controller():
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
            winner = self.game.get_winner()
            if winner is not None:
                self.ui.display_message(winner + " Wins!")
                self.ui.game_over()
            else:
                # if no winner check tie
                if self.game.is_tie():
                    self.ui.display_message("It's a Tie!")
                    self.ui.game_over()

    def play_again(self):
        self.ui.play_again()
        self.game.play_again()



app = Controller()