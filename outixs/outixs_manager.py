import json

class OutixsManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def mirror_utxo(self, utxo, metadata):
        mirrored_outixs = {
            "original_txid": utxo["txid"],
            "value": utxo["value"],
            "metadata": metadata,
            "state": "pending"
        }
        self.save_outixs(mirrored_outixs)
        return mirrored_outixs

    def save_outixs(self, outixs):
        with open(self.db_path, 'a') as db:
            db.write(json.dumps(outixs) + '\n')

    def get_all_outixs(self):
        with open(self.db_path, 'r') as db:
            return [json.loads(line) for line in db]

