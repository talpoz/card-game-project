import random
from random import randint
from card import Card
class DeckOfCards:
    def __init__(self):
        self.cards = []
        suits = ["diamonds", "spades", "hearts", "clubs"]
        for suit in suits:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle_card(self):
        random.shuffle(self.cards)

    def deal_one(self):
        index = randint(0, len(self.cards) - 1)
        return self.cards.pop(index)

