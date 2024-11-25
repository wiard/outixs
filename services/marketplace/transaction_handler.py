class TransactionHandler:
    def __init__(self, coin_system, marketplace_manager):
        self.coin_system = coin_system
        self.marketplace_manager = marketplace_manager

    def execute_purchase(self, buyer, item_id):
        item = self.marketplace_manager.get_item(item_id)
        if not item:
            raise ValueError("Item not found")
        if self.coin_system.get_balance(buyer) < item.price:
            raise ValueError("Insufficient funds")
        self.coin_system.transfer(buyer, item.owner, item.price)
        item.change_owner(buyer)
        return f"Purchase successful! {buyer} now owns {item.name}"

    def execute_swap(self, item_id_1, item_id_2):
        self.marketplace_manager.swap_items(item_id_1, item_id_2)
        return f"Swap successful! Items {item_id_1} and {item_id_2} 
exchanged ownership"

