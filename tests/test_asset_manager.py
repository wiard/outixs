import unittest
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from applications.asset_manager import AssetManager

class TestAssetManager(unittest.TestCase):

    def setUp(self):
        self.db_path = ":memory:"
        self.manager = AssetManager(self.db_path)
        self.create_test_tables()

    def tearDown(self):
        self.manager.close()

    def create_test_tables(self):
        with self.manager.conn:
            self.manager.cur.execute("""
                CREATE TABLE IF NOT EXISTS utxos (
                    txid TEXT PRIMARY KEY,
                    output_index INTEGER
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

    def test_create_asset_from_utxo(self):
        with self.manager.conn:
            self.manager.cur.execute("INSERT INTO utxos (txid, output_index) VALUES (?, ?)", 
                                      ("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0))

        result = self.manager.create_asset_from_utxo(
            txid="5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052",
            output_index=0,
            asset_name="Golden Sword",
            metadata="A unique sword with magical powers."
        )
        self.assertEqual(result, "Asset 'Golden Sword' created from UTXO 5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052:0.")
        
        self.manager.cur.execute("SELECT * FROM assets WHERE asset_name = 'Golden Sword'")
        asset = self.manager.cur.fetchone()
        self.assertIsNotNone(asset)
        self.assertEqual(asset[2], "Golden Sword")
    
    def test_get_all_assets(self):
        with self.manager.conn:
            self.manager.cur.execute("""
                INSERT INTO assets (txid, output_index, asset_name, metadata)
                VALUES (?, ?, ?, ?)
            """, ("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, "Golden Sword", "A unique sword with magical powers."))

        assets = self.manager.get_all_assets()
        self.assertEqual(len(assets), 1)
        self.assertEqual(assets[0][2], "Golden Sword")

    def test_get_assets_by_name(self):
        with self.manager.conn:
            self.manager.cur.execute("""
                INSERT INTO assets (txid, output_index, asset_name, metadata)
                VALUES (?, ?, ?, ?)
            """, ("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, "Golden Sword", "A unique sword with magical powers."))

        assets = self.manager.get_assets_by_name("Golden Sword")
        self.assertEqual(len(assets), 1)
        self.assertEqual(assets[0][2], "Golden Sword")

    def test_delete_asset(self):
        with self.manager.conn:
            self.manager.cur.execute("""
                INSERT INTO assets (txid, output_index, asset_name, metadata)
                VALUES (?, ?, ?, ?)
            """, ("5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052", 0, "Golden Sword", "A unique sword with magical powers."))

        result = self.manager.delete_asset("Golden Sword")
        self.assertEqual(result, "Asset 'Golden Sword' deleted.")
        
        self.manager.cur.execute("SELECT * FROM assets WHERE asset_name = 'Golden Sword'")
        asset = self.manager.cur.fetchone()
        self.assertIsNone(asset)

if __name__ == '__main__':
    unittest.main()

