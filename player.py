from card import Card
from rank import Rank
from suit import Suit

from typing import List

class Player:
    def __init__(self):
        # implenment some sort of wager system?
        self.hand: List[Card] = list()


    def add_card(self, card: Card) -> None:
        '''
        Adds a card to the player's hand
        '''
        self.hand.append(card)


    def get_card(self, idx: int) -> Card: # this function may be pointless
        if idx < 0 or idx >= len(self.hand):
            if len(self.hand) == 0:
                raise IndexError('hand is empty')

            raise IndexError('index is out of range')

        return self.hand[idx]


    def get_hand(self) -> List[Card]:
        '''
        returns the player's hand
        '''
        return list(self.hand)

