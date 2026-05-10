import unittest
import random
from players import Player
from deck import Deck, Card, Hand
from discard import discard_to_crib

random.seed(0)
deck=Deck()
deck.shuffle()
player1 = Player("p1")
player2 = Player("p2")
deck.deal([player1, player2])
print(player1.hand.cards)
print(player2.hand.cards)
crib = Hand([], True)
common = Card("5", "♠")
discard_to_crib(player1, player2, crib)
print(crib.cards)

class MyTestCase(unittest.TestCase):
    def test_deal(self):
        self.assertEqual(len(crib.cards), 4)  # cards added to crib
        self.assertEqual(crib.score_hand(common), 12)


if __name__ == '__main__':
    unittest.main()
