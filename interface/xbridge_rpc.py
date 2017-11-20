
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

def walletpassphrasechange(old=None, new=None):
    try:
        return rpc_connection.walletpassphrasechange(old, new)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Error: The wallet passphrase entered was incorrect" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def walletpassphrase(passphrase=None, timeout=0, anonymizeonly=False):
    try:
        return rpc_connection.walletpassphrase(passphrase, timeout, anonymizeonly)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "running with an unencrypted wallet, but walletpassphrase was called" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# backupwallet "destination"
def backupwallet(destination):
    try:
        return rpc_connection.backupwallet(destination)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt    
    
# bip38encrypt "blocknetdxaddress"
def bip38decrypt(blocknetdxaddress):
    try:
        return rpc_connection.bip38decrypt(blocknetdxaddress)
    except JSONRPCException as json_excpt:
        if "-1: bip38decrypt \"blocknetdxaddress\"" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt    
    
# bip38encrypt "blocknetdxaddress"
def bip38encrypt(blocknetdxaddress):
    try:
        return rpc_connection.bip38encrypt(blocknetdxaddress)
    except JSONRPCException as json_excpt:
        if "-1: bip38encrypt \"blocknetdxaddress\"" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt    
    
# setgenerate generate ( genproclimit )
def setgenerate(generate, genproclimit=None):
    try:
        return rpc_connection.setgenerate(generate, genproclimit)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# listtransactions ( "account" count from includeWatchonly)
def listtransactions(account=None, count=None, from_param=None, includeWatchonly=None):
    try:
        return rpc_connection.listtransactions(account, count, from_param, includeWatchonly)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# reservebalance [<reserve> [amount]]
def reservebalance(reserve, amount):
    try:
        return rpc_connection.reservebalance(reserve, amount)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# addnode "node" "add|remove|onetry"
def addnode(node_str, cmd):
    try:
        return rpc_connection.addnode(node_str, cmd)
    except JSONRPCException as json_excpt:
        if "Error: Node has not been added" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# getaddednodeinfo dns bool ( "node" )
def getaddednodeinfo(dns_bool, node_str=None):
    try:
        return rpc_connection.getaddednodeinfo(dns_bool, node_str)
    except JSONRPCException as json_excpt:
        if "Error: Node has not been added" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# verifymessage "blocknetdxaddress" "signature" "message"
def verifymessage(blocknetdxaddress, signature, message):
    try:
        return rpc_connection.verifymessage(blocknetdxaddress, signature, message)
    except JSONRPCException as json_excpt:
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
    
def validateaddress(address):
    try:
        return rpc_connection.validateaddress(address)
    except JSONRPCException as json_excpt:
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
            
def estimatepriority(int_value):
    try:
        return rpc_connection.estimatepriority(int_value)
    except JSONRPCException as json_excpt:
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
            
def estimatefee(int_value):
    try:
        return rpc_connection.estimatefee(int_value)
    except JSONRPCException as json_excpt:
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def importprivkey(blocknetdxprivkey, label=None, rescan=None):
    try:
        return rpc_connection.importprivkey(blocknetdxprivkey, label, rescan)
    except JSONRPCException as json_excpt:
        if "Invalid private key encoding" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def dumpprivkey(blocknetdxaddress):
    try:
        return rpc_connection.dumpprivkey(blocknetdxaddress)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def prioritisetransaction(txid, priority, fee):
    try:
        return rpc_connection.prioritisetransaction(txid, priority, fee)
    except UnicodeDecodeError as unicode_err:
        raise xbridge_custom_exceptions.ValidBlockNetException from unicode_err
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "txid must be hexadecimal string" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Parse error" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getnetworkhashps(blocks, height):
    try:
        return rpc_connection.getnetworkhashps(blocks, height)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getreceivedbyaccount(address=None):
    try:
        return rpc_connection.getreceivedbyaccount(address)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getaccountaddress(address=None):
    try:
        return rpc_connection.getbalance(address)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getaddressesbyaccount(account=None):
    try:
        return rpc_connection.getbalance(account)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# getbalance ( "account" minconf includeWatchonly )
