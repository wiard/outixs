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
            # Simulate a game tick
            input("Press Enter for next tick or 'q' to quit: ")
            if input() == 'q':
                self.stop()

    def update(self):
        print("Updating game state...")
        for player in self.players:
            player.update()
        for asset in self.assets:
            asset.update()

    def render(self):
        print("Rendering the game world...")
        print(f"Current Level: {self.level_data['name']}")
        for player in self.players:
            print(f"Player {player.name} at position {player.position}")

    def stop(self):
        print("Stopping the game...")
        self.game_state = "stopped"

