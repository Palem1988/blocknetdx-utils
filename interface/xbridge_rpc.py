# pip install python-bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
port = '8888'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:41414"%('Testuser', 'MySuperPassword'))


def get_blockcount():
    blockcount = rpc_connection.getblockcount()
    return blockcount

def get_budget():
    snode_budget = rpc_connection.mnbudget('show')
    return snode_budget

def get_tx(txid):
    return rpc_connection.getrawtransaction(txid)
    
def send_tx(txid):
    return rpc_connection.sendrawtransaction(txid)
    
def sign_tx(txid):
    return rpc_connection.signrawtransaction(txid)

def decode_raw_tx(txid):
    return rpc_connection.decoderawtransaction(txid)

def cancel_tx(txid):
    return rpc_connection.dxCancelTransaction(txid)

def accept_tx(txid, src, dest):
    return rpc_connection.dxAcceptTransaction(txid, src, dest)

def get_currency_list():
    return rpc_connection.dxGetCurrencyList()

# dxCreateTransaction (address from) (currency from) (amount from) (address to) (currency to) (amount to)

