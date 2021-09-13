from board import Board
from player import Player


class Game:
    def __init__(self):
        self.player_x = None
        self.player_o = None
        self.current_player = None
        self.board = None

    def setup(self):
        self.board = Board()
        name_x = input("Player X name: ")
        name_o = input("Player O name: ")
        self.player_x = Player(name_x, 'X')
        self.player_o = Player(name_o, 'O')
        self.current_player = self.player_x

    def play_again(self):
        self.board = Board()
        self.current_player = self.player_x

    def start(self):
        while True:
            print(self.current_player.get_name() + " plays")
            try:
                row = int(input("Row: "))
                col = int(input("Column: "))
            except ValueError:
                print("Invalid input, please numbers only")
                continue
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Values 1, 2, or 3 ony")
                continue
            if self.board.play(self.current_player.get_symbol(), row-1, col-1):
                self.board.display()
                # play was valid, look for winner or tie, if no winner or tie change player
                winner = self.board.winner()
                print("====> ", winner)
                if winner is not None:
                    print("Winner " + winner)
                    break
                elif self.board.tie():
                    print("Tie!")
                    break
                else:
                    self.current_player = self.player_x if self.current_player == self.player_o else self.player_o
            else:
                print("Invalid move, try again")
        play_again = input("Play again? y/n ")
        if play_again == 'y':
            self.play_again()
            self.start()
        else:
            print("Bye ...")


if __name__ == '__main__':
    game = Game()
    game.setup()
    game.start()



