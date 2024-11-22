from abc import ABC, abstractmethod

class NetworkInterface(ABC):
    @abstractmethod
    def connect(self):
        """Establish a connection with peers."""
        pass

    @abstractmethod
    def send_data(self, data):
        """Send data to peers."""
        pass

    @abstractmethod
    def receive_data(self):
        """Receive data from peers."""
        pass

