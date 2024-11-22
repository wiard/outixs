import json

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
                print(f"Configuration loaded from {self.config_path}")
        except FileNotFoundError:
            print(f"Configuration file not found: {self.config_path}. Using 
defaults.")
        except json.JSONDecodeError as e:
            print(f"Error decoding configuration: {e}")
            raise

    def get(self, key, default=None):
        return self.config.get(key, default)

    def update(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
                print(f"Configuration saved to {self.config_path}")
        except Exception as e:
            print(f"Error saving configuration: {e}")
            raise

