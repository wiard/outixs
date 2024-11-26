class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, initial_balance):
        if username in self.users:
            return "User already exists."
        self.users[username] = initial_balance
        return "User added successfully"

    def get_user_balance(self, username):
        return self.users.get(username, None)

    def update_user_balance(self, username, amount):
        if username in self.users:
            self.users[username] += amount
            return f"Balance updated for {username}"
        return "User not found"

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return "User removed successfully"
        return "User not found"

