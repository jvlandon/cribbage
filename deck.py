from card_values import *
from itertools import combinations
import random

class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))
        random.shuffle(self.deck)

    def deal(self, players):
        for player in players:
            while len(player.hand.cards) < 6:
                player.hand.cards.append(self.deck.pop())

    def cut_deck(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUES[self.rank]
        self.pos = RANK_NUMS[self.rank]

    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Hand:

    def __init__(self, cards, is_crib=False):
        self.cards = cards
        self.is_crib = is_crib

    def __repr__(self):
        return f"{self.cards}"

    def find_fifteens(self, common, verbose = True):
        fifteen_list = []
        total = 0
        for card in self.cards:
            fifteen_list.append(card)
        fifteen_list.append(common)
        for i in range(2, len(fifteen_list)+1):
            for combo in combinations(fifteen_list, i):
                if sum(card.value for card in combo) == 15:
                    total += 2
                    if verbose:
                        print(f"Scores 2 points for making 15: {combo}!")
        return total

    def find_pairs(self, common, verbose = True):
        total = 0
        all_cards = self.cards + [common]
        for combo in combinations(all_cards, 2):
            if combo[0].rank == combo[1].rank:
                total += 2
                if verbose:
                    print(f"Scores 2 points for making a pair: {combo}!")
        return total

    def find_runs(self, common, verbose = True):
        all_cards = sorted(self.cards + [common], key=lambda card_pos: card_pos.pos)
        run = []
        card_track = {}
        multiplier = 1
        for i in range(len(all_cards)):
            if not(all_cards[i].pos in card_track):
                card_track[all_cards[i].pos] = 0
            card_track[all_cards[i].pos] += 1
            if not run or all_cards[i].pos == run[-1].pos + 1:
                run.append(all_cards[i])
            elif all_cards[i].pos == run[-1].pos:
                continue
            else:
                if len(run) >= 3:
                    break
                else:
                    run = [all_cards[i]]
        if len(run) >=3:
            for card in run:
                multiplier *= card_track[card.pos]
        else:
            return 0
        if verbose:
            print(f"Scores {multiplier} run(s) of {len(run)} cards: {run}!")
        return len(run) * multiplier





    def find_flush(self, common, verbose = True):
        suits_in_hand = [card.suit for card in self.cards]
        if len(set(suits_in_hand)) == 1:
            if common.suit == suits_in_hand[0]:
                if verbose:
                    print("Scores a five-card flush!")
                return 5
            if verbose:
                print("Scores a four-card flush!")
            return 4
        return 0

    def find_flush_crib(self, common):
        all_cards = self.cards + [common]
        all_suits = [card.suit for card in all_cards]
        if len(set(all_suits)) == 1:
            print("Scores a five-card flush!")
            return 5
        return 0
    
    def nobs(self, common, verbose = True):
        for card in self.cards:
            if card.rank == "J" and card.suit == common.suit:
                if verbose:
                    print("Scores 1 point for Nobs!")
                return 1
        return 0
    
    def score_hand(self, common):
        total = 0
        total += self.find_fifteens(common)
        total += self.find_pairs(common)
        total += self.find_runs(common)
        if self.is_crib:
            total += self.find_flush_crib(common)
        else:
            total += self.find_flush(common)
        total += self.nobs(common)
        return total

    def score_hand_silent(self, common):
        total = 0
        total += self.find_fifteens(common, False)
        total += self.find_pairs(common, False)
        total += self.find_runs(common, False)
        if self.is_crib:
            total += self.find_flush_crib(common)
        else:
            total += self.find_flush(common, False)
        total += self.nobs(common, False)
        return total


