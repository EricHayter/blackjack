from suit import Suit
from rank import Rank

class Card:
    def __init__(self, rank: Rank, suit: Suit):
       self.rank = rank
       self.suit = suit

    def __repr__(self):
        return self.rank.name + " " + self.suit.name

    #@property
    #def suit(self):
    #    return self._suit

    #@property
    #def rank(self):
    #    return self.rank

    #@suit.getter
    #def suit() -> Suit:
    #    return self.suit

    
    #@rank.getter
    #def rank() -> Rank:
    #    return self.rank
