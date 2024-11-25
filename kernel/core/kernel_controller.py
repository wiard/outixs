import json
import os


class KernelController:
    def __init__(
        self,
        config_path="kernel/kernel_config.json",
        nodes_path="kernel/peer_nodes.json",
    ):
        self.config_path = config_path
        self.nodes_path = nodes_path
        self.config = self._load_json(self.config_path)
        self.peer_nodes = self._load_json(self.nodes_path)

    def _load_json(self, path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
            print(f"Loaded data from {path}.")
            return data
        except FileNotFoundError:
            print(f"File not found: {path}. Using default values.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {path}: {e}")
            return {}

    def _save_json(self, data, path):
        try:
            with open(path, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {path}.")
        except Exception as e:
            print(f"Error saving JSON to {path}: {e}")

    def add_peer_node(self, node):
        if node not in self.peer_nodes:
            self.peer_nodes.append(node)
            self._save_json(self.peer_nodes, self.nodes_path)

    def update_config(self, key, value):
        self.config[key] = value
        self._save_json(self.config, self.config_path)

    def execute_task(self, task_name):
        print(f"Executing task: {task_name}")
        # Simulate task execution
        if task_name == "sync_utxo":
            print("Syncing UTXO data...")
        elif task_name == "start_kernel":
            print("Starting kernel...")

    def get_status(self):
        return {"config": self.config, "peer_nodes": self.peer_nodes}
