class GameEngine:
    def __init__(self, level_data, players, assets):
        self.level_data = level_data
        self.players = players
        self.assets = assets
        self.game_state = "initialized"

    def start(self):
        print("Starting the game...")
        self.game_state = "running"
        self.run_game_loop()

    def run_game_loop(self):
        while self.game_state == "running":
            self.update()
            self.render()
            user_input = input("Press Enter for the next tick or 'q' to quit: ").strip()
            if user_input.lower() == "q":
                self.stop()

    def update(self):
        print("\nUpdating game state...")
        for player in self.players:
            player.update()
        for asset in self.assets:
            asset.update()

    def render(self):
        print("\nRendering the game world...")
        print(f"Current Level: {self.level_data['name']}")
        for player in self.players:
            print(f"Player {player.name} at position {player.position}")
        for asset in self.assets:
            print(f"Asset: {asset.name}")

    def stop(self):
        print("Stopping the game...")
        self.game_state = "stopped"


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def update(self):
        print(f"[Player {self.name}] Moving to a new position...")


class Asset:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"[Asset {self.name}] Updating status...")


if __name__ == "__main__":
    level_data = {"name": "Level 1"}
    players = [Player("Alice", (0, 0)), Player("Bob", (1, 1))]
    assets = [Asset("Tree"), Asset("Rock")]

    engine = GameEngine(level_data, players, assets)
    engine.start()
