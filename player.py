
from deck_of_cards import DeckOfCards
# class Player:
#     def __init__(self, name, num_cards=26):
#         self.name = name
#         self.num_cards = num_cards if 10 <= num_cards <= 26 else 26
#         self.hand = []
#
#     def set_hand(self, deck):
#         for i in range(self.num_cards):
#             self.hand.append(deck.deal_one())
#
#     def get_card(self):
#         return self.hand.pop(randint(0, len(self.hand) - 1))
#
#     def add_card(self, card):
#         self.hand.append(card)
class Player:
    def __init__(self, name, number_of_cards=26):
        if number_of_cards > 26 or number_of_cards < 10:
            number_of_cards = 26
        self.name = name
        self.deck = []
        self.number_of_cards = number_of_cards

    def set_hand(self, deck):
        for _ in range(self.number_of_cards):
            self.deck.append(deck.deal_one())

    def get_card(self):
        return self.deck.pop()

    def add_card(self, card):
        self.deck.append(card)