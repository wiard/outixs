import json

class MarketplaceManager:
    def __init__(self, storage_file="marketplace_data.json"):
        self.storage_file = storage_file
        self.items = self.load_items()

    def load_items(self):
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_items(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.items, f)

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price
        self.save_items()
        return "Item added successfully"

    def get_item(self, item_name):
        return self.items.get(item_name, None)

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            self.save_items()
            return "Item removed successfully"
        return "Item not found"

    def update_item(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            self.save_items()
            return "Item updated successfully"
        return "Item not found"

