import sqlite3

class AssetManager:
    def __init__(self, db_path="database/utxos.db"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create_asset_from_utxo(self, txid, output_index, asset_name, metadata):
        self.cur.execute(
            "SELECT * FROM utxos WHERE txid = ? AND output_index = ?",
            (txid, output_index),
        )
        utxo = self.cur.fetchone()

        if not utxo:
            raise ValueError(f"UTXO {txid}:{output_index} does not exist.")

        self.cur.execute(
            """
            INSERT INTO assets (txid, output_index, asset_name, metadata)
            VALUES (?, ?, ?, ?)
        """,
            (txid, output_index, asset_name, metadata),
        )

        self.conn.commit()
        return f"Asset '{asset_name}' created from UTXO {txid}:{output_index}."

    def get_all_assets(self):
        self.cur.execute("SELECT * FROM assets")
        return self.cur.fetchall()

    def get_assets_by_name(self, asset_name):
        self.cur.execute("SELECT * FROM assets WHERE asset_name = ?", (asset_name,))
        return self.cur.fetchall()

    def delete_asset(self, asset_name):
        self.cur.execute("DELETE FROM assets WHERE asset_name = ?", (asset_name,))
        self.conn.commit()
        return f"Asset '{asset_name}' deleted."

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    manager = AssetManager()

    try:
        print(
            manager.create_asset_from_utxo(
                txid="5f240ed7aa2b4cd8ba46baf46a8e3e43e430f33de72c93a0ca5e06fe9cb95052",
                output_index=0,
                asset_name="Golden Sword",
                metadata="A unique sword with magical powers.",
            )
        )
    except ValueError as e:
        print(e)

    print("\nAll Assets:")
    for asset in manager.get_all_assets():
        print(asset)

    print("\nAssets named 'Golden Sword':")
    for asset in manager.get_assets_by_name("Golden Sword"):
        print(asset)

    print("\nDeleting asset 'Golden Sword':")
    print(manager.delete_asset("Golden Sword"))

    manager.close()

