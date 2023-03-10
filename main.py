from cardgame import CardGame
from deck_of_cards import

def get_user_input():
    # get name as an unput from both players
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")

    # create a new object from type CardGame that gets both of the names
    game = CardGame(player1_name, player2_name)
    return game


def play_game(game):
    for i in range(10):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        print(
            f"Round {i + 1}: {game.player1.name} throws {card1.value} of {card1.suit}, {game.player2.name} throws {card2.value} of {card2.suit}")
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

    return game.get_winner()


def declare_the_winner(winner):
    if winner:
        print(f"{winner.name} wins the game with {len(winner.deck)} cards!")
    else:
        print("The game was a tie!")


if __name__ == "__main__":
    game = get_user_input()
    winner = play_game(game)
    declare_the_winner(winner)
