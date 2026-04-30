import unittest
import random
from players import Player
from deck import Deck, Card, Hand
from discard import discard_to_crib
from pegging import *

random.seed(0)
deck=Deck()
deck.shuffle()
player1 = Player()
player2 = Player()
deck.deal([player1, player2])
print(player1.hand.cards)
print(player2.hand.cards)
crib = Hand([], True)
common = Card("5", "♠")
discard_to_crib(player1, player2, crib)

class MyTestCase(unittest.TestCase):
    def test_check_for_go(self):
        pegging_phase(player1, player2)


if __name__ == '__main__':
    unittest.main()
