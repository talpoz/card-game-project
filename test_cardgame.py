from unittest import TestCase,mock
from player import Player
from cardgame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        """A constructor of cardgame test case"""
        self.player1 = Player("Tal", 26)
        self.player2 = Player("Pozniak", 26)
        self.game = CardGame("Tal", "pozniak", 26)

    def test_init_valid(self):
        """this test cases checking the constructor of cardgame class"""
        self.assertTrue("Pozniak", self.player2.name)
        self.assertTrue("tal", self.player1.name)
        self.assertEqual(len(self.player1.deck), len(self.player2.deck))

    def test_init_invalid_name_player_not_str(self):
        """this test cases checking that name include just a string in name"""
        with self.assertRaises(TypeError):
            self.player1 = Player(0, 26)
        with self.assertRaises(TypeError):
            self.player2 = Player(-1, 13)

    def test_init_invalid_number_of_cards_not_int(self):
        """this test cases checking that number of cards is a int number"""
        with self.assertRaises(TypeError):
            self.player1.number_of_cards = Player("Tal", " ")
        with self.assertRaises(TypeError):
            self.player2.number_of_cards = Player("Pozniak",10.5)
    def test_init_invalid_negative_number_of_cards(self):
        """this test case checking that number of cards is not a negative number"""
        with self.assertRaises(ValueError):
            self.player1.number_of_cards=Player("Tal",-2)

    @mock.patch('deck_of_cards.DeckOfCards.cards_shuffle')
    @mock.patch('player.Player.set_hand')
    def test_new_game_valid_mock(self, mock_set_hand, mock_cards_shuffle):
        """this method shuffle the deck and give cards for each player"""
        self.game.newgame()
        mock_cards_shuffle.assert_called_once()
        self.assertEqual(mock_set_hand.call_count, 2)


    def test_get_winner_valid_player1_winner(self):
        """this method return the winner name of player 1"""
        game1 = CardGame("Tal", "Pozniak", 26)
        game1.player2.deck = game1.player2.deck[1:]
        winner = game1.get_winner()
        self.assertEqual(winner, game1.player1)
        self.assertEqual(winner.name, "Tal")

    def test_get_winner_valid_player2_winner(self):
        """this method return the winner name of player 2"""
        game1 = CardGame("Tal", "Pozniak", 26)
        game1.player1.deck = game1.player1.deck[1:]
        winner = game1.get_winner()
        self.assertEqual(winner, game1.player2)
        self.assertEqual(winner.name, "Pozniak")

    def test_get_winner_valid_draw(self):
        """this method return that the game was tie and finish in draw"""
        game1 = CardGame("Tal", "Pozniak", 26)
        winner = game1.get_winner()
        self.assertIsNone(winner)
