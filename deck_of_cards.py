import random
from random import randint
from card import Card
class DeckOfCards:
    def __init__(self):
        """a constructor of the class"""
        self.cards = []
        suits = ["diamonds", "spades", "hearts", "clubs"]
        for suit in suits:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle_card(self):
        """this function mixing the cards in random way"""
        random.shuffle(self.cards)

    def deal_one(self):
        """the function choose random one card, remove him from the cards and return just him"""
        index = randint(0, len(self.cards) - 1)
        return self.cards.pop(index)

