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

valid_msgs = ["-22: TX decode failed", 
                    "-3: Invalid address", 
                    "-32700: Parse error", 
                    "must be hexadecimal string",
                    "txid must be hexadecimal string",                    
                    "-3: Expected type",
                    "Expected type"
                    "Invalid private key encoding", 
                    "Error: Node has not been added",
                    "Invalid parameter",
                    "Cannot open wallet dump file",
                    "get_value",
                    "Insufficient funds", 
                    "Invalid amount",
                    "running with an unencrypted wallet, but walletpassphrase was called", 
                    "Error: The wallet passphrase entered was incorrect", 
                    "-1: bip38decrypt \"blocknetdxaddress\"", 
                    "-1: bip38encrypt \"blocknetdxaddress\""]
   

def cancel_tx(txid=None):
    return rpc_connection.dxCancelTransaction(txid)
    
def get_tx_info(txid=None):
    return rpc_connection.dxGetTransactionInfo(txid)

def create_tx(fromAddress=None, fromToken=None, fromAmount=None, toAddress=None, toToken=None, toAmount=None):
    try:
        return rpc_connection.dxCreateTransaction(fromAddress, fromToken, fromAmount, toAddress, toToken, toAmount)
    except JSONRPCException as json_err:
        if str(json_err) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err
    
def accept_tx(txid=None, src=None, dest=None):
    try:
        return rpc_connection.dxAcceptTransaction(txid, src, dest)
    except JSONRPCException as json_err:
        if str(json_err) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException("JSONRPCException") from json_err
    
def get_currency_list():
    return rpc_connection.dxGetCurrencyList()

def get_transaction_list():
    return rpc_connection.dxGetTransactionList()

def get_transaction_history_list():
    return rpc_connection.dxGetTransactionsHistoryList()

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

# lockunspent unlock [{"txid":"txid","vout":n},...]
# string + string
def lockunspent(unlock=None, txid=None):
    try:
        return rpc_connection.lockunspent(unlock, txid)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# move "fromaccount" "toaccount" amount ( minconf "comment" )
def move(fromaccount=None, toaccount=None, amount=None, minconf=None, comment=None):
    try:
        return rpc_connection.move(fromaccount, toaccount, amount, minconf, comment)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
    
# autocombinerewards <true/false> threshold
def autocombinerewards(true_false=None, threshold=None):
    try:
        return rpc_connection.autocombinerewards(true_false, threshold)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        
# sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
def importwallet(filename_str=None):
    try:
        return rpc_connection.importwallet(filename_str)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# listsinceblock ("blockhash" target-confirmations includeWatchonly)
def listsinceblock(blockhash=None, target_confirmations=None, includeWatchonly=None):
    try:
        return rpc_connection.listsinceblock(blockhash, target_confirmations, includeWatchonly)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# getblockhash index
def getblockhash(index=None):
    try:
        return rpc_connection.getblockhash(index)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# getrawmempool ( verbose )
def getrawmempool(verbose=None):
    try:
        return rpc_connection.getrawmempool(verbose)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# verifychain ( checklevel numblocks )
def verifychain(checklevel=None, numblocks=None):
    try:
        return rpc_connection.verifychain(checklevel, numblocks)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# listreceivedbyaddress (minconf includeempty includeWatchonly)
def listreceivedbyaddress(minconf=None, includeempty=None, includeWatchonly=None):
    try:
        return rpc_connection.listreceivedbyaddress(minconf, includeempty, includeWatchonly)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# listreceivedbyaccount (minconf includeempty includeWatchonly)
def listreceivedbyaccount(minconf=None, includeempty=None, includeWatchonly=None):
    try:
        return rpc_connection.listreceivedbyaccount(minconf, includeempty, includeWatchonly)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def settxfee(amount=None):
    try:
        return rpc_connection.settxfee(amount)
    except JSONRPCException as json_excpt:
        if str(json_excpt) in valid_msgs:
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
def sendtoaddressix(blocknetdxaddress=None, amount=None, comment=None, commentto=None):
    try:
        return rpc_connection.sendtoaddressix(blocknetdxaddress, amount, comment, commentto)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
def sendtoaddress(blocknetdxaddress=None, amount=None, comment=None, commentto=None):
    try:
        return rpc_connection.sendtoaddress(blocknetdxaddress, amount, comment, commentto)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

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

# listaccounts (minconf includeWatchonly)
def listaccounts(minconf=None, includeWatchonly=None):
    try:
        return rpc_connection.listaccounts(minconf, includeWatchonly)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Parse error" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# listtransactions ( "account" count from includeWatchonly)
def listtransactions(account=None, count=None, from_param=None, includeWatchonly=None):
    try:
        return rpc_connection.listtransactions(account, count, from_param, includeWatchonly)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Parse error" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# reservebalance [<reserve> [amount]]
def reservebalance(reserve, amount):
    try:
        return rpc_connection.reservebalance(reserve, amount)
    except JSONRPCException as json_excpt:
        if "get_value" in str(json_excpt) and "called on" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Parse error" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# addnode "node" "add|remove|onetry"
def addnode(node_str, cmd):
    try:
        return rpc_connection.addnode(node_str, cmd)
    except JSONRPCException as json_excpt:
        if "Error: Node has not been added" in str(json_excpt):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        if "Parse error" in str(json_excpt):
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
        if any(t in str(json_excpt) for t in valid_msgs):
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
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getnetworkhashps(blocks, height):
    try:
        return rpc_connection.getnetworkhashps(blocks, height)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getreceivedbyaccount(address=None):
    try:
        return rpc_connection.getreceivedbyaccount(address)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getaccountaddress(address=None):
    try:
        return rpc_connection.getbalance(address)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def getaddressesbyaccount(account=None):
    try:
        return rpc_connection.getbalance(account)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

# getbalance ( "account" minconf includeWatchonly )
def getbalance(account=None, minconf=None, includeWatchonly=None):
    try:
        return rpc_connection.getbalance(account, minconf, includeWatchonly)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def sendtoaddress(txid=None):
    try:
        return rpc_connection.sendtoaddress(txid)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        
def send_tx(txid=None):
    try:
        return rpc_connection.sendrawtransaction(txid)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        
def decode_raw_tx(txid=None):
    try:
        return rpc_connection.decoderawtransaction(txid)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

def sign_message(address=None, msg=None):
    try:
        rpc_connection.signmessage(address, msg)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt
        
# signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )
def signrawtransaction(hexstring=None, optional_param=None):
    try:
        return rpc_connection.signrawtransaction(hexstring, optional_param)
    except JSONRPCException as json_excpt:
        if any(t in str(json_excpt) for t in valid_msgs):
            raise xbridge_custom_exceptions.ValidBlockNetException from json_excpt

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


