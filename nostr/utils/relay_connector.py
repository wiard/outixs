# File: nostr/utils/relay_connector.py

import websocket
import json
from lib.logger import Logger

logger = Logger("RelayConnector")


class RelayConnector:
    def __init__(self, relays_config_file="nostr/relays/default_relays.json"):
        self.relays = self.load_relays(relays_config_file)

    def load_relays(self, relays_config_file):
        """
        Load relay URLs from a configuration file.
        """
        try:
            with open(relays_config_file, "r") as file:
                relays = json.load(file)["relays"]
            logger.info(f"Loaded {len(relays)} relays.")
            return relays
        except Exception as e:
            logger.error(f"Failed to load relays: {e}")
            return []

    def broadcast_event(self, event):
        """
        Broadcast an event to all configured relays.
        """
        serialized_event = json.dumps(event)
        for relay in self.relays:
            try:
                ws = websocket.create_connection(relay["url"])
                ws.send(serialized_event)
                ws.close()
                logger.debug(f"Event broadcasted to relay {relay['url']}.")
            except Exception as e:
                logger.warning(f"Failed to broadcast to relay {relay['url']}: {e}")

    def query_events(self, filters):
        """
        Query relays for events based on filters.
        """
        events = []
        query_message = json.dumps({"type": "REQ", "filters": filters})
        for relay in self.relays:
            try:
                ws = websocket.create_connection(relay["url"])
                ws.send(query_message)
                while True:
                    response = ws.recv()
                    if not response:
                        break
                    events.append(json.loads(response))
                ws.close()
                logger.debug(f"Queried events from relay {relay['url']}.")
            except Exception as e:
                logger.warning(f"Failed to query relay {relay['url']}: {e}")
        return events

