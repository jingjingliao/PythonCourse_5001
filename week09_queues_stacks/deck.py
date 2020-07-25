import random as r
from card import Card


class Deck:
    """A deck of cards"""
    def __init__(self, size="full"):
        if size == "mini":
            suits = ["hearts", "spades"]
            values = ['ace', '2']
        else:
            suits = ["hearts", "spades", "diamonds", "clubs"]
            values = ['ace', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'jack', 'queen', 'king']

        self.cards = [Card(suit, value)
                      for suit in suits
                      for value in values]
        r.shuffle(self.cards)

    def deal_one(self):
        """Deal a card from the deck"""
        return self.cards.pop()