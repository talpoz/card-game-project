class Card:
    def __init__(self, value, suit):
        """this function is the constructor of the class"""
        self.value = value
        self.suit = suit

    def __gt__(self, other):
        """This function check if value bigger than other value,if the value is bigger the function returns true,else return false"""
        if self.value > other.value:
            if self.value==1:
                return True
            if self.value == 1 and other.value != 1:
                return True
            if other.value == 1 and self.value != 1:
                return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other_card):
        """this function comparing value and suit of card to other value and suit of card,if they are the same the function return true,else return false"""
        if self.value == other_card.value and self.suit == other_card.suit:
            return True
        else:
            return False
    def __repr__(self):
        """this function returns card details"""
        return f"{self.suit}{self.value}"



