def discard_to_crib(player1, player2, crib):
    while len(player1.hand.cards) > 4:
        player_choice = int(input("Player 1, Please choose a card: "))
        card_choice = player1.discard(player_choice)
        if card_choice:
            crib.cards.append(card_choice)
    while len(player2.hand.cards) > 4:
        player_choice = int(input("Player 2, Please choose a card: "))
        card_choice = player2.discard(player_choice)
        if card_choice:
            crib.cards.append(card_choice)