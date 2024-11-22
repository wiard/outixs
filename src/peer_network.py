from networking.peer_sync import PeerSync

class PeerNetwork:
    def __init__(self, node_id, peer_list):
        self.node_id = node_id
        self.peer_list = peer_list
        self.peer_sync = PeerSync(self.peer_list)

    def add_peer(self, peer):
        if peer not in self.peer_list:
            self.peer_list.append(peer)
            print(f"Peer {peer['address']} added to the network.")

    def remove_peer(self, peer):
        if peer in self.peer_list:
            self.peer_list.remove(peer)
            print(f"Peer {peer['address']} removed from the network.")

    def broadcast_data(self, data):
        print("Broadcasting data to all peers...")
        self.peer_sync.sync_data(data)

    def listen_for_data(self, port):
        print(f"Node {self.node_id} listening for data on port {port}...")
        received_data = self.peer_sync.receive_data(port)
        if received_data:
            print("Processing received data...")
            self.process_received_data(received_data)

    def process_received_data(self, data):
        print(f"Data received at node {self.node_id}: {data}")
        # Custom processing logic can be added here

