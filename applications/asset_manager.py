import sqlite3

class AssetManager:
    def __init__(self, db_path="data/marketplace.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                metadata TEXT
            )
        """)
        self.conn.commit()

    def add_asset(self, name, metadata):
        self.cursor.execute("INSERT INTO assets (name, metadata) VALUES (?, ?)", (name, 
metadata))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_asset_metadata(self, asset_id):
        self.cursor.execute("SELECT metadata FROM assets WHERE id = ?", (asset_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def update_asset_metadata(self, asset_id, metadata):
        self.cursor.execute("UPDATE assets SET metadata = ? WHERE id = ?", (metadata, asset_id))
        self.conn.commit()

    def remove_asset(self, asset_id):
        self.cursor.execute("DELETE FROM assets WHERE id = ?", (asset_id,))
        self.conn.commit()

