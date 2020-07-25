from die import Die


class PairOfDice:
    def __init__(self):
        """Has two Die class attributes"""
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        """roll two dies"""
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        """returns the sum of its Die objects' current values"""
        return (self.die1.current_value + self.die2.current_value)
