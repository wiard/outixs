from bitcoinrpc.authproxy import AuthServiceProxy

class InscriptionTool:
    def __init__(self, rpc_user, rpc_password, rpc_host="127.0.0.1", rpc_port=8332):
        self.rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        self.rpc_client = AuthServiceProxy(self.rpc_url)

    def create_inscription(self, address, data, fee_rate=1):
        txid = self.rpc_client.sendtoaddress(address, 0.00001, "", "", True, False, fee_rate)
        self.rpc_client.settxdata(txid, {"data": data})
        return txid

    def get_inscription(self, txid):
        return self.rpc_client.gettxdata(txid)

