import unittest
from services.marketplace.marketplace_manager import MarketplaceManager

class TestMarketplaceManager(unittest.TestCase):

    def setUp(self):
        self.manager = MarketplaceManager()
        self.item_name = "Golden Sword"
        self.item_price = 100  # Provide the item price
        self.item_data = {"name": self.item_name, "price": self.item_price}  # Include both name and price

    def test_add_item(self):
        result = self.manager.add_item(self.item_name, self.item_price)  # Pass both name and price
        self.assertEqual(result, "Item added successfully")

    def test_remove_item(self):
        self.manager.add_item(self.item_name, self.item_price)
        result = self.manager.remove_item(self.item_name)
        self.assertEqual(result, "Item removed successfully")

    def test_update_item(self):
        self.manager.add_item(self.item_name, self.item_price)
        updated_item_price = 120
        result = self.manager.update_item(self.item_name, updated_item_price)
        self.assertEqual(result, "Item updated successfully")

    def test_item_not_found(self):
        result = self.manager.remove_item("NonExistentItem")
        self.assertEqual(result, "Item not found")

if __name__ == "__main__":
    unittest.main()

