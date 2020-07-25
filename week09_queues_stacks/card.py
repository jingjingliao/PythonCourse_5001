class Card:
    """A playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit

    def __repr__(self):
        return (f"{self.__class__.__name__}"  # get class and name, for debugger
                f"(suit: {self.suit}, value: {self.value})")

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt(self, other):
        return self.value > other.value

    def __hash__(self):  # unique numerical code
        return hash((self.suit, self.value))
                     # string hashable, tuple hashable

    def num_value(self):
        ACE_VALUE = 11
        FACE_CARD_VALUE = 10
        if self.value == "ace":
            return ACE_VALUE
        elif (self.value == "jack" or
              self.value == "queen" or
              self.value == "king"):
            return FACE_CARD_VALUE
        else:
            return int(self.value)
