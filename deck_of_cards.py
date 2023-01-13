import random
from random import randint
from card import Card
class DeckOfCards:
    def __init__(self):
        """a constructor of the deck_of_cards"""
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
import random
from card import *
<<<<<<< HEAD


=======
>>>>>>> origin/main
class DeckOfCards:
    def __init__(self):
        SUITS = ["diamonds", "spades", "hearts", "clubs"]
        self.cards = [Card(value, suit) for value in range(1, 14) for suit in SUITS]
<<<<<<< HEAD

=======
>>>>>>> origin/main
    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
<<<<<<< HEAD
        return self.cards.pop()
=======
        return self.cards.pop()
>>>>>>> origin/main
