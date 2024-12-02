# File: nostr/events/nostr_event_types.py

class NostrEventTypes:
    """
    Enumeration of standard Nostr event types used in the application.
    """
    DIRECT_MESSAGE = 4
    MARKETPLACE_ITEM = 30000
    TRANSACTION_STATUS = 30001
    SYSTEM_NOTIFICATION = 30002
    CUSTOM_EVENT = 30003

class NostrTags:
    """
    Common tags used in Nostr events.
    """
    RECIPIENT = "p"  # Public key of the recipient
    TYPE = "type"    # Type of the event
    ITEM_ID = "item_id"  # ID of a marketplace item
    TRANSACTION_ID = "transaction_id"  # ID of a transaction

