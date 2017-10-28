# pip install python-bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
port = '8888'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:41414"%('Testuser', 'MySuperPassword'))


def get_blockcount():
    blockcount = rpc_connection.getblockcount()
    return blockcount

def get_tx(txid):
    return rpc_connection.getrawtransaction(txid)
    
def send_tx(txid):
    return rpc_connection.sendrawtransaction(txid)
    
def sign_tx(txid):
    return rpc_connection.decoderawtransaction(txid)

def decode_raw_tx(txid):
    return rpc_connection.decoderawtransaction(txid)
    
def get_budget():
    snode_budget = rpc_connection.mnbudget('show')
    return snode_budget

def cancel_tx(txid):
    return rpc_connection.dxCancelTransaction(txid)

