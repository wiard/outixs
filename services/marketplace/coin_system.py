class CoinSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username, initial_balance):
        self.users[username] = initial_balance
        return "User added successfully"

    def get_balance(self, username):
        return self.users.get(username, 0)

    def transfer_coins(self, sender, receiver, amount):
        if self.get_balance(sender) < amount:
            return "Insufficient funds"
        if receiver not in self.users:
            return "Receiver not found"
        
        self.users[sender] -= amount
        self.users[receiver] = self.users.get(receiver, 0) + amount
        return f"Transferred {amount} coins from {sender} to {receiver}"

    def user_exists(self, username):
        if username not in self.users:
            return "User not found"
        return True

