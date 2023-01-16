import unittest
from deck_of_cards import DeckOfCards
from card import Card
class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        """A constructor of test case deck of cards"""
        self.deck = DeckOfCards()
        self.deck2 = DeckOfCards()
    def test_init_valid(self):
        """test case of valid init"""
        self.assertEqual(len(self.deck.cards), 52)
        self.assertIn(Card(2,'Hearts'),self.deck.cards)
        self.assertTrue(Card(13,"Hearts"),self.deck.cards)

    def test_init_invalid_with_incorrect_input(self):
        """test case with invalid input """
        with self.assertRaises(TypeError):
            self.deck = DeckOfCards(["hearts", "diamonds"])
        with self.assertRaises(TypeError):
            self.deck = DeckOfCards([1, 2, 3, 4])

    def test_shuffle_valid(self):
        """test case that check the shuffle cards"""
        self.deck.cards_shuffle()
        self.assertNotEqual(self.deck.cards, self.deck2.cards)

    def test_deal_one_valid(self):
        """test case for deal one that pull out one card and remove him from the deck"""
        self.assertIsInstance(self.deck.deal_one(), Card)
        self.assertEqual(len(self.deck.cards), 51)
    def test_deal_one_invalid_empty_deck(self):
        """test case of invalid input empty deck """
        with self.assertRaises(ValueError):
            for i in range(53):
                self.deck.deal_one()



if __name__ == '__main__':
    unittest.main()
