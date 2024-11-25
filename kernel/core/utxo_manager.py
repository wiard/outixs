import sqlite3

class UTXOManager:
    def __init__(self, db_path="database/utxos.db"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def get_all_utxos(self):
        self.cur.execute("SELECT * FROM utxos")
        return self.cur.fetchall()

    def get_utxos_by_address(self, address):
        self.cur.execute("SELECT * FROM utxos WHERE address = ?", 
(address,))
        return self.cur.fetchall()

    def get_utxo_balance(self, address):
        self.cur.execute("SELECT SUM(value) FROM utxos WHERE address = ?", 
(address,))
        return self.cur.fetchone()[0] or 0

    def remove_utxo(self, txid, output_index):
        self.cur.execute("DELETE FROM utxos WHERE txid = ? AND 
output_index = ?", (txid, output_index))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    manager = UTXOManager()

    # Example usage
    print("All UTXOs:")
    for utxo in manager.get_all_utxos():
        print(utxo)

    address = "bc1qmj02xg7hsxypexzw4xd3nr09pnq8ce3zr847mm"
    print(f"\nUTXOs for address {address}:")
    for utxo in manager.get_utxos_by_address(address):
        print(utxo)

    print(f"\nBalance for address {address}: 
{manager.get_utxo_balance(address)} sats")
    
    manager.close()

