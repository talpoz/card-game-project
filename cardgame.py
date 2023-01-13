from deck_of_cards import *
class CardGame:
    def __init__(self, player1_name, player2_name, num_cards=26):
        self.deck = DeckOfCards()
        self.player1 = Player(player1_name, num_cards)
        self.player2 = Player(player2_name, num_cards)
        self.newgame()

    def newgame(self):
        self.deck.shuffle_card()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    def get_winner(self):
        if len(self.player1.hand) > len(self.player2.hand):
            return self.player1.name
        elif len(self.player1.hand) < len(self.player2.hand):
            return self.player2.name
        else:
            return None
