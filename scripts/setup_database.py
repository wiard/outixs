import sqlite3


def initialize_database(db_path="database/utxos.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create the UTXOs table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS utxos (
            txid TEXT,
            output_index INTEGER,
            address TEXT,
            value INTEGER,
            block_height INTEGER,
            PRIMARY KEY (txid, output_index)
        );
    """
    )

    # Create the Assets table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS assets (
            txid TEXT,
            output_index INTEGER,
            asset_name TEXT UNIQUE,
            metadata TEXT,
            PRIMARY KEY (txid, output_index)
        );
    """
    )

    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")


if __name__ == "__main__":
    initialize_database()
