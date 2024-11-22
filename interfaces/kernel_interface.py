from abc import ABC, abstractmethod

class KernelInterface(ABC):
    @abstractmethod
    def start_kernel(self):
        """Start the kernel process."""
        pass

    @abstractmethod
    def stop_kernel(self):
        """Stop the kernel process."""
        pass

    @abstractmethod
    def configure_kernel(self, config):
        """Configure kernel settings."""
        pass

