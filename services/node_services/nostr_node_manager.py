from nostr.relay_manager import RelayManager
from nostr.event import Event

class NostrNodeManager:
    def __init__(self, relays):
        self.relay_manager = RelayManager()
        for relay in relays:
            self.relay_manager.add_relay(relay)

    def connect(self):
        self.relay_manager.open_connections()

    def publish_event(self, private_key, content):
        event = Event(private_key=private_key, content=content)
        self.relay_manager.publish(event)

    def disconnect(self):
        self.relay_manager.close_connections()

