from player import Player
from deck_of_cards import DeckOfCards


class CardGame:
    def __init__(self, player1_name, player2_name, number_of_cards=26):
        """A constructor of cardgame"""
        if type(player1_name) != str:
            raise TypeError("player name must to be a string")
        if type(player2_name) != str:
            raise TypeError("player name must to be a string")
        if type(number_of_cards) != int:
            raise TypeError("number of cards must to be a int number")
        self.player1 = Player(player1_name, number_of_cards)
        self.player2 = Player(player2_name, number_of_cards)
        self.deck = DeckOfCards()
        self.newgame()

    def newgame(self):
        """This function mixing the deck and deal cards to every player"""
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        print(f"{self.player1.name} has {len(self.player1.deck)} cards:{self.player1.deck}")
        print(f"{self.player2.name} has {len(self.player2.deck)} cards:{self.player2.deck}")

    def get_winner(self):
        """This function return the winner name,if the game is draw the function return NONE"""
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        else:
            return None
