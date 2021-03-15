import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Clubs", 4)

    def test_card_has_suit(self):
        self.assertEqual("Spades", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.card1.value)

    def test_can_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_can_check_not_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    def test_can_get_highest_card(self):    
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_can_get_cards_total(self):
        self.cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 5", self.card_game.cards_total(self.cards))