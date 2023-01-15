from player import Player
from deck_of_cards import DeckOfCards
from card import Card
import unittest

class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player("tal", 26)
            self.player2=Player("amit",26)
            self.deck = DeckOfCards()



        def test_init_valid(self):
            self.assertEqual(self.player.name, "tal")
            self.assertEqual(self.player.number_of_cards, 26)
            self.assertEqual(len(self.player.deck), 26)

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
        def test_set_hand_invalid_type(self):
            with self.assertRaises(TypeError):
                self.player.set_hand(self.player)
        def test_set_hand_invalid_empty_deck(self):
            with self.assertRaises(ValueError):
                self.player.set_hand(self.deck)
                self.player.set_hand(self.deck)
                self.player.set_hand(self.deck)

        def test_get_card_valid(self):
            card = self.player.get_card()
            self.assertIsInstance(card, Card)
            self.assertEqual(len(self.player.deck), 25)
            self.assertTrue(len(self.player.deck), 24)
            self.assertTrue(card,self.player.get_card())


        def test_add_card_valid(self):
            card = self.deck.deal_one()
            self.player.add_card(card)
            self.assertIn(card, self.player.deck)
            self.assertTrue(self.player,DeckOfCards)

        def test_invalid_input_add_card_type_not_int(self):
            with self.assertRaises(TypeError):
                card=Card('aaa','Diamond')
                self.player.add_card(card)
        def  test_invalid_add_card_type_not_str(self):
            with self.assertRaises(TypeError):
                card2=Card(13,12)
                self.player.add_card(card2)
        def test_invalid_add_card_value_out_range(self):
            with self.assertRaises(ValueError):
                card=Card(0,'Spades')
                self.player.add_card(card)
            with self.assertRaises(ValueError):
                card=Card(14,'Spades')
                self.player.add_card(card)



    # if __name__ == '__main__':
    #     unittest.main()

