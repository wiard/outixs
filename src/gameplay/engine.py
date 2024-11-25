from plugins.loader import PluginLoader

class GameEngine:
    def __init__(self, level_data, players, assets):
        self.level_data = level_data
        self.players = players
        self.assets = assets
        self.game_state = "initialized"
        self.plugins = []
        self.plugin_loader = PluginLoader("plugins/")  # Path to the 
plugins directory

    def initialize_plugins(self):
        """
        Loads and initializes plugins for the game engine.
        """
        print("[GameEngine] Loading plugins...")
        self.plugin_loader.load_plugins()
        self.plugins = self.plugin_loader.plugins

        for plugin in self.plugins:
            plugin.load(self)
            print(f"[GameEngine] Plugin '{plugin.__class__.__name__}' 
initialized.")

    def start(self):
        """
        Starts the game and initializes plugins before entering the game 
loop.
        """
        print("Starting the game...")
        self.initialize_plugins()
        self.game_state = "running"
        self.run_game_loop()

    def run_game_loop(self):
        """
        Runs the main game loop, updating and rendering the game state.
        Plugins are executed at each game tick.
        """
        while self.game_state == "running":
            self.update()
            self.execute_plugins()
            self.render()
            # Simulate a game tick
            user_input = input("Press Enter for next tick or 'q' to quit: 
")
            if user_input.lower() == 'q':
                self.stop()

    def update(self):
        """
        Updates the game state, including players and assets.
        """
        print("Updating game state...")
        for player in self.players:
            player.update()
        for asset in self.assets:
            asset.update()

    def execute_plugins(self):
        """
        Executes plugin logic during each game tick.
        """
        for plugin in self.plugins:
            plugin.execute()
            print(f"[GameEngine] Executed plugin: 
{plugin.__class__.__name__}")

    def render(self):
        """
        Renders the current game state.
        """
        print("Rendering the game world...")
        print(f"Current Level: {self.level_data['name']}")
        for player in self.players:
            print(f"Player {player.name} at position {player.position}")

    def stop(self):
        """
        Stops the game and updates the game state.
        """
        print("Stopping the game...")
        self.game_state = "stopped"

# Example Player and Asset classes for testing
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

# Entry point for testing the GameEngine
if __name__ == "__main__":
    level_data = {"name": "Level 1"}
    players = [Player("Alice", (0, 0)), Player("Bob", (1, 1))]
    assets = [Asset("Tree"), Asset("Rock")]

    engine = GameEngine(level_data, players, assets)
    engine.start()

