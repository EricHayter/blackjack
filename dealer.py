from player import Player

class Dealer(Player):
    def __init__(self):
        super()

# might want to add some features to prevent people from getting
# entire hand of the dealer 
    
    def get_top_card(self) -> Card:
        if self._hand == []:
            yield IndexError

        return self._hand[0]
