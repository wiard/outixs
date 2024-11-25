import json
import socket

class PeerSync:
    def __init__(self, peer_list):
        self.peer_list = peer_list

    def sync_data(self, data):
        print("Starting data synchronization with peers...")
        for peer in self.peer_list:
            self.send_data(peer, data)

    def send_data(self, peer, data):
        try:
            print(f"Connecting to peer {peer['address']} on port 
{peer['port']}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((peer['address'], peer['port']))
                s.sendall(json.dumps(data).encode('utf-8'))
                print(f"Data sent to peer {peer['address']}.")
        except Exception as e:
            print(f"Failed to send data to peer {peer['address']}: {e}")

    def receive_data(self, port):
        print(f"Listening for data on port {port}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    received_data = json.loads(data.decode('utf-8'))
                    print(f"Data received: {received_data}")
                    return received_data

