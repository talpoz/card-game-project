import random
from card import *


class DeckOfCards:
    def __init__(self):
        SUITS = ["diamonds", "spades", "hearts", "clubs"]
        self.cards = [Card(value, suit) for value in range(1, 14) for suit in SUITS]

    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()