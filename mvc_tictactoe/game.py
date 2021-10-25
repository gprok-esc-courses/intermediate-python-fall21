# Empty: 0
# Player X: 1
# Player O: 2
from mvc_tictactoe.player import Player


class Game:
    def __init__(self):
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.player_x = Player('A', 'X', 1)
        self.player_o = Player('B', 'O', 2)
        self.current_player = self.player_x

    def play(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = self.current_player.value
            self.current_player = self.player_x if self.current_player == self.player_o else self.player_o
            return True
        else:
            print("Cell not empty")
            return False