from unittest import TestCase
from player import Player
from cardgame import CardGame
from unittest.mock import patch


class TestCardGame(TestCase):
    def setUp(self):
        self.player1 = Player("amit", 26)
        self.player2 = Player("tal", 26)
        self.game = CardGame("amit", "tal", 26)

    def test_init_valid(self):
        self.assertTrue("amit", self.player1.name)
        self.assertTrue("tal", self.player2.name)
        self.assertEqual(len(self.player1.deck), len(self.player2.deck))

    def test_init_invalid_name_player_not_str(self):
        with self.assertRaises(TypeError):
            self.player1 = Player(2, 26)
        with self.assertRaises(TypeError):
            self.player2 = Player(4, 13)

    def test_init_invalid_number_of_cards_not_int(self):
        with self.assertRaises(TypeError):
            self.player1.number_of_cards = Player("aaa", "Diamond")
        with self.assertRaises(TypeError):
            self.player1.number_of_cards = Player(10.5, "Hearts")

    @patch('deck_of_cards.DeckOfCards.cards_shuffle')
    @patch('player.Player.set_hand')
    def test_new_game_valid_mock(self, mock_set_hand, mock_cards_shuffle):
        self.game.newgame()
        mock_cards_shuffle.assert_called_once()
        self.assertEqual(mock_set_hand.call_count, 2)

    def test_get_winner_valid_player1_winner(self):
        game1 = CardGame("tal", "amit", 26)
        game1.player2.deck = game1.player2.deck[1:]
        winner = game1.get_winner()
        self.assertEqual(winner, game1.player1)
        self.assertEqual(winner.name, "tal")

    def test_get_winner_valid_player2_winner(self):
        game1 = CardGame("tal", "amit", 26)
        game1.player1.deck = game1.player1.deck[1:]
        winner = game1.get_winner()
        self.assertEqual(winner, game1.player2)
        self.assertEqual(winner.name, "amit")

    def test_get_winner_valid_draw(self):
        game1 = CardGame("tal", "amit", 26)
        winner = game1.get_winner()
        self.assertIsNone(winner)