def getbalance(account=None, minconf=None, includeWatchonly=None):
    try:
        return rpc_connection.getbalance(account, minconf, includeWatchonly)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def sendtoaddress(txid=None):
    try:
        return rpc_connection.sendtoaddress(txid)
    except JSONRPCException as json_excpt:
        valid_msgs = ["-6: Insufficient funds"]
        if str(json_excpt) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def send_tx(txid=None):
    try:
        return rpc_connection.sendrawtransaction(txid)
    except JSONRPCException as json_excpt:
        valid_msgs = ["-22: TX decode failed"]
        if str(json_excpt) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def decode_raw_tx(txid=None):
    try:
        return rpc_connection.decoderawtransaction(txid)
    except JSONRPCException as json_excpt:
        valid_msgs = ["-22: TX decode failed"]
        if str(json_excpt) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Expected type" in str(json_excpt) and "got" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def sign_message(address=None, msg=None):
    try:
        rpc_connection.signmessage(address, msg)
    except JSONRPCException as json_excpt:
        valid_msgs = ["-3: Invalid address", "-32700: Parse error"]
        if str(json_excpt) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "-1: get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def sign_tx(txid=None):
    return rpc_connection.signrawtransaction(txid)
    
def cancel_tx(txid=None):
    return rpc_connection.dxCancelTransaction(txid)
    
def get_tx_info(txid=None):
    return rpc_connection.dxGetTransactionInfo(txid)

def create_tx(fromAddress=None, fromToken=None, fromAmount=None, toAddress=None, toToken=None, toAmount=None):
    try:
        return rpc_connection.dxCreateTransaction(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount)
    except JSONRPCException as json_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err
    
def accept_tx(txid=None, src=None, dest=None):
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

# mnbudgetvoteraw <servicenode-tx-hash> <servicenode-tx-index> <proposal-hash> <yes|no> <time> <vote-sig>
def mnbudgetvoteraw(txhash=None, txindex=None, proposal_hash=None, yes_no=None, time=None, vote_sig=None):
    try:
        return rpc_connection.mnbudgetvoteraw(txhash, txindex, proposal_hash, yes_no, time, vote_sig)
    except UnicodeDecodeError as unicode_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("UnicodeDecodeError") from unicode_err
    except JSONRPCException as json_err:
        # raise JSONRPCException
        raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err

def spork(name_param=None, value_param=None):
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
# print(rpc_connection.autocombinerewards(True, -99999999999999))
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

# print(decode_raw_tx(9999999999999999999999999999999999999999999999999999999999999999))
# print(decode_raw_tx(-9999999999999999999999999999999999999999999999999999999999999999))

# print(send_tx("-"))
# print(send_tx(9999999999999999999999999999999999999999999999999999999999999999))
# print(send_tx(-9999999999999999999999999999999999999999999999999999999999999999))

# print(rpc_connection.getmininginfo())
# print(rpc_connection.getnetworkhashps())
# print(rpc_connection.getnetworkhashps(0, -9999999))
# print(rpc_connection.prioritisetransaction(9999999999999999999999999999999999999999999999999999999999999999, "-", " "))

# print(importprivkey(True))
# bitcoinrpc.authproxy.JSONRPCException: -3: Expected type integer, got real
# bitcoinrpc.authproxy.JSONRPCException: -3: Expected type integer, got string
# decimal
# print(rpc_connection.estimatefee(0))
# print(rpc_connection.estimatefee(-100))

# returns None if wrong int or bool, or if wrong string {'isvalid': False}
# print(verifymessage("dsds", "dsd", "sdsdk"))
# print(rpc_connection.importprivkey("dsdsdddddddddddddddddddddddddd"))
# print(rpc_connection.reservebalance(True, "dklsd"))

# print(rpc_connection.getaddednodeinfo(False, ""))
# print(addnode("dsd", "dsdsd"))

# print(rpc_connection.getinfo())

## print(getaddednodeinfo("dsd", "dsd"))

# {'id': '0000000000000000000000000000000000000000000000000000000000000000'}
# print(create_tx("", "", 0, "", "", 0))
# print(create_tx("dsds", "dsd", 10, "dsqdsq", "dsqdsqd", 10))

# returns a list
# print(rpc_connection.listtransactions("", 0, 0, False))
# print(rpc_connection.listtransactions("", 0, 0, True))

# print(rpc_connection.bip38decrypt(-2))
# print(rpc_connection.validateaddress("dksldks"))
# print(rpc_connection.validateaddress(2))
# print(rpc_connection.verifymessage(rpc_connection.getnewaddress(), "dsdsd", "dsdsds"))

# print(rpc_connection.encryptwallet("mypwd"))
# print(rpc_connection.walletpassphrase("mypwd", 60, False))
# print(rpc_connection.dumpwallet("C:\\Users\\kbentahmed\\Desktop\\BlockNetDX\\test_wallet_dump5.dat"))

# None if successful
# print(rpc_connection.walletpassphrasechange("mypwd2", "mypwd"))
# print(rpc_connection.walletlock(""))
