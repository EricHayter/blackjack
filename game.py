from typing import List

from deck import Deck
from dealer import Dealer
from player import Player

class Game:
    MIN_CARDS = 52 # cards to play with before resetting the deck

    
    def __init__(self, num_players = 1):
        self.deck: Deck = Deck(num_decks=6)
        self.dealer: Dealer = Dealer()
        self.top_card = None
        self.players: List[Player] = [Player() for _ in range(num_players)]


    def play(self) -> None:
        if self.deck.get_num_cards() < Game.MIN_CARDS:
            self.deck.reset_deck()

        self.dealer.add_card(self.deck.get_card())
        self.dealer.add_card(self.deck.get_card())
        self.top_card = self.dealer.get_top_card() # reveal dealer's top card

        for p in self.players:
            p.add_card(self.deck.get_card())
            p.add_card(self.deck.get_card())

        # player action 
        for p in self.players:
            if p.get_hand_value() > 21:
                continue





# this is a working sum function for get_hand_value

