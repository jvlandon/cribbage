from deck import Hand, Deck, Card

class Player:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.hand = Hand([], False)
        self.score = 0