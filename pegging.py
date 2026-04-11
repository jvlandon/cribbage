from deck import Deck, Hand, Card
from card_values import *
from players import Player

def pegging_phase(player1, player2):
    while player1.hand or player2.hand:
        count = 0
        card_stack = []
        players = [player1, player2]
        turn = 0
        while count <= 31:
            current_player = players[turn % 2]
            valid_moves = get_valid_moves(current_player.hand, count)


def get_valid_moves(hand, count):
    valid_moves = []
    for card in hand:
        if card.value + count <= 31:
            valid_moves.append(card)
    return valid_moves

def pegging_score(count, card_stack, player):
    pass

def check_for_go(hand, count):
    pass


