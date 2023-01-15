from player import Player
from deck_of_cards import DeckOfCards
from card import Card
import unittest
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player("tal", 26)
            self.player2=Player("amit",26)
            self.deck = DeckOfCards()

        def test_init_valid(self):
            self.assertEqual(self.player.name, "tal")
            self.assertEqual(self.player.number_of_cards, 26)

        def test_invalid_input_init_name(self):
            with self.assertRaises(TypeError):
                player = Player(123, 10)

        def test_invalid_input_init_number_of_cards(self):
            with self.assertRaises(TypeError):
                player = Player("tal", "twenty six")

        def test_invalid_input_init_number_of_cards_negative_number(self):
            with self.assertRaises(ValueError):
                player = Player("tal", -5)
        def test_set_hand_valid(self):
            self.player.set_hand(self.deck)
            self.player2.set_hand(self.deck)
            self.assertEqual(len(self.player.deck),len(self.player2.deck))
        def test_set_hand_valid_mock(self):
            """this test case checks that the function adds the card from the deck to the player"""
            with patch('deck_of_cards.DeckOfCards.deal_one') as mock_rand:
                mock_rand.return_value = Card(6, "Diamonds")
                player = Player("tal", 26)
                player.set_hand(self.deck)
                self.assertEqual(len(player.deck), 26)
                self.assertEqual(player.deck[0], Card(6, "Diamonds"))

        def test_set_hand_invalid_type(self):
            with self.assertRaises(TypeError):
                self.player.set_hand(self.player)
        def test_set_hand_invalid_empty_deck(self):
            with self.assertRaises(ValueError):
                self.player.set_hand(self.deck)
                self.player.set_hand(self.deck)
                self.player.set_hand(self.deck)

        def test_get_card_valid(self):
            """valid test cases of get card method"""
            player = Player("tal", 26)
            deck = DeckOfCards()
            player.set_hand(deck)
            card = player.get_card()
            self.assertEqual(type(card), Card)
            self.assertEqual(len(player.deck), 25)


        def test_add_card_valid(self):
            """valid test cases of add card method"""
            card = self.deck.deal_one()
            self.player.add_card(card)
            self.assertIn(card, self.player.deck)
            self.assertTrue(self.player,DeckOfCards)

        def test_invalid_input_add_card_type_not_int(self):
            """test case of value as string and not number"""
            with self.assertRaises(TypeError):
                card=Card('aaa','Diamond')
                self.player.add_card(card)
        def  test_invalid_add_card_type_not_str(self):
            """test case of suit as num and not string"""
            with self.assertRaises(TypeError):
                card2=Card(13,12)
                self.player.add_card(card2)
        def test_invalid_add_card_value_out_range(self):
            """test cases of out of range of add card method"""
            with self.assertRaises(ValueError):
                card=Card(0,'Spades')
                self.player.add_card(card)
            with self.assertRaises(ValueError):
                card=Card(14,'Spades')
                self.player.add_card(card)




