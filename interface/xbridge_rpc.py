
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import xbridge_config

"""
port = '8888'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:41414" % ('Testuser', 'MySuperPassword'))
"""

login = xbridge_config.get_conf_login()
pwd = xbridge_config.get_conf_password()
ip_address = xbridge_config.get_conf_IP()

if (login != "") and (pwd != "") and (ip_address != ""):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s" % (str(login), str(pwd), str(ip_address)))
else:
    print("credential information missing in the tests.conf file. Program stopped")
    exit(1)


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

rst = accept_tx("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc", "sdksdks", "sdksldk")
print(rst)

rst = create_tx("d6a0006cc", "sdksdks", 1, "sdksldk", "sdksldk", 2)
print(rst)

"""

"""
valid_src_Address = "edC5dCD9BEC36A2Baa2C5b15Bfc88b93f1cF2A3D838836c67aDaEb6"
valid_dest_Address = "C195DbfCcDb1F05f50d6E7919f19dE6E7ed"
valid_src_Token = "ZCSJH"
valid_dest_Token = "BSOUR"
invalid_sm_positive_nb = 1e-109
invalid_lg_positive_nb= \
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


# def create_tx(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount):
# create_tx(valid_src_Address, valid_src_Token, invalid_lg_positive_nb, valid_dest_Address, valid_dest_Token, invalid_lg_positive_nb)

"""