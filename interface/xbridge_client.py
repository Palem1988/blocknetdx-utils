import subprocess
import json
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


def TIMED_CHECK_ACCEPT_TX(j):
    garbage_input_str1 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str2 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str3 = xbridge_utils.generate_garbage_input(j)
    ts = time.time()
    CHECK_ACCEPT_TX(garbage_input_str1, garbage_input_str2, garbage_input_str3)
    # assert type(CHECK_ACCEPT_TX(garbage_input_str1, garbage_input_str2, garbage_input_str3)) == None
    te = time.time()
    return te - ts


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


def CHECK_CREATE_TX(src_Address, src_Curr, src_Qty, dest_Address, dest_Curr, dest_Qty):
    try:
        rst = subprocess.check_output([CLIENT_PATH, 'dxCreateTransaction', src_Address, src_Curr, src_Qty, dest_Address, dest_Curr, dest_Qty])
        return rst
    except:
        pass


def TIMED_CHECK_CREATE_TX(j):
    garbage_input_str1 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str2 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str3 = xbridge_utils.generate_garbage_input(j)
    garbage_input_str4 = xbridge_utils.generate_garbage_input(j)
    source_nb = xbridge_utils.generate_random_number(-9999999999999, 999999999999)
    dest_nb = xbridge_utils.generate_random_number(-9999999999999, 999999999999)
    ts = time.time()
    CHECK_CREATE_TX(garbage_input_str1, garbage_input_str2, source_nb, garbage_input_str3, garbage_input_str4, dest_nb)
    te = time.time()
    return te - ts


def GENERIC_RAW_TX(raw_cmd, param):
    try:
        rst = subprocess.check_output([CLIENT_PATH, raw_cmd, param])
        return rst
    except:
        pass


def TIMED_GENERIC_RAW_TX(raw_cmd, param):
    try:
        ts = time.time()
        rst = subprocess.check_output([CLIENT_PATH, raw_cmd, param])
        te = time.time()
        return te - ts
    except:
        pass


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
