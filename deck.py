from card_values import *
from itertools import combinations
import random

class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card((rank, suit)))
                random.shuffle(self.deck)

    def deal(self, players):
        for player in players:
            while len(player.hand) < 6:
                player.hand.append(self.deck.pop())

    def cut_deck(self):
        self.deck.pop(random.randrange(0, len(self.deck)))

class Card:

    def __init__(self, code):
        self.rank = code[0]
        self.suit = code[1]
        self.value = RANK_VALUES[self.rank]
        self.pos = RANK_NUMS[self.rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Hand:

    def __init__(self, cards):
        self.cards = cards

    def discard(self, hand_pos):
        card_index = hand_pos - 1
        if len(self.cards) == 6:
            if card_index < 0 or card_index > 5:
                raise Exception("please choose a number 1-6")
        elif len(self.cards) == 5:
            if card_index < 0 or card_index > 4:
                raise Exception("please choose a number 1-5")
        self.cards.pop(card_index)
    
    def find_fifteens(self, common):
        fifteen_list = []
        total = 0
        for card in self.cards:
            fifteen_list.append(card.value)
        fifteen_list.append(common.value)
        for i in range(2, len(fifteen_list)+1):
            for combo in combinations(fifteen_list, i):
                if sum(combo) == 15:
                    total += 2
        return total

    def find_pairs(self, common):
        total = 0
        all_cards = self.cards + [common]
        for combo in combinations(all_cards, 2):
            if combo[0].rank == combo[1].rank:
                total += 2
        return total

    def find_runs(self, common):
        all_cards = sorted(self.cards + [common], key=lambda card: card.pos)
        all_runs = []
        current_run = []
        for i in range(len(all_cards)):
            if not current_run or all_cards[i].pos == current_run[-1].pos + 1:
                current_run.append(all_cards[i])
            else:
                if len(current_run) >= 3:
                    all_runs.append(current_run)
        if len(current_run) >=3:
            all_runs.append(current_run)
        if not all_runs:
            return 0
        elif len(all_runs[0]) == 5:
            return 5
        elif len(all_runs[0]) == 4:
            return len(all_runs) * 4





    def find_flush(self, common):
        suits_in_hand = [card.suit for card in self.cards]
        if len(set(suits_in_hand)) == 1:
            if common.suit == suits_in_hand[0]:
                return 5
            return 4
        return 0

    def find_flush_crib(self, common):
        all_cards = self.cards + [common]
        all_suits = [card.suit for card in all_cards]
        if len(set(all_suits)) == 1:
            return 5
        return 0
    
    def nobs(self, common):
        for card in self.cards:
            if card.rank == "J" and card.suit == common.suit:
                return 1
        return 0
    
    def score_hand(self):
        total = 0
        total += self.find_fifteens
        total += self.find_pairs
        total += self.find_runs
        total += self.find_flush
        total += self.nobs
        return total


