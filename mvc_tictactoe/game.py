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

    def get_winner(self):
        '''
        Checks for winner and returns proper value
        :return: None if no winner, 'X' or 'O' if winner is X or O.
        '''
        # Check rows and columns
        for i in range(0, 3):
            if self.grid[i][0] == self.grid[i][1] and self.grid[i][0] == self.grid[i][2] and self.grid[i][0] != 0:
                return 'X' if self.grid[i][0] == 1 else 'O'
            if self.grid[0][i] == self.grid[1][i] and self.grid[0][i] == self.grid[2][i] and self.grid[0][i] != 0:
                return 'X' if self.grid[0][i] == 1 else 'O'
        # check diagonals
        if self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2] and self.grid[0][0] != 0:
            return 'X' if self.grid[0][0] == 1 else 'O'
        if self.grid[0][2] == self.grid[1][1] and self.grid[0][2] == self.grid[2][0] and self.grid[0][2] != 0:
            return 'X' if self.grid[0][2] == 1 else 'O'

    def is_tie(self):
        '''
        Checks for tie, checking that there are no zeros in the grid
        :return: True if tie, False otherwise
        '''
        for row in range(0, 3):
            for col in range(0, 3):
                if self.grid[row][col] == 0:
                    return False
        return True

    def play_again(self):
        self.current_player = self.player_x
        for row in range(0, 3):
            for col in range(0, 3):
                self.grid[row][col] = 0

