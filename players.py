from deck import Hand, Deck, Card

class Player:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.hand = Hand([], False)
        self.score = 0

    def discard(self, hand_pos):
        card_index = hand_pos - 1
        if card_index > len(self.hand.cards)-1 or card_index < 0:
            print("Invalid card choice")
            return None
        return self.hand.cards.pop(card_index)