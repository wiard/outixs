import unittest
from src.assets.marketplace_items import MarketplaceItem
from src.marketplace.marketplace_manager import MarketplaceManager
from src.marketplace.coin_system import CoinSystem
from src.marketplace.transaction_handler import TransactionHandler

class TestTransactionHandler(unittest.TestCase):
    def setUp(self):
        self.coin_system = CoinSystem()
        self.manager = MarketplaceManager()
        self.handler = TransactionHandler(self.coin_system, self.manager)
        self.item = MarketplaceItem("item1", "Sword", "A sharp sword", 
100, "user1")
        self.manager.list_item(self.item)

    def test_execute_purchase(self):
        self.coin_system.mint("user2", 150)
        result = self.handler.execute_purchase("user2", "item1")
        self.assertEqual(result, "Purchase successful! user2 now owns 
Sword")
        self.assertEqual(self.item.owner, "user2")

