from active_listener import ActiveListener

class ListenerManager:
    def __init__(self):
        self.listeners = []

    def add_listener(self, relay_url, tags):
        listener = ActiveListener(relay_url, tags)
        self.listeners.append(listener)

    def start_listening(self):
        for listener in self.listeners:
            listener.listen()

