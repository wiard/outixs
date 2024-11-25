import sqlite3

class UTXOManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def add_utxo(self, txid, output_index, amount):
        self.cur.execute("INSERT OR REPLACE INTO utxos (txid, output_index, amount) VALUES (?, ?, ?)", 
                         (txid, output_index, amount))
        self.conn.commit()
        return "UTXO added successfully"

    def fetch_utxo(self, txid, output_index):
        self.cur.execute("SELECT * FROM utxos WHERE txid = ? AND output_index = ?", (txid, output_index))
        return self.cur.fetchone()

    def delete_utxo(self, txid, output_index):
        self.cur.execute("DELETE FROM utxos WHERE txid = ? AND output_index = ?", (txid, output_index))
        self.conn.commit()
        if self.cur.rowcount == 0:
            return "UTXO not found"
        return "UTXO deleted successfully"

    def close(self):
        self.conn.close()

