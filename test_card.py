from card import Card
import unittest
class TestCard(unittest.TestCase):
    def setUp(self):
        """A constructor of the card test case"""
        self.card = Card(5, "Spades")
        self.card2 = Card(5, "Hearts")
        self.card3 = Card(6, "Hearts")
        self.SUITS=["Diamonds", "Spades", "Hearts", "Clubs"]
        print("setUP")
    def test_init_valid(self):
        """valid tests for init constructor of class"""
        self.assertEqual(self.card.value, 5)
        self.assertEqual(self.card.suit, "Spades")
        self.assertIn("Hearts",self.SUITS)

    def test_invalid_value_init(self):
        """test case of invalid input value in init"""
        with self.assertRaises(ValueError):
            card = Card(15, "Spades")
        with self.assertRaises(TypeError):
            card = Card("five", "Spades")
    def test_invalid_suit_init(self):
        """test case of invalid input suit in init"""
        with self.assertRaises(TypeError):
            card=Card(0,8)

    def test_eq_valid(self):
        """this test case check the valid of comparing one card to other and check if they are the same"""
        self.assertTrue(self.card==self.card)

    def test_eq_invalid(self):
        """this test case is invalid input for eq function """
        self.assertFalse(self.card==self.card2)

    def test_gt_valid(self):
        """this test case check the valid of comparing one card to other and check if the first are bigger"""
        self.assertTrue(self.card3>self.card2)

    def test_gt_invalid(self):
        """this test case is invalid input for gt function"""
        self.assertFalse(self.card>self.card3)



if __name__ == '__main__':
    unittest.main()
