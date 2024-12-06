import unittest
import sqlite3
from kernel.core.utxo_manager import UTXOManager

class TestUTXOManager(unittest.TestCase):

    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.manager = UTXOManager(":memory:")
        
        # Create the 'utxos' table in the setup method
        with self.manager.conn:
            self.manager.cur.execute("""
                CREATE TABLE utxos (
                    txid TEXT PRIMARY KEY,
                    output_index INTEGER,
                    amount INTEGER
                )
            """)
        
        self.txid = "5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052"
        self.output_index = 0
        self.amount = 1000

    def test_add_utxo(self):
        result = self.manager.add_utxo(self.txid, self.output_index, self.amount)
        self.assertEqual(result, "UTXO added successfully")

    def test_fetch_utxo(self):
        self.manager.add_utxo(self.txid, self.output_index, self.amount)
        result = self.manager.fetch_utxo(self.txid, self.output_index)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], self.txid)

    def test_delete_utxo(self):
        self.manager.add_utxo(self.txid, self.output_index, self.amount)
        result = self.manager.delete_utxo(self.txid, self.output_index)
        self.assertEqual(result, "UTXO deleted successfully")

    def test_delete_non_existent_utxo(self):
        result = self.manager.delete_utxo("non_existent_txid", 0)
        self.assertEqual(result, "UTXO not found")

    def test_fetch_non_existent_utxo(self):
        result = self.manager.fetch_utxo("non_existent_txid", 0)
        self.assertIsNone(result)

    def tearDown(self):
        # Close the database connection after each test
        self.manager.close()

if __name__ == "__main__":
    unittest.main()

