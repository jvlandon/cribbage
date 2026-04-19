import unittest

from pegging import pegging_score
from players import Player
from deck import Card

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()

class MyTestCase(unittest.TestCase):
    def test_pegging_scores(self):
        pegging_score(15, [Card("4", "♣"), Card("6", "♥"), Card("5", "♠")], player1)
        self.assertEqual(player1.score, 5)  # run of three adds to 15
        pegging_score(16, [Card("4", "♣"), Card("4", "♥"), Card("4", "♠"), Card("4", "♦")], player2)
        self.assertEqual(player2.score, 12) #four of a kind
        pegging_score(30, [Card("9", "♣"), Card("7", "♥"), Card("8", "♠"), Card("6", "♠")], player3)
        self.assertEqual(player3.score, 4) #wonky run of 4
        pegging_score(23, [Card("6", "♣"), Card("5", "♠"), Card("5","♣"),  Card("7", "♣")], player4)
        self.assertEqual(player4.score, 0) #not a run
        pegging_score(15, [Card("5", "♣"),Card("5", "♠"),Card("5", "♥")], player4)
        self.assertEqual(player4.score, 8) #three of a kind for 15
        pegging_score(31, [Card("10","♥"), Card("9","♦"), Card("8","♦"), Card("4","♦")], player5)
        self.assertEqual(player5.score, 2)
        pegging_score(28, [Card("A", "♥"), Card("2", "♥"), Card("3", "♥"), Card("4", "♥"),
    Card("5", "♥"), Card("6", "♥"), Card("7", "♥")
], player6)
        self.assertEqual(player6.score, 7)

if __name__ == '__main__':
    unittest.main()
