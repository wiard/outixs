from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class BitcoinManager:
    def __init__(self, rpc_user, rpc_password, rpc_host="127.0.0.1", rpc_port=8332):
        self.rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        self.rpc_client = AuthServiceProxy(self.rpc_url)

    def fetch_utxos(self, address):
        return self.rpc_client.listunspent(0, 9999999, [address])

    def create_raw_transaction(self, inputs, outputs):
        return self.rpc_client.createrawtransaction(inputs, outputs)

    def sign_raw_transaction(self, raw_tx):
        return self.rpc_client.signrawtransactionwithwallet(raw_tx)

    def broadcast_transaction(self, signed_tx):
        return self.rpc_client.sendrawtransaction(signed_tx["hex"])

