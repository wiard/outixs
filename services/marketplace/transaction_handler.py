class TransactionHandler:
    def __init__(self, marketplace_manager):
        self.marketplace_manager = marketplace_manager

    def process_transaction(self, item_name, quantity):
        item = self.marketplace_manager.get_item(item_name)
        if not item:
            return "Item not found"
        if quantity > self.marketplace_manager.get_balance(item_name):  # Check for sufficient funds
            return "Insufficient funds"
        return f"Purchase successful! {quantity} {item_name}(s) purchased"

    def refund_transaction(self, item_name, quantity):
        item = self.marketplace_manager.get_item(item_name)
        if not item:
            return "Item not found"
        return f"Refund successful! {quantity} {item_name}(s) refunded"

    def transaction_status(self, item_name, quantity):
        item = self.marketplace_manager.get_item(item_name)
        if not item:
            return "Item not found"
        return f"Transaction status: {quantity} {item_name}(s) processed"

