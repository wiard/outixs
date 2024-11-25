class PluginInterface:
    def load(self, engine):
        """Initialize the plugin with the game engine."""
        pass

    def execute(self, *args, **kwargs):
        """Execute plugin-specific logic."""
        pass

