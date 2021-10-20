from game_ui import GameUI


class Controller:
    def __init__(self):
        self.ui = GameUI(self)

    def play(self, row, col):
        print("button clicked at ", row, col)


app = Controller()