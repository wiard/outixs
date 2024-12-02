# File: nostr/relays/relay_health.py

import websocket
import time
import json
from threading import Thread
from lib.logger import Logger

# Initialize logger
logger = Logger("RelayHealth")

class RelayHealth:
    def __init__(self, relay_config_file="nostr/relays/default_relays.json"):
        self.relay_config_file = relay_config_file
        self.relays = self.load_relays()
        self.status = {}

    def load_relays(self):
        """
        Load relays from the configuration file.
        """
        try:
            with open(self.relay_config_file, 'r') as file:
                config = json.load(file)
            logger.info(f"Loaded {len(config['relays'])} relays from configuration.")
            return config['relays']
        except Exception as e:
            logger.error(f"Failed to load relay configuration: {e}")
            return []

    def check_relay(self, relay_url):
        """
        Check the health of a single relay.
        """
        try:
            ws = websocket.create_connection(relay_url, timeout=5)
            ws.send(json.dumps({"type": "ping"}))  # Send a ping to check response
            response = ws.recv()
            ws.close()
            if response:
                logger.debug(f"Relay {relay_url} is healthy.")
                return True
        except Exception as e:
            logger.warning(f"Relay {relay_url} is not reachable: {e}")
        return False

    def update_relay_status(self):
        """
        Update the health status of all relays.
        """
        for relay in self.relays:
            relay_url = relay["url"]
            self.status[relay_url] = self.check_relay(relay_url)
        logger.info(f"Relay status updated: {self.status}")

    def get_healthy_relays(self):
        """
        Get a list of currently healthy relays.
        """
        healthy_relays = [url for url, is_healthy in self.status.items() if is_healthy]
        logger.info(f"Healthy relays: {healthy_relays}")
        return healthy_relays

    def monitor_relays(self, interval=60):
        """
        Continuously monitor relay health at a specified interval.
        """
        logger.info("Starting relay health monitoring...")
        while True:
            self.update_relay_status()
            time.sleep(interval)

    def start_monitoring_thread(self, interval=60):
        """
        Start the relay health monitoring in a separate thread.
        """
        thread = Thread(target=self.monitor_relays, args=(interval,), daemon=True)
        thread.start()
        logger.info("Relay health monitoring thread started.")

