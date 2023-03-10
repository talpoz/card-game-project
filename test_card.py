from card import Card
import unittest


class TestCard(unittest.TestCase):
    def setUp(self):
        """A constructor of the card test case"""
        self.card = Card(5, "Spades")
        self.card2 = Card(5, "Hearts")
        self.card3 = Card(6, "Hearts")
        self.SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]

    def test_init_valid(self):
        """valid tests for init constructor of class"""
        self.assertEqual(self.card.value, 5)
        self.assertEqual(self.card.suit, "Spades")
        self.assertIn("Hearts", self.SUITS)

    def test_invalid_value_out_range_init(self):
        """test case of invalid input value out of range in init"""
        with self.assertRaises(ValueError):
            card = Card(14, "Spades")
        with self.assertRaises(ValueError):
            card = Card(0, "Spades")
        with self.assertRaises(ValueError):
            card = Card(20, "Spades")
        with self.assertRaises(ValueError):
            card = Card(-1, "Spades")

    def test_invalid_init_not_int_value(self):
        """test invalid value that is not int"""
        with self.assertRaises(TypeError):
            card = Card("five", "Spades")

    def test_invalid_init_not_string_suit(self):
        """test case of invalid input suit in init"""
        with self.assertRaises(TypeError):
            card = Card(5, 6)

    def test_init_invalid_negative_value(self):
        """test case of negative value"""
        with self.assertRaises(ValueError):
            card = Card(-1, "Diamond")

    def test_eq_valid(self):
        """this test case check the valid of comparing one card to other and check if they are the same"""
        self.assertTrue(self.card == self.card)
        self.assertFalse(self.card == self.card2)
        self.assertIn(self.card.suit,self.SUITS)

    def test_eq_invalid_suit_not_int(self):
        """this test case is invalid value not int for eq function """
        with self.assertRaises(TypeError):
            self.card == (5," ")
        with self.assertRaises(TypeError):
            self.card == Card(3,0.5)

    def test_eq_invalid_not_card(self):
        """this test case is invalid card example"""
        with self.assertRaises(TypeError):
            self.card == Card("aaa", "bbb")
        with self.assertRaises(TypeError):
            self.card == Card(14, 15)

    def test_eq_invalid_value_out_range(self):
        """this test case is invalid value out of range"""
        with self.assertRaises(ValueError):
            card = Card(0, "Hearts")
        with self.assertRaises(ValueError):
            card = Card(14, "Spades")

    def test_gt_invalid_suit_not_str(self):
        """this test case is invalid suit that not string"""
        with self.assertRaises(TypeError):
            card = Card(3, 7)

    def test_gt_valid(self):
        """this test case check the valid of comparing one card to other and check if the first are bigger"""
        self.assertTrue(self.card3 > self.card2)
        self.assertFalse(self.card > self.card3)
        self.assertTrue(5, self.card.suit)

    def test_gt_invalid_value_not_int(self):
        """test case of invalid card that not int number"""
        with self.assertRaises(TypeError):
            self.card == Card('',"Hearts")
        with self.assertRaises(TypeError):
            self.card == Card(0.5,"Diamond")

    def test_gt_invalid_value_out_range(self):
        """test case of invalid value out of range"""
        with self.assertRaises(ValueError):
            card = Card(14, "Spades")
        with self.assertRaises(ValueError):
            card = Card(0, "Spades")
        with self.assertRaises(ValueError):
            card = Card(20, "Spades")
        with self.assertRaises(ValueError):
            card = Card(-1, "Spades")

    def test_gt_invalid(self):
        """this test case is invalid input for gt function"""
        with self.assertRaises(TypeError):
            self.card > Card(5,4)


if __name__ == '__main__':
    unittest.main()
