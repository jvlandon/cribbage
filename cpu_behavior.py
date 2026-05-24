from deck import Deck, Card, Hand
from itertools import combinations

def cpu_choose_play(valid_moves, count, card_stack, common):
    candidates = {}
    for card in valid_moves:
        candidates[card] = 0
        if card.value + count == 31:
            return card
        if card.value + count == 15:
            candidates[card] += 1
        if card_stack:
            if card_stack[-1].rank == card.rank:
                candidates[card] += 1
        if is_run(card, card_stack):
            candidates[card] += 1
        if common.rank == card.rank:
            candidates[card] += 1
    best = max(candidates, key=candidates.get)
    return best

def cpu_choose_discard(player, crib):
    candidates = {}
    best_score = 0
    best_combo = None
    fake_deck = Deck()
    fake_deck.shuffle()
    for card in player.hand.cards:
        candidates[card] = 0
    for combo in combinations(player.hand.cards, 4):
        for deal in fake_deck.deck:
            if deal in player.hand.cards:
                continue
            test_hand = Hand([])
            for combo_card in combo:
                test_hand.cards.append(combo_card)
            score = test_hand.score_hand_silent(deal)
            if score > best_score:
                best_score = score
                best_combo = combo
    for card in best_combo:
        candidates[card] += 1
    while len(player.hand.cards) > 4:
        discard = min(candidates, key=candidates.get)
        discard_index = player.hand.cards.index(discard)
        crib.cards.append(discard)
        player.discard(discard_index+1)
        del candidates[discard]


def is_run(candidate, card_stack):
    if len(card_stack) > 1:
        all_cards = [candidate] + card_stack
        run_length = 1
        for i in range(len(all_cards), 2, -1):
            tail = [card.pos for card in all_cards[-i:]]
            if len(set(tail)) == len(tail) and max(tail) - min(tail) == len(tail) - 1:
                run_length += 1
            else:
                break
        if run_length >= 3:
            return True
        return False
    return False