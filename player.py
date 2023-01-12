class Player:
    def __init__(self, name, number_of_cards=26):
        if number_of_cards > 26 or number_of_cards < 10:
            number_of_cards = 26
        self.name = name
        self.deck = []
        self.number_of_cards = number_of_cards

    def set_hand(self, deck):
        for _ in range(self.number_of_cards):
            self.deck.append(deck.deal_one())

    def get_card(self):
        return self.deck.pop()

    def add_card(self, card):
        self.deck.append(card)