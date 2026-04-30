from deck import Deck, Hand, Card
from card_values import *
from players import Player

def pegging_phase(player1, player2):
    turn = 0
    used_cards = []
    last_player = None
    players = [player1, player2]
    while get_valid_moves(player1, used_cards) and get_valid_moves(player2, used_cards):
        count = 0
        card_stack = []
        while count <= 31:
            current_player = players[turn % 2]
            valid_moves = get_valid_moves(current_player, used_cards, count)
            if valid_moves:
                print(valid_moves)
                choice = int(input("choose a card from your hand: "))
                move = valid_moves[choice-1]
                count += move.value
                print(f"Count is at {count}")
                used_cards.append(move)
                card_stack.append(move)
                pegging_score(count, card_stack, players[turn % 2])
                last_player = current_player
                turn += 1
                continue
            else:
                if count == 31:
                    break
                elif check_for_go(players, used_cards, count):
                    print(f"Scores 1 point for making a go!")
                    last_player.score += 1
                    turn += 1
                    break
                else:
                    print("No moves available, but your opponent can play a card!")
                    turn += 1
                    continue
    print(used_cards)
    print("Pegging phase complete! moving to scoring phase...")

def get_valid_moves(player, used_cards, count=0):
    valid_moves = []
    for card in player.hand.cards:
        if card.value + count <= 31 and card not in used_cards:
            valid_moves.append(card)
    return valid_moves

def check_for_go(players, used_cards, count):
    for player in players:
        if get_valid_moves(player, used_cards, count):
            return False
    return True

def pegging_score(count, card_stack, player):
    pair_count = 1
    if count == 15:
        player.score += 2
        print("Scores 2 points for making 15!")
    if count == 31:
        player.score += 2
        print("Scores 2 points for making 31!")
    for i in range(len(card_stack)-1, 0, -1):
        if card_stack[i].rank == card_stack[i-1].rank:
            pair_count += 1
        else:
            break
    if pair_count > 1:
        if pair_count == 4:
            player.score += 12
            print("Scores 12 points for making 4 of a kind!")
        elif pair_count == 3:
            player.score += 6
            print("Scores 6 points for making 3 of a kind!")
        else:
            player.score += 2
            print("Scores 2 points for making a pair!")
    if len(card_stack) >= 3:
        for i in range(len(card_stack), 2, -1):
            tail = [card.pos for card in card_stack[-i:]]
            if len(set(tail)) != len(tail):
                continue
            if max(tail) - min(tail) == len(tail) - 1:
                player.score += len(tail)
                print(f"Scores {len(tail)} points for making a run!")
                break
    return








