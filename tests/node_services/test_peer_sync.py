import unittest
from services.networking.peer_sync import PeerSync

class TestPeerSync(unittest.TestCase):

    def setUp(self):
        self.peer_list = ["peer1", "peer2", "peer3"]
        self.peer_sync = PeerSync(self.peer_list)

    def test_connect_to_peer(self):
        result = self.peer_sync.connect_to_peer("peer1")
        self.assertEqual(result, "Connected to peer1")

    def test_disconnect_peer(self):
        result = self.peer_sync.disconnect_peer("peer1")
        self.assertEqual(result, "Disconnected from peer1")

    def test_sync_data(self):
        result = self.peer_sync.sync_data("peer1", "some_data")
        self.assertEqual(result, "Data synced with peer1")

    def test_sync_timeout(self):
        result = self.peer_sync.sync_data("peer2", "some_data")
        self.assertEqual(result, "Data synced with peer2")

    def test_sync_peer_not_found(self):
        result = self.peer_sync.sync_data("peer4", "some_data")
        self.assertEqual(result, "Sync timeout with peer4")

if __name__ == "__main__":
    unittest.main()

