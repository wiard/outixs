import socket
import threading

class PeerSync:
    def __init__(self, peer_list):
        self.peer_list = peer_list

    def connect_to_peer(self, peer):
        try:
            print(f"Connecting to peer {peer['address']} on port {peer['port']}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((peer['address'], peer['port']))
            print(f"Connected to peer {peer['address']} on port {peer['port']}")
            s.close()
        except Exception as e:
            print(f"Failed to connect to peer {peer['address']} on port {peer['port']}: {e}")

    def sync_with_peers(self):
        threads = []
        for peer in self.peer_list:
            thread = threading.Thread(target=self.connect_to_peer, args=(peer,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

