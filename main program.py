from cardgame import CardGame

player1_name = input("Enter the name of player 1: ")
player2_name = input("Enter the name of player 2: ")
game = CardGame(player1_name, player2_name)

print(f"{player1_name} has {len(game.player1.hand)} cards: {game.player1.hand}")
print(f"{player2_name} has {len(game.player2.hand)} cards: {game.player2.hand}")

for round in range(1, 11):
    card1 = game.player1.get_card()
    card2 = game.player2.get_card()
    print(f"Round {round}: {player1_name} throws {card1}, {player2_name} throws {card2}")
    if card1 > card2:
        print(f"{player1_name} wins this round!")
        game.player1.add_card(card1)
        game.player1.add_card(card2)
    elif card2 > card1:
        print(f"{player2_name} wins this round!")
        game.player2.add_card(card1)
        game.player2.add_card(card2)
    else:
        print("It's a tie!")
    winner = game.get_winner()
    if winner:
        print(f"{winner} has won the game with {len(game.player1.hand)} cards!")
    else:
        print("The game is a draw!")
