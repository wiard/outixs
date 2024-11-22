import json

class LevelLoader:
    def __init__(self, level_file):
        self.level_file = level_file
        self.level_data = None

    def load_level(self):
        print(f"Loading level from {self.level_file}...")
        try:
            with open(self.level_file, 'r') as file:
                self.level_data = json.load(file)
                print("Level loaded successfully.")
        except FileNotFoundError:
            print(f"Error: Level file {self.level_file} not found.")
        except json.JSONDecodeError:
            print("Error: Failed to parse level file.")

        return self.level_data

