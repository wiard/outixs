import unittest
import sqlite3
from kernel.core.utxo_manager import UTXOManager

class TestUTXOManager(unittest.TestCase):
    
    def setUp(self):
        self.db_path = ":memory:"
        self.manager = UTXOManager(self.db_path)
        self.create_test_tables()

    def tearDown(self):
        self.manager.close()

    def create_test_tables(self):
        with self.manager.conn:
            self.manager.cur.execute("""
                CREATE TABLE IF NOT EXISTS utxos (
                    txid TEXT PRIMARY KEY,
                    output_index INTEGER,
                    amount INTEGER
                )
            """)
            self.manager.cur.execute("""
                CREATE TABLE IF NOT EXISTS assets (
                    txid TEXT,
                    output_index INTEGER,
                    asset_name TEXT,
                    metadata TEXT,
                    PRIMARY KEY (txid, output_index)
                )
            """)

    def test_add_utxo(self):
        result = self.manager.add_utxo("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, 1000)
        self.assertEqual(result, "UTXO added successfully")
        
        self.manager.cur.execute("SELECT * FROM utxos WHERE txid = ?", 
("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052",))
        utxo = self.manager.cur.fetchone()
        self.assertIsNotNone(utxo)
        self.assertEqual(utxo[0], "5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052")
    
    def test_fetch_utxo(self):
        self.manager.add_utxo("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, 1000)
        utxo = self.manager.fetch_utxo("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0)
        self.assertIsNotNone(utxo)
        self.assertEqual(utxo[0], "5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052")
    
    def test_delete_utxo(self):
        self.manager.add_utxo("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, 1000)
        result = self.manager.delete_utxo("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0)
        self.assertEqual(result, "UTXO deleted successfully")
        
        self.manager.cur.execute("SELECT * FROM utxos WHERE txid = ?", 
("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052",))
        utxo = self.manager.cur.fetchone()
        self.assertIsNone(utxo)

    def test_fetch_non_existent_utxo(self):
        utxo = self.manager.fetch_utxo("nonexistent_txid", 0)
        self.assertIsNone(utxo)
    
    def test_delete_non_existent_utxo(self):
        result = self.manager.delete_utxo("nonexistent_txid", 0)
        self.assertEqual(result, "UTXO not found")

if __name__ == '__main__':
    unittest.main()

