from pegging import pegging_phase
from players import Player
from deck import Deck, Hand, Card
from discard import discard_to_crib
from cpu_behavior import *

def main():
    players = [Player("Player 1", False), Player("CPU", True)]
    player1, player2 = players
    deck = Deck()
    turn = 0
    print("Welcome to Cribbage!")
    input("Press Enter to continue...")
    while True:
        for player in players:
            player.hand.cards=[]
            player.dealer = False
        players[turn % 2].dealer = True
        dealer = players[turn % 2]
        print(f"current dealer: {players[turn % 2].name}")
        crib = Hand([], True)
        deck.shuffle()
        deck.deal(players)
        cpu_choose_discard(player2, crib)
        discard_to_crib([player1], crib)
        common = deck.cut_deck()
        print(f"common card: {common}")
        if common.rank == "J":
            dealer.score += 2
            print(f"Nibs! Dealer scores 2 points!")
        pegging_phase(player1, player2, common)
        input("Press Enter to continue...")
        for player in players:
            if not player.dealer:
                print(f"Scoring {player.name}'s hand: {player.hand.cards} {common}")
                points_scored = player.hand.score_hand(common)
                player.score += points_scored
                print(f"Total points scored: {points_scored}")
                input("Press Enter to continue...")
                if player.score >= 121:
                    print(f"Player 1 score: {player1.score}, Player 2 score: {player2.score}")
                    print("Winner! Thanks for playing!")
                    exit()
        print(f"Scoring {dealer.name}'s hand: {dealer.hand.cards} {common}")
        dealer_scored = dealer.hand.score_hand(common)
        dealer.score += dealer_scored
        print(f"Total points scored: {dealer_scored}")
        input("Press Enter to continue...")
        print(f"Scoring crib: {crib.cards} {common}")
        crib_scored = crib.score_hand(common)
        dealer.score += crib_scored
        print(f"Total points scored: {crib_scored}")
        if dealer.score >= 121:
            print(f"Player 1 score: {player1.score}, Player 2 score: {player2.score}")
            print("Winner! Thanks for playing!")
            break
        print(f"Player 1 score: {player1.score}, Player 2 score: {player2.score}")
        turn += 1





if __name__ == '__main__':
    main()