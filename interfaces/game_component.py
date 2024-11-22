from abc import ABC, abstractmethod

class GameComponent(ABC):
    @abstractmethod
    def update(self):
        """Update the component's state."""
        pass

    @abstractmethod
    def render(self):
        """Render the component."""
        pass

