from unittest import TestCase
from player import Player

class TestCardGame(TestCase):
    def setUp(self):
        self.player1=Player("amit",26)
        self.player2=Player("tal",26)

    def test_init_valid(self):
        self.assertTrue("amit",self.player1.name)
        self.assertTrue("tal",self.player2.name)
        self.assertEqual(self.player1.deck,self.player2.deck)
    def test_init_invalid_name_not_str(self):
        with self.assertRaises(TypeError):
            self.player1=Player(2,26)

    def test_newgame(self):
        self.fail()

    def test_get_winner(self):
        self.fail()
