import unittest
from card_values import *
from deck import *

ace_s = Card(("A", "SPADES"))
two_c = Card(("2", "CLUBS"))
three_h = Card(("3", "HEARTS"))
four_h = Card(("4", "HEARTS"))
five_h = Card(("5", "HEARTS"))
five_s = Card(("5", "SPADES"))
six_s = Card(("6", "SPADES"))
seven_d = Card(("7", "DIAMONDS"))
eight_d = Card(("8", "DIAMONDS"))
eight_c = Card(("8", "CLUBS"))
nine_c = Card(("9", "CLUBS"))
nine_h = Card(("9", "HEARTS"))
ten_h = Card(("10", "HEARTS"))
ten_s = Card(("10", "SPADES"))
ten_c = Card(("10", "CLUBS"))
jack_c = Card(("J", "CLUBS"))
jack_h = Card(("J", "HEARTS"))
jack_s = Card(("J", "SPADES"))
jack_d = Card(("J", "DIAMONDS"))
king_s = Card(("K", "SPADES"))

hand1 = Hand([five_h, ten_c , seven_d , five_s])
hand2 = Hand([nine_c, ten_h, six_s, eight_d])
hand3 = Hand([five_h, two_c, four_h, ace_s])

class MyTestCase(unittest.TestCase):
    def check_values(self):
        print(f"ace value: {ace_s.value}")
        self.assertEqual(ace_s.value, "1")
        print(f"king value: {king_s.value}")
        self.assertEqual(king_s.value, "10")

    def test_find_fifteens(self):

        self.assertEqual(hand1.find_fifteens(three_h), 8)  # one 10 and one five x2, 7+3+5 x2
        self.assertEqual(hand2.find_fifteens(king_s), 2) # 9+6
        self.assertEqual(hand3.find_fifteens(three_h), 2)  # all cards add to 15

    def test_find_flush(self):

        self.assertEqual(Hand([five_h, ten_h, three_h, four_h]).find_flush(ace_s), 4)
        self.assertEqual(Hand([five_h, ten_h, three_h, four_h]).find_flush(Card(("K", "HEARTS"))), 5)
        self.assertEqual(Hand([five_h, ten_h, three_h, ace_s]).find_flush(Card(("K", "HEARTS"))), 0)

    def test_find_pairs(self):
        self.assertEqual(Hand([five_h, ten_c, five_s, ace_s]).find_pairs(ten_h), 4) #two pairs
        self.assertEqual(Hand([jack_c, jack_h, jack_s, jack_d]).find_pairs(ten_h), 12) #four of a kind

    def test_find_runs(self):
        self.assertEqual(Hand([ace_s, two_c, three_h, four_h]).find_runs(five_h), 5) #five in a row
        self.assertEqual(Hand([five_h, five_s, six_s, seven_d]).find_runs(four_h), 8) #two runs of four
        self.assertEqual(Hand([jack_h, nine_c, jack_c, nine_h]).find_runs(ten_s), 12) #four runs of three
        self.assertEqual(Hand([ace_s, king_s, ten_h, seven_d]).find_runs(five_s), 0) #no runs


if __name__ == '__main__':
    unittest.main()
