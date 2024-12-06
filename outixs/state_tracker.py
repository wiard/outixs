class StateTracker:
    def __init__(self):
        self.states = {}

    def update_state(self, txid, new_state):
        self.states[txid] = new_state

    def get_state(self, txid):
        return self.states.get(txid, "unknown")

