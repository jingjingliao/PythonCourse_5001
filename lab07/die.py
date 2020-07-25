import random


class Die:
    """Die class representing a single die, roll it and get current value"""
    def __init__(self):
        self.roll()

    def roll(self):
        MIN_POINT = 1
        MAX_POINT = 6
        self.current_value = random.randint(MIN_POINT, MAX_POINT)
