
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import xbridge_config

from utils import xbridge_custom_exceptions

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

def get_core_version():
    try:
        vers = rpc_connection.getinfo()
        return vers["version"]
    except JSONRPCException:
        return 0
    
def get_blockcount():
    blockcount = rpc_connection.getblockcount()
    return blockcount
    
def decode_script(hex):
    blockcount = rpc_connection.decodescript(hex)
    return blockcount
        
def get_budget():
    snode_budget = rpc_connection.mnbudget('show')
    return snode_budget
    
def get_node_list():
    return rpc_connection.servicenodelist()
    
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
    
def get_tx_info(txid):
    return rpc_connection.dxGetTransactionInfo(txid)

def create_tx(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount):
    try:
        return rpc_connection.dxCreateTransaction(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount)
    except JSONRPCException as json_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err
    
def accept_tx(txid, src, dest):
    return rpc_connection.dxAcceptTransaction(txid, src, dest)
    
def get_currency_list():
    return rpc_connection.dxGetCurrencyList()

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

# Exception chaining here
# mnbudgetvoteraw <servicenode-tx-hash> <servicenode-tx-index> <proposal-hash> <yes|no> <time> <vote-sig>
def mnbudgetvoteraw(txhash, txindex, proposal_hash, yes_no, time, vote_sig):
    try:
        return rpc_connection.mnbudgetvoteraw(txhash, txindex, proposal_hash, yes_no, time, vote_sig)
    except UnicodeDecodeError as unicode_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("UnicodeDecodeError") from unicode_err
    except JSONRPCException as json_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err

# Exception chaining here
def spork(name_param, value_param):
    try:
        rst = rpc_connection.spork(name_param, value_param)
        if rst == "Invalid spork name":
            raise xbridge_custom_exceptions.ValidBlockNetException("Invalid spork name")
        else:
            return rst
    except JSONRPCException as json_err:
        raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err



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

print(get_blockcount())
print(get_budget())
node_list = get_node_list()
print(len(node_list))

print(get_core_version())

"""


"""
valid_src_Address = "edC5dCD9BEC36A2Baa2C5b15Bfc88b93f1cF2A3D838836c67aDaEb6"
valid_dest_Address = "C195DbfCcDb1F05f50d6E7919f19dE6E7ed"
valid_src_Token = "ZCSJH"
valid_dest_Token = "BSOUR"

invalid_sm_positive_nb = 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
invalid_lg_positive_nb = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


# def create_tx(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount):
print(create_tx(valid_src_Address, valid_src_Token, invalid_lg_positive_nb, valid_dest_Address, valid_dest_Token, invalid_lg_positive_nb))
print(create_tx(valid_src_Address, valid_src_Token, 2, valid_dest_Address, valid_dest_Token, 1000))
print(create_tx(valid_src_Address, valid_src_Token, "2,2", valid_dest_Address, valid_dest_Token, 1000))
print(create_tx(valid_src_Address, valid_src_Token, "2,2", valid_dest_Address, valid_dest_Token, invalid_lg_positive_nb))

print(rpc_connection.settxfee(0))
# return list
print(rpc_connection.getaddressesbyaccount("SyscoinTest"))
print(rpc_connection.getaddressesbyaccount(""))

returns dict
print(rpc_connection.getnettotals())
print(rpc_connection.getnetworkinfo())

print(rpc_connection.ping())
print(rpc_connection.getpeerinfo())

# print(rpc_connection.getnewaddress())
# print(rpc_connection.getaccount("dsdsd"))
# print(rpc_connection.getaccountaddress("dsds"))
print(rpc_connection.getaddressesbyaccount("cwxcxwc"))

print(rpc_connection.decodescript(""))

# print(rpc_connection.decodescript("sdsqdqsdsq"))
# print(rpc_connection.decoderawtransaction(""))
# print(rpc_connection.decoderawtransaction("sdsqdqsdsq"))
# print(rpc_connection.settxfee(-3))
# from logs


print(rpc_connection.getbalance())
print(rpc_connection.getbalance("sdsdsd"))
print(rpc_connection.getblockhash(100))

print(type(rpc_connection.getreceivedbyaccount("dsds")))

print(send_tx(""))

print(rpc_connection.submitblock(" "))
print(type(rpc_connection.submitblock("dsds")))

print(rpc_connection.getdifficulty())
print(type(rpc_connection.getdifficulty()))

returns None
print(rpc_connection.keypoolrefill())
"""

# print(rpc_connection.setaccount(rpc_connection.getnewaddress(), "dsqdsqdsqdsqdsqdsqd"))
# print(rpc_connection.listreceivedbyaccount(rpc_connection.getnewaddress()))
# print(rpc_connection.listreceivedbyaccount(99, ""))

# print(rpc_connection.listreceivedbyaddress("dsds"))

# ConnectionAbortedError: [WinError 10053] Une connexion établie a été abandonnée par un logiciel de votre ordinateur hôte
# print(rpc_connection.encryptwallet("dsds"))

# Invalid BlocknetDX address
# print(rpc_connection.dumpprivkey("dsds"))

# print(rpc_connection.dumpprivkey("dsds"))

# JSONRPCException: -8: Cannot open wallet dump file
# print(rpc_connection.dumpwallet("dsds"))

# Auto Combine Rewards Threshold Set
# print(rpc_connection.autocombinerewards(False, -99999999999999))
# print(rpc_connection.autocombinerewards(False))
# Error
# print(rpc_connection.autocombinerewards(True))

# List
# print(rpc_connection.multisend("print"))
# Error with list of commands
# print(rpc_connection.multisend(""))

# print(get_tx_info("c9a59af05356605a9c028ea7c0b9f535393d9ffe32cda4af23e3c9ccc0e5f64a"))

# print(rpc_connection.lockunspent())

"""
bitcoinrpc.authproxy.JSONRPCException: -1: spork <name> [<value>]
<name> is the corresponding spork name, or 'show' to show all current spork settings, active to show which sporks are active<value> is a epoch datetime to enable or disable spork
Requires wallet passphrase to be set with walletpassphrase call.
"""
# print(rpc_connection.spork())

# bitcoinrpc.authproxy.JSONRPCException: -1: get_value< string > called on integer Value
# print(rpc_connection.mnsync(3))

# print(rpc_connection.encryptwallet("mypwd"))

# addr = rpc_connection.getnewaddress()
# print(rpc_connection.bip38decrypt(addr))

# print(rpc_connection.getrawmempool(-1))

# print(rpc_connection.spork("*", "*"))

print(get_tx_info("////////"))
