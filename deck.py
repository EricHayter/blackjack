from itertools import product, repeat, chain
from random import shuffle
from typing import List

from card import Card
from rank import Rank
from suit import Suit


class Deck:
    DEFAULT_DECK: List[Card] = [Card(r, s) for r,s in  (product(list(Rank), list(Suit)))]
    def __init__(self, num_decks:int =6):
        '''
        Creates a deck of cards consisting of num_decks amount of 52-card standard decks and then
        shuffles the deck
        '''
        self.num_decks = num_decks
        self.cards = list(chain.from_iterable(repeat(c, num_decks) for c in Dealer.DEFAULT_DECK))
        shuffle(cards)


    def get_card(self) -> Card:
        '''
        returns a card popped off the deck
        '''
        return self.cards.pop()


    def get_num_cards(self) -> int:
        '''
        gives the amount of cards that are left in the deck
        '''
        return len(self.cards)

    
    def reset_deck(self) -> None:
        '''
        creates a new deck of the cards from num_decks decks of cards
        '''
        self.__init__(self.num_decks) 


    
    




