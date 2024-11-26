class PeerSync:
    
    def __init__(self, peer_list):
        self.peer_list = peer_list
    
    def connect_to_peer(self, peer):
        if peer in self.peer_list:
            return f"Connected to {peer}"
        return f"Peer {peer} not found"
    
    def disconnect_peer(self, peer):
        if peer in self.peer_list:
            return f"Disconnected from {peer}"
        return f"Peer {peer} not found"
    
    def sync_data(self, peer, data):
        if peer in self.peer_list:
            return f"Data synced with {peer}"
        return f"Sync timeout with {peer}"

