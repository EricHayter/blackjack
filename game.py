from card import Card
from player import Player
from rank import Rank
from suit import Suit

class Game:
    MIN_CARDS = 52 # cards to play with before resetting the deck

    def get_hand_value(self, p: Player) -> int:
        s = 0
        a  = 0

        for c in p.get_hand():
            if True:
                break


    def __init__(self, num_players = 1):
       return


# this is a working sum function for get_hand_value
print(max([10 + n*10 if 10 + n*10 <= 21 else 0 for n in range(3)]))

