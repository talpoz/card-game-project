from player import Player
from deck_of_cards import DeckOfCards


class CardGame:
    def __init__(self, player1_name, player2_name, number_of_cards=26):
        self.player1 = Player(player1_name, number_of_cards)
        self.player2 = Player(player2_name, number_of_cards)
        self.deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        print(f"{self.player1.name} has {len(self.player1.deck)} cards")
        print(f"{self.player2.name} has {len(self.player2.deck)} cards")

    def get_winner(self):
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        else:
            return None

    def war_game(player1_name, player2_name, number_of_cards=26):
        game = CardGame(player1_name, player2_name, number_of_cards)
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

        winner = game.get_winner()
        if winner:
            print(f"{winner.name} wins the game with {len(winner.deck)} cards!")
        else:
            print("The game was a tie!")
