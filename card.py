class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __gt__(self, other_card):
        if self.value > other_card.value:
            return True
        elif self.value == other_card.value:
            if self.suit > other_card.suit:
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



