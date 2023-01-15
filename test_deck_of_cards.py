import unittest
from deck_of_cards import DeckOfCards
from card import Card
class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.deck = DeckOfCards()
        self.deck2 = DeckOfCards()
    def test_init_valid(self):
        self.assertEqual(len(self.deck.cards), 52)
        self.assertIn(Card(2,'Hearts'),self.deck.cards)
        self.assertTrue(Card(13,"Hearts"),self.deck.cards)

    def test_init_with_incorrect_input(self):
        with self.assertRaises(TypeError):
            self.deck = DeckOfCards(["hearts", "diamonds"])
        with self.assertRaises(TypeError):
            self.deck = DeckOfCards([1, 2, 3, 4])

    def test_shuffle_valid(self):
        self.deck.cards_shuffle()
        self.assertNotEqual(self.deck.cards, self.deck2.cards)

    def test_deal_one_valid(self):
        self.assertIsInstance(self.deck.deal_one(), Card)
        self.assertEqual(len(self.deck.cards), 51)
    def test_deal_one_invalid_empty_deck(self):
        with self.assertRaises(ValueError):
            for i in range(53):
                self.deck.deal_one()



if __name__ == '__main__':
    unittest.main()
