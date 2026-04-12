from deck import Deck, Hand, Card
from card_values import *
from players import Player

def pegging_phase(player1, player2):
    turn = 0
    while player1.hand or player2.hand:
        count = 0
        card_stack = []
        players = [player1, player2]
        while count <= 31:
            current_player = players[turn % 2]
            valid_moves = get_valid_moves(current_player.hand, count)
            if valid_moves:
                print(valid_moves)
                choice = int(input("choose a card from your hand: "))
                move = valid_moves[choice-1]
                current_player.hand.pop(move)
                count += move.value
                card_stack.append(move)
                pegging_score(count, card_stack, players[turn % 2])
                if check_for_go(players, count) == True:
                    current_player.score += 1
                    turn += 1
                    break
                else:
                    continue
            else:
                print("No moves available, but your opponent can play a card!")
            turn += 1


def get_valid_moves(hand, count):
    valid_moves = []
    for card in hand:
        if card.value + count <= 31:
            valid_moves.append(card)
    return valid_moves

def pegging_score(count, card_stack, player):
    pair_count = 1
    run_count = 1
    if count == 15:
        player.score += 2
    for i in range(len(card_stack)):
        if card_stack[-i].rank == card_stack[-i-1].rank:
            pair_count += 1
    if pair_count > 1:
        player.score += 2 * pair_count
    if len(card_stack) >= 3:
        tail = sorted(card_stack[-3:], key=lambda card: card.pos)
        if





def check_for_go(players, count):
    for player in players:
        for card in player.hand:
            if card.value + count <= 31:
                return False
    return True


