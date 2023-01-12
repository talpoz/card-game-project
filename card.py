class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __gt__(self, other):
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
        if self.value == other_card.value and self.suit == other_card.suit:
            return True
        else:
            return False



