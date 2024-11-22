class MarketplaceItem:
    def __init__(self, item_id, name, description, price, owner=None):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.owner = owner

    def update_price(self, new_price):
        self.price = new_price

    def change_owner(self, new_owner):
        self.owner = new_owner

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "owner": self.owner,
        }

    @staticmethod
    def from_dict(data):
        return MarketplaceItem(
            data["item_id"],
            data["name"],
            data["description"],
            data["price"],
            data["owner"],
        )

