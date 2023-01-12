from random import randint
from deck_of_cards import DeckOfCards
class Player:
    def __init__(self, name, num_cards=26):
        self.name = name
        self.num_cards = num_cards if 10 <= num_cards <= 26 else 26
        self.hand = []

    def set_hand(self, deck):
        for i in range(self.num_cards):
            self.hand.append(deck.deal_one())

    def get_card(self):
        return self.hand.pop(randint(0, len(self.hand) - 1))

    def add_card(self, card):
        self.hand.append(card)
