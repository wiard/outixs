# File: nostr/plugins/nostr_marketplace.py

import json
from nostr.utils.key_manager import generate_keys, sign_event
from nostr.relays.relay_connector import RelayConnector
from nostr.events.event_manager import EventManager
from services.marketplace.marketplace_manager import MarketplaceManager
from lib.logger import Logger

# Initialize logger
logger = Logger("NostrMarketplace")

class NostrMarketplace:
    def __init__(self, relays_config, marketplace_config):
        self.relay_connector = RelayConnector(relays_config)
        self.event_manager = EventManager()
        self.marketplace = MarketplaceManager(marketplace_config)
        self.private_key, self.public_key = generate_keys()

    def publish_item(self, item_data):
        """
        Publish a marketplace item as a Nostr event.
        """
        logger.info(f"Publishing item: {item_data}")
        event = {
            "pubkey": self.public_key,
            "created_at": self.event_manager.current_timestamp(),
            "kind": 30000,  # Custom event type for marketplace
            "tags": [["type", "marketplace_item"]],
            "content": json.dumps(item_data),
        }
        event["id"] = self.event_manager.calculate_event_id(event)
        event["sig"] = sign_event(event, self.private_key)
        
        self.relay_connector.broadcast_event(event)
        logger.info("Item published to Nostr relays successfully.")
        return event

    def fetch_marketplace_items(self):
        """
        Fetch marketplace items from Nostr relays.
        """
        logger.info("Fetching marketplace items from relays.")
        events = self.relay_connector.query_events(
            filters={"kind": 30000, "tags": [["type", "marketplace_item"]]}
        )
        items = [json.loads(event["content"]) for event in events]
        logger.info(f"Retrieved {len(items)} items.")
        return items

    def process_transaction(self, item_id, buyer_pubkey, payment_hash):
        """
        Process a transaction tied to a Nostr event and Lightning payment.
        """
        logger.info(f"Processing transaction for item {item_id}")
        item = self.marketplace.get_item(item_id)
        if not item:
            logger.error(f"Item {item_id} not found!")
            return False

        # Validate payment
        if not self.marketplace.validate_payment(payment_hash, item["price"]):
            logger.error("Invalid or incomplete payment!")
            return False

        # Finalize transaction and notify buyer and seller
        self.marketplace.mark_item_as_sold(item_id)
        notification_event = {
            "pubkey": self.public_key,
            "created_at": self.event_manager.current_timestamp(),
            "kind": 4,  # Direct message
            "tags": [["p", buyer_pubkey], ["type", "transaction_completed"]],
            "content": f"Transaction complete for item {item_id}. Thank you!",
        }
        notification_event["id"] = self.event_manager.calculate_event_id(notification_event)
        notification_event["sig"] = sign_event(notification_event, self.private_key)
        self.relay_connector.broadcast_event(notification_event)
        logger.info("Transaction completed and notifications sent.")
        return True

