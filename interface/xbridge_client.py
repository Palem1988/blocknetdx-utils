import subprocess
import json
# ++ https://stackoverflow.com/questions/24849998/how-to-catch-exception-output-from-python-subprocess-check-output
import traceback
import time

from utils import xbridge_utils

CLIENT_PATH = "C:\\Program Files\\Blocknetdx\\daemon\\blocknetdx-cli.exe"

def CHECK_ACCEPT_TX(txid, src, dest):
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxAcceptTransaction', txid, src, dest])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
        pass
    # except subprocess.CalledProcessError as e:
        # tb = traceback.format_exc()
        # print("tb: " + tb)

def TIMED_CHECK_ACCEPT_TX(j):
    garbage_input_str1 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str2 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str3 = xbridge_utils.generate_garbage_input(j)
    ts = time.time()
    CHECK_ACCEPT_TX(garbage_input_str1, garbage_input_str2, garbage_input_str3)
    # assert type(CHECK_ACCEPT_TX(garbage_input_str1, garbage_input_str2, garbage_input_str3)) == None
    te = time.time()
    return te - ts

# return: b'{\r\n    "id" : "0000000000000000000000000000000000000000000000000000000000000000"\r\n}\r\n'
def CHECK_CANCEL_TX(txid):
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxCancelTransaction', txid])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
    # except subprocess.CalledProcessError as e:
        tb = traceback.format_exc()
        print("tb: " + tb)

def TIMED_CHECK_CANCEL_TX_LIST(j):
    garbage_input_str = xbridge_utils.generate_garbage_input(j)
    ts = time.time()
    assert type(CHECK_CANCEL_TX(garbage_input_str)) == dict
    te = time.time()
    return te - ts

# CHECK_CREATE_TX("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", "LTC", 1, "12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey", "SYS", 1)
def CHECK_CREATE_TX(src_Address, src_Curr, src_Qty, dest_Address, dest_Curr, dest_Qty):
    try:
        rst = subprocess.check_output([CLIENT_PATH, 'dxCreateTransaction', src_Address, src_Curr, src_Qty, dest_Address, dest_Curr, dest_Qty])
        return rst
    except:
        pass
    # except subprocess.CalledProcessError as e:
        # tb = traceback.format_exc()
        # print("tb: " + tb)
        # print("e output: " + e.output)
        # raise Exception("An error occured")
        # exit(1)


def TIMED_CHECK_CREATE_TX(j):
    garbage_input_str1 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str2 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str3 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str4 = xbridge_utils.generate_garbage_input(j)
    source_nb = xbridge_utils.generate_random_number(-9999999999999, 999999999999)
    dest_nb = xbridge_utils.generate_random_number(-9999999999999, 999999999999)
    ts = time.time()
    CHECK_CREATE_TX(garbage_input_str1, garbage_input_str2, source_nb, garbage_input_str3, garbage_input_str4, dest_nb)
    # assert type(CHECK_ACCEPT_TX(garbage_input_str1, garbage_input_str2, garbage_input_str3)) == None
    te = time.time()
    return te - ts


def GENERIC_RAW_TX(raw_cmd, param):
    try:
        rst = subprocess.check_output([CLIENT_PATH, raw_cmd, param])
        return rst
    except:
        pass
    # except subprocess.CalledProcessError as e:
        # tb = traceback.format_exc()
        # print("tb: " + tb)
        # print("e output: " + e.output)
        # raise Exception("An error occured")
        # exit(1)

def TIMED_GENERIC_RAW_TX(raw_cmd, param):
    try:
        ts = time.time()
        rst = subprocess.check_output([CLIENT_PATH, raw_cmd, param])
        te = time.time()
        return te - ts
    except:
        return 0

# createrawtransaction "[{\"txid\":\"dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF\",\"vout\":0}]" "{\"address\":0.01}"
# ==> Invalid BlocknetDX address: address (code -5)
# blocknetdx-cli createrawtransaction "[{\"txid\":\"myid\",\"vout\":0}]" "{\"address\":0.01}"
def CREATE_RAW_TX(txid, vout, address_amount):
    try:
        first_Param = "[{'txid':" + txid + ",'vout\':" + vout + "}]"
        second_Param = "{'address':" + address_amount + "}"
        rst = subprocess.check_output([CLIENT_PATH, 'createrawtransaction', first_Param, second_Param])
        return rst
    except:
        pass

def CHECK_GET_TX_LIST():
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxGetTransactionList'])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
    # except subprocess.CalledProcessError as e:
        tb = traceback.format_exc()
        print("tb: " + tb)

