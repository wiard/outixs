import unittest
from src.assets.marketplace_items import MarketplaceItem
from src.marketplace.marketplace_manager import MarketplaceManager

class TestMarketplaceManager(unittest.TestCase):
    def setUp(self):
        self.manager = MarketplaceManager()
        self.item1 = MarketplaceItem("item1", "Sword", "A sharp sword", 
100, "user1")
        self.item2 = MarketplaceItem("item2", "Shield", "A sturdy shield", 
150, "user2")

    def test_list_item(self):
        self.manager.list_item(self.item1)
        self.assertEqual(self.manager.get_item("item1").name, "Sword")

    def test_swap_items(self):
        self.manager.list_item(self.item1)
        self.manager.list_item(self.item2)
        self.manager.swap_items("item1", "item2")
        self.assertEqual(self.manager.get_item("item1").owner, "user2")
        self.assertEqual(self.manager.get_item("item2").owner, "user1")

