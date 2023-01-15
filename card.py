class Card:
    def __init__(self, value:int, suit:str):
        """A constructor of card"""
        if type(value)!=int:
            raise TypeError("value must to be a int number")
        if type(suit)!=str:
            raise TypeError("suit must to be str from the list of SUITS")
        if suit not in SUITS:
            raise ValueError("suit must to be a string from the list of SUITS")
        if value<=0 or value>13:
            raise ValueError("value must to be a int number between 1-13")
        self.value = value
        self.suit = suit
        self.SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
    def __gt__(self, other):
        """this function comparing value and suit of card to other,if self bigger the function return True,else return False"""
        if type(other.value)!=int:
            raise TypeError("other value must to be a int number")
        if other.value<=0 or other.value>13:
            raise ValueError("other value must to be a int number between 1-13")
        if type(other.suit)!=str:
            raise TypeError("other suit must to be a string from the list of SUITS")
        if other.suit not in self.SUITS:
            raise TypeError("suit must to be a string from list SUITS")
        if self.value==1 and other.value!=1:
            return True
        if other.value==1 and self.value!=1:
            return False
        if self.value > other.value:
            return True
        if self.value == other.value:
            if SUITS.index(self.suit) > SUITS.index(other.suit):
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        """this function comparing between one card and other if they have the same value and suit the function return True,else return False"""
        if type(other)!=Card:
            raise TypeError("other must to be from type of card")
        if type(other.value)!=int:
            raise TypeError("other value must be a int number")
        if other.value<=0 or other.value>13:
            raise ValueError("other value must to be a int number between 1-13")
        if type(other.suit)!=str:
            raise TypeError("suit must to be a string from the list of SUITS")
        if other.suit not in self.SUITS:
            raise ValueError("suit must to be a string from the list of SUITS")
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __repr__(self):
        """this function returns card details"""
        return f"{self.suit}{self.value}"

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]



