import unittest
import sqlite3
from applications.asset_manager import AssetManager

class TestAssetManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = "data/marketplace.db"
        conn = sqlite3.connect(cls.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                metadata TEXT
            );
        """)
        conn.commit()
        conn.close()

    def setUp(self):
        self.asset_manager = AssetManager(db_path="data/marketplace.db")

    def test_add_asset(self):
        asset_id = self.asset_manager.add_asset("TestAsset", "TestMetadata")
        asset = self.asset_manager.get_asset_metadata(asset_id)
        self.assertEqual(asset, "TestMetadata")

    def test_get_asset_metadata(self):
        asset_id = self.asset_manager.add_asset("MetadataTest", "SomeMetadata")
        metadata = self.asset_manager.get_asset_metadata(asset_id)
        self.assertEqual(metadata, "SomeMetadata")

    def test_update_asset_metadata(self):
        asset_id = self.asset_manager.add_asset("UpdateTest", "OldMetadata")
        self.asset_manager.update_asset_metadata(asset_id, "NewMetadata")
        updated_metadata = self.asset_manager.get_asset_metadata(asset_id)
        self.assertEqual(updated_metadata, "NewMetadata")

    def test_remove_asset(self):
        asset_id = self.asset_manager.add_asset("RemoveTest", "RemoveMetadata")
        self.asset_manager.remove_asset(asset_id)
        asset = self.asset_manager.get_asset_metadata(asset_id)
        self.assertIsNone(asset)

    def test_get_nonexistent_asset(self):
        asset = self.asset_manager.get_asset_metadata(999)
        self.assertIsNone(asset)

if __name__ == "__main__":
    unittest.main()

