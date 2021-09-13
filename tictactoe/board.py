from cell import Cell


class Board:
    def __init__(self):
        self.board = [
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()]
        ]

    def display(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col].get_status(), end=" ")
            print()

    def play(self, player_symbol, row, col):
        if self.board[row][col].is_empty():
            self.board[row][col].set_status(player_symbol)
            return True
        else:
            return False

    def winner(self):
        # check rows
        for row in range(3):
            if self.board[row][0].get_status() != '-' and \
                    self.board[row][0].get_status() == self.board[row][1].get_status() and \
                    self.board[row][0].get_status() == self.board[row][2].get_status():
                return self.board[row][0].get_status()
        # check columns
        for col in range(3):
            if self.board[0][col].get_status() != '-' and \
                    self.board[0][col].get_status() == self.board[1][col].get_status() and \
                    self.board[0][col].get_status() == self.board[2][col].get_status():
                return self.board[0][col].get_status()
        # check diagonals
        if self.board[0][0].get_status() != '-' and \
                self.board[0][0].get_status() == self.board[1][1].get_status() and \
                self.board[0][0].get_status() == self.board[2][2].get_status():
            return self.board[0][0].get_status()
        if self.board[0][2].get_status() != '-' and \
                self.board[0][2].get_status() == self.board[1][1].get_status() and \
                self.board[0][2].get_status() == self.board[2][0].get_status():
            return self.board[0][2].get_status()
        # No winner
        return None

    def tie(self):
        if self.winner() is None:
            for row in range(3):
                for col in range(3):
                    if self.board[row][col].is_empty():
                        return False
            return True
        else:
            return False

