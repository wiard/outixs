class KernelController:
    def __init__(self):
        self.config = {"config_key": "value"}
        self.peer_nodes = {}
        self.is_running = False

    def start(self):
        self.is_running = True
        return "Kernel started successfully"

    def stop(self):
        self.is_running = False
        return "Kernel stopped successfully"

    def get_config(self):
        return self.config

    def get_peer_nodes(self):
        return self.peer_nodes

    def invalid_method(self):
        raise AttributeError("Invalid method called")

    def get_status(self):
        return {"config": self.config, "peer_nodes": self.peer_nodes}

if __name__ == "__main__":
    kernel = KernelController()
    print(kernel.start())
    print(kernel.get_config())
    print(kernel.stop())

