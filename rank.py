from aenum import Enum, NoAlias

class Rank(Enum):
    _settings_ = NoAlias

    ACE: int = 1
    TWO: int = 2
    THREE: int = 3
    FOUR: int = 4
    FIVE: int = 5
    SIX: int = 6
    SEVEN: int = 7
    EIGHT: int = 8
    NINE: int = 9
    TEN: int = 10
    JACK: int = 10
    QUEEN: int = 10
    KING: int = 10

