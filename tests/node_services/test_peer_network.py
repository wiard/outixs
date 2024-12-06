import unittest
from src.peer_network import PeerNetwork


class TestPeerNetwork(unittest.TestCase):
    def setUp(self):
        self.peer_network = PeerNetwork()

    def test_add_peer(self):
        peer_address = "192.168.1.10"
        self.peer_network.add_peer(peer_address)
        self.assertIn(peer_address, self.peer_network.get_peers())

    def test_remove_peer(self):
        peer_address = "192.168.1.10"
        self.peer_network.add_peer(peer_address)
        self.peer_network.remove_peer(peer_address)
        self.assertNotIn(peer_address, self.peer_network.get_peers())

    def test_broadcast_message(self):
        peer_address = "192.168.1.10"
        self.peer_network.add_peer(peer_address)
        response = self.peer_network.broadcast_message("Hello, World!")
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main()
