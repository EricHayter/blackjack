from suit import Suit
from rank import Rank

class Card:
    def __init__(self, rank: Rank, suit: Suit):
       self.rank = rank
       self.suit = suit

    @property
    def suit(self):
        print('we be setting')
        return self.suit

    @property
    def rank(self):
        print('we be setting')
        return self.rank

    #@suit.getter
    #def suit() -> Suit:
    #    return self.suit

    
    #@rank.getter
    #def rank() -> Rank:
    #    return self.rank
