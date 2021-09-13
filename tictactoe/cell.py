
class Cell:
    def __init__(self):
        self.status = 'E'

    def get_status(self):
        if self.status == 'E':
            return '-'
        else:
            return self.status

    def set_status(self, player_symbol):
        self.status = player_symbol

    def is_empty(self):
        return self.status == 'E'


