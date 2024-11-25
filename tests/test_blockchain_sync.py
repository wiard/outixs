import unittest
from unittest.mock import patch, Mock
from kernel.core.blockchain_sync import BlockchainSync

class TestBlockchainSync(unittest.TestCase):
    
    @patch('requests.get')
    def test_fetch_block_data(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"block_id": 1, "data": "sample data"}
        
        mock_get.return_value = mock_response
        
        blockchain_sync = BlockchainSync(api_url="http://mock-api-url")
        block_data = blockchain_sync.fetch_block_data(block_id=1)
        
        self.assertIsNotNone(block_data)
        self.assertEqual(block_data['block_id'], 1)
        self.assertEqual(block_data['data'], "sample data")

    @patch('requests.get')
    def test_fetch_block_data_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {}
        
        mock_get.return_value = mock_response
        
        blockchain_sync = BlockchainSync(api_url="http://mock-api-url")
        
        with self.assertRaises(Exception) as context:
            blockchain_sync.fetch_block_data(block_id=999)
        
        self.assertTrue('Failed to fetch block data' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

