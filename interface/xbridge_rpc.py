
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

port = '8888'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:41414"%('Testuser', 'MySuperPassword'))

def get_blockcount():
    try:
        blockcount = rpc_connection.getblockcount()
        return blockcount
    except JSONRPCException:
        return 0

def get_budget():
    try:
        snode_budget = rpc_connection.mnbudget('show')
        return snode_budget
    except JSONRPCException:
        return None

def get_node_list():
    try:
        return rpc_connection.servicenodelist()
    except JSONRPCException:
        return None

def get_tx(txid):
    try:
        return rpc_connection.getrawtransaction(txid)
    except JSONRPCException:
        return None
    
def send_tx(txid):
    try:
        return rpc_connection.sendrawtransaction(txid)
    except JSONRPCException:
        return None
    
def sign_tx(txid):
    try:
        return rpc_connection.signrawtransaction(txid)
    except JSONRPCException:
        return None

def decode_raw_tx(txid):
    try:
        return rpc_connection.decoderawtransaction(txid)
    except JSONRPCException:
        return None

def cancel_tx(txid):
    try:
        return rpc_connection.dxCancelTransaction(txid)
    except JSONRPCException:
        return None

def get_tx_info(txid):
    try:
        return rpc_connection.dxGetTransactionInfo(txid)
    except JSONRPCException:
        return None

def create_tx(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount):
    try:
        return rpc_connection.dxCreateTransaction(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount)
    except JSONRPCException:
        return None

def accept_tx(txid, src, dest):
    try:
        return rpc_connection.dxAcceptTransaction(txid, src, dest)
    except JSONRPCException:
        return None

def get_currency_list():
    try:
        return rpc_connection.dxGetCurrencyList()
    except JSONRPCException:
        return None

def get_transaction_list():
    try:
        return rpc_connection.dxGetTransactionList()
    except JSONRPCException:
        return None

def get_transaction_history_list():
    try:
        return rpc_connection.dxGetTransactionsHistoryList()
    except JSONRPCException:
        return None


"""
rst = get_tx_info("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc")
print(rst)
print(len(rst))

rst = cancel_tx("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc")
print(rst)
"""
