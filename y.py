import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

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

    def __repr__(self):
        """this function returns card details"""
        return f"{self.suit}{self.value}"

SUITS = ["diamonds", "spades", "hearts", "clubs"]

class DeckOfCards:
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(1, 14) for suit in SUITS]

    def cards_shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

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


class CardGame:
    def __init__(self, player1_name, player2_name, number_of_cards=26):
        self.player1 = Player(player1_name, number_of_cards)
        self.player2 = Player(player2_name, number_of_cards)
        self.deck = DeckOfCards()
        self.newgame()

    def newgame(self):
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
        print(f"{self.player1.name} has {len(self.player1.deck)} cards")
        print(f"{self.player2.name} has {len(self.player2.deck)} cards")

    def get_winner(self):
        if len(self.player1.deck) > len(self.player2.deck):
            return self.player1
        elif len(self.player2.deck) > len(self.player1.deck):
            return self.player2
        else:
            return None


def war_game(player1_name, player2_name, number_of_cards=26):
    game = CardGame(player1_name, player2_name, number_of_cards)
    for i in range(10):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        print(
            f"Round {i + 1}: {game.player1.name} throws {card1.value} of {card1.suit}, {game.player2.name} throws {card2.value} of {card2.suit}")
        if card1 > card2:
            game.player1.add_card(card1)
            game.player1.add_card(card2)
            print(f"{game.player1.name} wins this round")
        elif card2 > card1:
            game.player2.add_card(card1)
            game.player2.add_card(card2)
            print(f"{game.player2.name} wins this round")
        else:
            print("This round was a tie!")

    winner = game.get_winner()
    if winner:
        print(f"{winner.name} wins the game with {len(winner.deck)} cards!")
    else:
        print("The game was a tie!")
if __name__ == "__main__":
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")
    game = CardGame(player1_name, player2_name)

    for i in range(10):
        card1 = game.player1.get_card()
        card2 = game.player2.get_card()
        print(f"Round {i+1}: {game.player1.name} throws {card1.value} of {card1.suit}, {game.player2.name} throws {card2.value} of {card2.suit}")
        if card1 > card2:
            game.player1.add_card(card1)
            game.player1.add_card(card2)
            print(f"{game.player1.name} wins this round")
        elif card2 > card1:
            game.player2.add_card(card1)
            game.player2.add_card(card2)
            print(f"{game.player2.name} wins this round")
        else:
            print("This round was a tie!")

    winner = game.get_winner()
    if winner:
        print(f"{winner.name} wins the game with {len(winner.deck)} cards!")
    else:
        print("The game was a tie!")


