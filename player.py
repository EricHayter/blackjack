from card import Card
from rank import Rank

from typing import List

class Player:
    STAND: int = 0
    HIT: int = 1
    SPLIT: int = 2

    def __init__(self):
        # implenment some sort of wager system?
        self._hand: List[Card] = list()
        self._playing: bool = True


    def add_card(self, card: Card) -> None:
        '''
        Adds a card to the player's hand
        '''
        self._hand.append(card)


    def get_card(self, idx: int) -> Card: # this function may be pointless
        if idx < 0 or idx >= len(self._hand):
            if len(self._hand) == 0:
                raise IndexError('hand is empty')

            raise IndexError('index is out of range')

        return self._hand[idx]


    @property
    def hand(self) -> List[Card]:
        '''
        returns a copy of the player's hand
        '''
        return list(self._hand)

    @property
    def playing(self) -> bool:
        return self._playing

    def stand(self) -> None:
        self._playing = False


    def get_hand_value(self) -> int:
        '''
        finds the value of the player's current hand
        '''
        sum_hand = 0
        num_aces  = 0

        for c in self._hand:
            if c.rank == Rank.ACE:
                num_aces += 1

            sum_hand += c.rank.value

        return max([sum_hand + n*10 if sum_hand + n*10 <= 21 else 0 for n in range(num_aces + 1)])


    def get_best_play(self, dealer_card: Card) -> int:
        # checking for pairs
        if self._hand[0].rank == self._hand[1].rank:
           return Player.HIT 
        elif self._hand[0].rank == Rank.ACE or self._hand[1].rank == Rank.ACE:
            return Player.HIT
        else:
            return Player.HIT

