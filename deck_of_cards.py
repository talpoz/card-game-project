import random
from card import Card
class DeckOfCards:
    def __init__(self):
        """A constructor of deck of cards"""
        self.cards = []
        for suit in ["Diamonds", "Spades", "Hearts", "Clubs"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
    def cards_shuffle(self):
        """this function mixing the cards in the deck"""
        random.shuffle(self.cards)
    def deal_one(self):
        """this function pull out one random card from the deck remove him from the deck and return the card to the program """
        return self.cards.pop(random.randint(0, len(self.cards)-1))
