import unittest
from services.marketplace.coin_system import CoinSystem

class TestCoinSystem(unittest.TestCase):

    def setUp(self):
        self.coin_system = CoinSystem()
        self.user = "user1"
        self.coin_system.add_user(self.user, 1000)
        self.coin_system.add_user("user2", 500)  # Ensure user2 is added

    def test_add_user(self):
        result = self.coin_system.add_user("user3", 1000)
        self.assertEqual(result, "User added successfully")

    def test_get_balance(self):
        result = self.coin_system.get_balance(self.user)
        self.assertEqual(result, 1000)

    def test_transfer_coins(self):
        result = self.coin_system.transfer_coins(self.user, "user2", 500)
        self.assertEqual(result, "Transferred 500 coins from user1 to user2")

    def test_transfer_insufficient_funds(self):
        result = self.coin_system.transfer_coins(self.user, "user2", 1500)
        self.assertEqual(result, "Insufficient funds")

    def test_user_not_found(self):
        result = self.coin_system.get_balance("non_existent_user")
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()

