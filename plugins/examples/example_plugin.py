from interfaces.plugin_interface import PluginInterface

class ExamplePlugin(PluginInterface):
    def load(self, engine):
        print("ExamplePlugin loaded into the engine.")

    def execute(self, *args, **kwargs):
        print("ExamplePlugin executed.")

