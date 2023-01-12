class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        SUITS = ["diamonds", "spades", "hearts", "clubs"]

    def __gt__(self, other):
        if self.value > other.value:
                return True
        if self.value==1 and other.value!=1:
            return True
        if other.value==1 and self.value!=1:
            return True
        elif self.value == other.value:
            if SUITS.index(self.suit) > SUITS.index(other.suit):
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

    SUITS = ["diamonds", "spades", "hearts", "clubs"]
    def __repr__(self):
        """this function returns card details"""
        return f"{self.suit}{self.value}"




