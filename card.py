class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
<<<<<<< HEAD
        self.SUITS = ["diamonds", "spades", "hearts", "clubs"]
=======
        SUITS = ["diamonds", "spades", "hearts", "clubs"]
>>>>>>> origin/main

    def __gt__(self, other):
        if self.value > other.value:
                return True
        if self.value==1 and other.value!=1:
            return True
        if other.value==1 and self.value!=1:
            return True
        elif self.value == other.value:
<<<<<<< HEAD
            if self.SUITS.index(self.suit) > self.SUITS.index(other.suit):
=======
            if SUITS.index(self.suit) > SUITS.index(other.suit):
>>>>>>> origin/main
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

<<<<<<< HEAD
=======
    SUITS = ["diamonds", "spades", "hearts", "clubs"]
>>>>>>> origin/main
    def __repr__(self):
        """this function returns card details"""
        return f"{self.suit}{self.value}"




