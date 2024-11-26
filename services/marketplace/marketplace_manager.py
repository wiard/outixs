class MarketplaceManager:
    def __init__(self):
        self.items = {}
        self.balances = {}  # Store the quantity of each item

    def add_item(self, item_name, item_price, initial_quantity=100):
        self.items[item_name] = item_price
        self.balances[item_name] = initial_quantity
        return "Item added successfully"

    def get_item(self, item_name):
        return self.items.get(item_name, None)

    def get_balance(self, item_name):
        return self.balances.get(item_name, 0)

    def update_item(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            return "Item updated successfully"
        return "Item not found"

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            return "Item removed successfully"
        return "Item not found"

