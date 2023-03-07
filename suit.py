from aenum import Enum, NoAlias

class Suit(Enum):
    _settings_ = NoAlias

    CLUB: int = 1
    DIAMOND: int = 2
    HEART: int = 3
    SPADE: int = 4
