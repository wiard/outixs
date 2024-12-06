import unittest
from kernel.core.blockchain_sync import BlockchainSync
from unittest.mock import patch

class TestBlockchainSync(unittest.TestCase):
    
    def setUp(self):
        self.api_url = "https://example.com/api"
        self.blockchain_sync = BlockchainSync(self.api_url)

    @patch('requests.get')
    def test_fetch_block_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"block": "data"}

        block_data = self.blockchain_sync.fetch_block_data("block_123")
        self.assertEqual(block_data, {"block": "data"})
        
    @patch('requests.get')
    def test_fetch_block_data_error(self, mock_get):
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            self.blockchain_sync.fetch_block_data("block_123")

if __name__ == '__main__':
    unittest.main()

