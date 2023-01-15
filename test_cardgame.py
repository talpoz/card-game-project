from unittest import TestCase
from player import Player
from cardgame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        self.player1=Player("amit",26)
        self.player2=Player("tal",26)


    def test_init_valid(self):
        self.assertTrue("amit",self.player1.name)
        self.assertTrue("tal",self.player2.name)
        self.assertEqual(self.player1.number_of_cards,self.player2.number_of_cards)

    def test_init_invalid_name_not_str(self):
        with self.assertRaises(TypeError):
            self.player1=Player(2,26)

    def test_newgame(self):
        self.fail()

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




