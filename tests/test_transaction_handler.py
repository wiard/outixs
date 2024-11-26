import unittest
from services.marketplace.marketplace_manager import MarketplaceManager
from services.marketplace.transaction_handler import TransactionHandler

class TestTransactionHandler(unittest.TestCase):

    def setUp(self):
        self.marketplace_manager = MarketplaceManager()
        self.item_name = "Golden Sword"
        self.item_price = 100  # Provide the item price
        self.marketplace_manager.add_item(self.item_name, self.item_price)  # Pass both name and price
        self.handler = TransactionHandler(self.marketplace_manager)

    def test_process_transaction_success(self):
        result = self.handler.process_transaction(self.item_name, 1)
        self.assertEqual(result, f"Purchase successful! 1 {self.item_name}(s) purchased")

    def test_process_transaction_item_not_found(self):
        result = self.handler.process_transaction("NonExistentItem", 1)
        self.assertEqual(result, "Item not found")

    def test_process_transaction_insufficient_funds(self):
        result = self.handler.process_transaction(self.item_name, 200)
        self.assertEqual(result, "Insufficient funds")

    def test_refund_transaction(self):
        result = self.handler.refund_transaction(self.item_name, 1)
        self.assertEqual(result, f"Refund successful! 1 {self.item_name}(s) refunded")

    def test_transaction_status(self):
        result = self.handler.transaction_status(self.item_name, 1)
        self.assertEqual(result, f"Transaction status: 1 {self.item_name}(s) processed")

if __name__ == "__main__":
    unittest.main()

