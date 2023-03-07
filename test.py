import unittest
from player import Player
from card import Card
from suit import Suit
from rank import Rank 

class TestPlayer(unittest.TestCase):
    def test_empty_hand(self):
        """
        Test for retrieving card from empty hand.

        """
        p = Player()
        self.assertRaises(IndexError, p.get_card, 0)


    def test_add_card(self):
        """
        Testing for adding card
        """
        p = Player()
        c = Card(Rank.ACE, Suit.HEART)
        p.add_card(c)
        self.assertEqual(p.hand == [c],True)


if __name__ == '__main__':
    unittest.main()
