class CoinSystem:
    def __init__(self):
        self.balances = {}

    def mint(self, user, amount):
        if user not in self.balances:
            self.balances[user] = 0
        self.balances[user] += amount

    def burn(self, user, amount):
        if user in self.balances and self.balances[user] >= amount:
            self.balances[user] -= amount
        else:
            raise ValueError("Insufficient balance to burn")

    def transfer(self, sender, receiver, amount):
        if sender in self.balances and self.balances[sender] >= amount:
            self.balances[sender] -= amount
            if receiver not in self.balances:
                self.balances[receiver] = 0
            self.balances[receiver] += amount
        else:
            raise ValueError("Insufficient balance to transfer")

    def get_balance(self, user):
        return self.balances.get(user, 0)

