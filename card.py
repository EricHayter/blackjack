from suit import Suit
from rank import Rank

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return self._rank.name + " " + self._suit.name

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank
