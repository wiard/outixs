import os
import importlib.util
from interfaces.plugin_interface import PluginInterface

class PluginLoader:
    def __init__(self, plugins_path):
        self.plugins_path = plugins_path
        self.plugins = []

    def load_plugins(self):
        for file in os.listdir(self.plugins_path):
            if file.endswith(".py") and file != "loader.py":
                plugin_path = os.path.join(self.plugins_path, file)
                spec = importlib.util.spec_from_file_location(file[:-3], 
plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type) and issubclass(obj, 
PluginInterface) and obj != PluginInterface:
                        self.plugins.append(obj())

    def initialize_plugins(self, engine):
        for plugin in self.plugins:
            plugin.load(engine)

