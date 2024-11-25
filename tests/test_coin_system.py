import unittest
from src.marketplace.coin_system import CoinSystem


class TestCoinSystem(unittest.TestCase):
    def setUp(self):
        self.coin_system = CoinSystem()

    def test_mint_and_balance(self):
        self.coin_system.mint("user1", 100)
        self.assertEqual(self.coin_system.get_balance("user1"), 100)

    def test_transfer(self):
        self.coin_system.mint("user1", 100)
        self.coin_system.transfer("user1", "user2", 50)
        self.assertEqual(self.coin_system.get_balance("user1"), 50)
        self.assertEqual(self.coin_system.get_balance("user2"), 50)

    def test_burn(self):
        self.coin_system.mint("user1", 100)
        self.coin_system.burn("user1", 50)
        self.assertEqual(self.coin_system.get_balance("user1"), 50)
