class MarketplaceManager:
    def __init__(self):
        self.items = {}

    def list_item(self, item):
        if item.item_id in self.items:
            raise ValueError("Item already listed")
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise ValueError("Item not found")

    def get_item(self, item_id):
        return self.items.get(item_id)

    def swap_items(self, item_id_1, item_id_2):
        if item_id_1 not in self.items or item_id_2 not in self.items:
            raise ValueError("One or both items not found")
        item_1 = self.items[item_id_1]
        item_2 = self.items[item_id_2]
        item_1_owner, item_2_owner = item_1.owner, item_2.owner
        item_1.change_owner(item_2_owner)
        item_2.change_owner(item_1_owner)
