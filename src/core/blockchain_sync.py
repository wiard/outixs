import requests
import sqlite3

def fetch_block_data(block_hash):
    url = f"https://blockstream.info/api/block/{block_hash}/txs"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch block data: 
{response.status_code}")

def update_local_database(transactions):
    conn = sqlite3.connect("database/utxos.db")
    cur = conn.cursor()
    
    for tx in transactions:
        txid = tx["txid"]
        for vout in tx["vout"]:
            value = vout.get("value", 0)
            scriptpubkey = vout.get("scriptpubkey", {})
            address = scriptpubkey.get("address", "No address available")
            output_index = vout.get("n", 0)

            cur.execute("""
                INSERT INTO utxos (txid, output_index, address, value)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(txid, output_index) DO NOTHING
            """, (txid, output_index, address, value))
    
    conn.commit()
    conn.close()

def main():
    # Replace with the block hash you want to fetch
    block_hash = 
"000000000000000000006a72e68bf60bc250d601c40dc3fcad2a8573c6f353c6"
    try:
        transactions = fetch_block_data(block_hash)
        update_local_database(transactions)
        print("Local database updated successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

