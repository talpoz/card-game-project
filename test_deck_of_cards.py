from unittest import TestCase
import unittest
from deck_of_cards import DeckOfCards
from card import Card
class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.deck = DeckOfCards()
        self.deck2 = DeckOfCards()
    def test_init(self):
        self.assertEqual(len(self.deck.cards), 52)
    def test_shuffle(self):
        self.deck.cards_shuffle()
        self.assertNotEqual(self.deck.cards, self.deck2.cards)
    def test_deal_one(self):
        self.assertIsInstance(self.deck.deal_one(), Card)
        self.assertEqual(len(self.deck.cards), 51)
    def test_invalid_input_shuffle(self):
        for i in range(52):
            self.deck.deal_one()
        with self.assertRaises(IndexError):
            self.deck.cards_shuffle()
    def test_invalid_input_deal_one(self):
        for i in range(52):
            self.deck.deal_one()
        with self.assertRaises(IndexError):
            self.deck.deal_one()
    def test_invalid_input_deal_one_type(self):
        with self.assertRaises(TypeError):
            self.deck.deal_one("card")

if __name__ == '__main__':
    unittest.main()
