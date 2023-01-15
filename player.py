from random import  randint
from deck_of_cards import DeckOfCards
from card import *
class Player:
    def __init__(self, name, number_of_cards=26):
        """A constructor of player"""
        if type(name)!=str:
            raise TypeError("name must to be a string")
        if type(number_of_cards)!=int:
            raise TypeError("number of cards must to be a int number")
        if number_of_cards<=0:
            raise ValueError("number of cards must to be a int and positive number")
        if number_of_cards > 26 or number_of_cards < 10:
            number_of_cards = 26
        self.name = name
        self.deck = []
        self.number_of_cards = number_of_cards

    def set_hand(self, deck):
        """This function getting deck of cards and gives for the player random cards according to number of cards for the game"""
        if type(deck)!=DeckOfCards:
            raise TypeError("deck must to be a type of deck of cards")
        for i in range(self.number_of_cards):
            self.deck.append(deck.deal_one())

    def get_card(self):
        """this function pull out random card from the player deck remove him from the deck and return the card"""
        return self.deck.pop(randint(0, len(self.deck)-1))

    def add_card(self, card):
        """This function add a card to the deck player"""
        if type(card)!=Card:
            raise TypeError("card must to be type of Card class")
        if type(card.value)!=int:
            raise TypeError("card value must to be a int number")
        if card.value<=0 or card.value>13:
            raise ValueError("card value must be between 1-13")
        if type(card.suit)!=str:
            raise TypeError("card suit must to be a string from the list of SUITS")
        self.deck.append(card)