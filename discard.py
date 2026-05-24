def discard_to_crib(players, crib):
    for player in players:
        while len(player.hand.cards) > 4:
            print(player.hand.cards)
            player_choice = input(f"{player.name}, Please choose a card: ")
            if not player_choice:
                print("Invalid card choice")
                continue
            try:
                player_choice = int(player_choice)
            except ValueError:
                print("Invalid card choice")
                continue
            if player_choice < 1 or player_choice > len(player.hand.cards):
                print("Invalid card choice")
                continue
            card_choice = player.discard(player_choice)
            if card_choice:
                crib.cards.append(card_choice)
