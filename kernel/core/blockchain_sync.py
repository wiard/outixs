import requests

class BlockchainSync:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_block_data(self, block_id):
        response = requests.get(f"{self.api_url}/block/{block_id}")
        if response.status_code != 200:
            raise Exception(f"Failed to fetch block data: {response.status_code}")
        return response.json()

    def get_block_info(self, block_id):
        try:
            block_data = self.fetch_block_data(block_id)
            return block_data
        except Exception as e:
            print(f"Error: {e}")
            return None

