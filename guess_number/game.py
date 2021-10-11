import random


class Game:
    def __init__(self):
        self.value = 0
        self.steps = 0

    def select_value(self):
        self.value = random.randint(0, 100)
        self.steps = 0

    def check_value(self, v):
        self.steps += 1
        if v < self.value:
            return -1
        elif v > self.value:
            return 1
        else:
            return 0



