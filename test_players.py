import unittest
import random
from players import Player
from deck import Deck, Card, Hand

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
while len(player1.hand.cards) > 4:
    player_choice = int(input("Player 1, Please choose a card: "))
    card_choice = player1.discard(player_choice)
    if card_choice:
        crib.cards.append(card_choice)
while len(player2.hand.cards) > 4:
    player_choice = int(input("Player 2, Please choose a card: "))
    card_choice = player2.discard(player_choice)
    if card_choice:
        crib.cards.append(card_choice)
print(crib.cards)

class MyTestCase(unittest.TestCase):
    def test_deal(self):
        self.assertEqual(len(crib.cards), 4)  # cards added to crib
        self.assertEqual(crib.score_hand(common), 12)


if __name__ == '__main__':
    unittest.main()