def TIMED_CHECK_GET_TX_LIST():
    ts = time.time()
    assert type(CHECK_GET_TX_LIST()) == list
    te = time.time()
    return te - ts

def CHECK_GET_TX_HISTORY_LIST():
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxGetTransactionsHistoryList'])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
        tb = traceback.format_exc()
        print("tb: " + tb)

def TIMED_CHECK_GET_TX_HISTORY_LIST():
    ts = time.time()
    assert type(CHECK_GET_TX_HISTORY_LIST()) == list
    te = time.time()
    return te - ts

def CHECK_GET_TX_INFO(tx):
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxGetTransactionInfo', tx])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
    # except subprocess.CalledProcessError as e:
        tb = traceback.format_exc()
        print("tb: " + tb)

def TIMED_CHECK_GET_TX_INFO(car_length):
    garbage_input_str = xbridge_utils.generate_garbage_input(car_length)
    ts = time.time()
    assert type(CHECK_GET_TX_INFO(garbage_input_str)) == list
    te = time.time()
    return te - ts

def CHECK_GET_CURRENCY_LIST():
    try:
        bytes_string = subprocess.check_output([CLIENT_PATH, 'dxGetCurrencyList'])
        rst_str = str(bytes_string, 'utf-8')
        rst = json.loads(rst_str)
        return rst
    except:
        # except subprocess.CalledProcessError as e:
        tb = traceback.format_exc()
        print("tb: " + tb)


def TIMED_CHECK_GET_CURRENCY_LIST():
    ts = time.time()
    assert type(CHECK_GET_CURRENCY_LIST()) == dict
    te = time.time()
    return te - ts


# print(CHECK_ACCEPT_TX("wccwxc", "cxcxwc", "cxcxcxw"))
# print(type(CHECK_ACCEPT_TX("wccwxc", "cxcxwc", "cxcxcxw")))
# CHECK_ACCEPT_TX("wccwxc", "cxcxwc", "cxcxcxw")
# TIMED_CHECK_ACCEPT_TX(3)
#for i in range(100):
    # print(TIMED_CHECK_CREATE_TX(3))

# print(CHECK_GET_TX_INFO(" "))
# print(CHECK_GET_CURRENCY_LIST())
# CHECK_CANCEL_TX(StringGenerator('[\p\d\W\w\h]{40000}').render())
# print(CHECK_CANCEL_TX("d63f5ed682ad744b176af1d58e9602219a40ab9bf3b506baeca81b975*$*ù/!."))
# print(CHECK_CANCEL_TX("d63f5ed682ad744b176af1d58e9602219a40ab9bf3b506baeca81b975XXXXXXXXXX"))

# createrawtransaction "[{\"txid\":\"dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF\",\"vout\":0}]" "{\"address\":0.01}"
# ==> Invalid BlocknetDX address: address (code -5)

# createrawtransaction "[{"txid": "dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF","vout":0}]" "{"address":0.01}"
# Error: Error parsing JSON:[{txid: dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF,vout:0}]

# createrawtransaction "[{\"txid\": \"dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF\", \"vout\":0}]" "{\"address\":0.01}"
# ==> Invalid BlocknetDX address: address (code -5)

# createrawtransaction "[{\"txid\": \"dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF\"
# ==>  Parse error: unbalanced ' or "

# createrawtransaction "{\"address\":0.01}"
# ==> Method not found (code -32601)

# createrawtransaction [] {}
# createrawtransaction [""] {""}
# createrawtransaction "[]" "{}"
# ==> 01000000000000000000

# createrawtransaction "[]" "{}"

# createrawtransaction [[]] {}
# get_value< Object > called on Array Value (code -1)

# createrawtransaction "[{\"txid\": "\"2\", \"vout\":"0"}]" "{\"address\":0.01}"
# sendrawtransaction sss

"""
print(CHECK_RAW_CREATE_TX("dcfb97dEb93b1c93ca3Ad55bb6aE8BED18a86Ed0F989ddf6Abc77DdDE75E0a9E1E1f3Ca6c9ba77C1432bFA3FFbb0C1A537DF", 2, 2))
hex_str = StringGenerator('[\h]{100}').render()
print(hex_str)
print(CHECK_RAW_CREATE_TX(hex_str, -2, 2))

rst = subprocess.check_output([CLIENT_PATH, 'createrawtransaction', "[]", "{}"])
print(rst)

rst = subprocess.check_output([CLIENT_PATH, 'createrawtransaction', "[[]]", "{}"])
print(rst)
"""

"""
print(CHECK_RAW_CREATE_TX("", 0, 0))
for i in range(1, 100):
    print(CHECK_RAW_CREATE_TX(StringGenerator('[\p]{1000}').render(), 0, 0))
"""