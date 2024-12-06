class RelayDiscovery:
    def __init__(self, relays):
        self.relays = relays

    def discover(self, tags):
        results = []
        for relay in self.relays:
            if any(tag in relay["tags"] for tag in tags):
                results.append(relay)
        return results

