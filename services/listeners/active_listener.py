from nostr_client import NostrClient

class ActiveListener:
    def __init__(self, relay_url, tags):
        self.relay_url = relay_url
        self.tags = tags
        self.client = NostrClient(relay_url)

    def listen(self):
        for message in self.client.fetch_messages():
            if any(tag in message["tags"] for tag in self.tags):
                self.process_message(message)

    def process_message(self, message):
        # Add logic to handle the message based on tags
        print(f"Processing message: {message}")
        # Additional processing logic goes here


