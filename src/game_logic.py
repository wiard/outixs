class GameLogic:
    def __init__(self):
        self.game_state = {"players": [], "assets": [], "round": 1}

    def initialize_game(self, players, assets):
        print("Initializing game...")
        self.game_state["players"] = players
        self.game_state["assets"] = assets
        print("Game initialized.")

    def process_action(self, action):
        print(f"Processing action: {action}")
        action_type = action.get("type")
        if action_type == "move":
            self._handle_move(action)
        elif action_type == "trade":
            self._handle_trade(action)
        else:
            print("Unknown action type.")

    def _handle_move(self, action):
        player_id = action.get("player")
        position = action.get("position")
        print(f"Player {player_id} moves to {position}.")

    def _handle_trade(self, action):
        asset_id = action.get("asset")
        from_player = action.get("from_player")
        to_player = action.get("to_player")
        print(f"Asset {asset_id} traded from {from_player} to {to_player}.")

    def end_round(self):
        print("Ending round...")
        self.game_state["round"] += 1
        print(f"Round {self.game_state['round']} started.")

    def get_state(self):
        return self.game_state

