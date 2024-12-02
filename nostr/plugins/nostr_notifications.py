# File: nostr/plugins/nostr_notifications.py

import json
from nostr.utils.key_manager import sign_event
from nostr.events.event_manager import EventManager
from nostr.relays.relay_connector import RelayConnector
from lib.logger import Logger

# Initialize logger
logger = Logger("NostrNotifications")


class NostrNotifications:
    def __init__(self, relays_config, private_key, public_key):
        self.relay_connector = RelayConnector(relays_config)
        self.event_manager = EventManager()
        self.private_key = private_key
        self.public_key = public_key

    def send_notification(self, recipient_pubkey, notification_type, message, extra_tags=None):
        """
        Send a notification to a specific user via Nostr.
        
        Args:
            recipient_pubkey (str): Public key of the recipient.
            notification_type (str): Type of notification (e.g., "transaction", "system", "custom").
            message (str): Content of the notification.
            extra_tags (list): Optional additional tags for the event.
        """
        logger.info(f"Sending notification to {recipient_pubkey}: {notification_type}")

        tags = [["p", recipient_pubkey], ["type", notification_type]]
        if extra_tags:
            tags.extend(extra_tags)

        event = {
            "pubkey": self.public_key,
            "created_at": self.event_manager.current_timestamp(),
            "kind": 4,  # Direct message event
            "tags": tags,
            "content": message,
        }
        event["id"] = self.event_manager.calculate_event_id(event)
        event["sig"] = sign_event(event,

