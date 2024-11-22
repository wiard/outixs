import unittest
from src.core.utxo_manager import UTXOManager

class TestUTXOManager(unittest.TestCase):
    def setUp(self):
        self.utxo_manager = UTXOManager()

    def test_add_utxo(self):
        utxo = {"txid": "abc123", "value": 1000, "address": "1BitcoinAddress"}
        self.utxo_manager.add_utxo(utxo)
        self.assertIn(utxo, self.utxo_manager.get_all_utxos())

    def test_remove_utxo(self):
        utxo = {"txid": "abc123", "value": 1000, "address": "1BitcoinAddress"}
        self.utxo_manager.add_utxo(utxo)
        self.utxo_manager.remove_utxo(utxo["txid"])
        self.assertNotIn(utxo, self.utxo_manager.get_all_utxos())

    def test_find_utxo_by_address(self):
        utxo = {"txid": "abc123", "value": 1000, "address": "1BitcoinAddress"}
        self.utxo_manager.add_utxo(utxo)
        result = self.utxo_manager.find_utxo_by_address("1BitcoinAddress")
        self.assertEqual(result, [utxo])

if __name__ == "__main__":
    unittest.main()

