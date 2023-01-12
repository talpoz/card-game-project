from random import randint
#"""A class that includeed the name of the player,the number of the card and the number of the round"""
class Player:
    def __init__(self, name, num_cards=26):
        self.name = name
        self.num_cards = num_cards if 10 <= num_cards <= 26 else 26
        self.hand = []
#"""a function that accepts a shell pack and deals 26 from it"""
    def set_hand(self, deck):
        for i in range(self.num_cards):
            self.hand.append(deck.deal_one())
#"""a function that draws a random card from the player deck"""
    def get_card(self):
        return self.hand.pop(randint(0, len(self.hand) - 1))
#"""a function that accepet a card and adds it from the player's deck of cards"""
    def add_card(self, card):
        self.hand.append(card)
