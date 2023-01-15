from cardgame import *
if __name__ == "__main__":
    number_of_cards=int(input("enter number here:"))
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")
    game = CardGame(player1_name, player2_name,number_of_cards)

    for i in range(10):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        print(f"Round {i+1}: {game.player1.name} throws {card1.value} of {card1.suit}, {game.player2.name} throws {card2.value} of {card2.suit}")
        if card1 > card2:
            game.player1.add_card(card1)
            game.player1.add_card(card2)
            print(f"{game.player1.name} wins this round")
        elif card2 > card1:
            game.player2.add_card(card1)
            game.player2.add_card(card2)
            print(f"{game.player2.name} wins this round")
        else:
            print("This round was a tie!")

    winner = game.get_winner()
    if winner:
        print(f"{winner.name} wins the game with {len(winner.deck)} cards!")
    else:
        print("The game was a tie!")