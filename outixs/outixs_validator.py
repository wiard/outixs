class OutixsValidator:
    def validate(self, outixs):
        if not outixs.get("utxo"):
            return False
        if not isinstance(outixs.get("metadata"), dict):
            return False
        if not outixs.get("conditions"):
            return False
        return True

