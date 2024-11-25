from abc import ABC, abstractmethod


class MarketplaceInterface(ABC):
    @abstractmethod
    def initialize(self):
        """Initialize the marketplace component."""
        pass

    @abstractmethod
    def process_transaction(self, transaction):
        """Process a transaction."""
        pass

    @abstractmethod
    def sync_with_peers(self):
        """Synchronize marketplace data with peers."""
        pass
