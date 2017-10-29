import time
import random

from utils import xbridge_utils
from interface import xbridge_rpc

"""
    - WE WANT TO TEST SCENARIOS IN WHICH USERS POLL CONSTANTLY THE DX TO GET INFORMATION.
    - SO WE FOCUS ON GET_TX_LIST + GET_TRANSACTION_HISTORY + CHECK_GET_CURRENCY_LIST
    - THIS TEST WILL HAVE TO BE COMPLETED WITH THE APIs THAT ALLOW TO GET THE ORDERBOOK
    
    SCENARIOS GROUPS THAT ARE TESTED HERE:
    - ORDERED SEQUENCE
    - UNORDERED RANDOM SEQUENCE
    - SINGLE RPC SEQUENCE
    
"""

"""
    - UNORDERED SEQUENCE OF RPC CALLS TO GET INFORMATION - NO MARKET ACTIONS
    - GET_TX_LIST + GET_TRANSACTION_HISTORY + GET_TX_INFO
"""

def random_seq_polling_rpc_calls(nb_of_runs=1000, data_nature=xbridge_utils.RANDOM_VALID_INVALID):
    time_distribution = []
    total_elapsed_seconds = 0
    no_param_func_list = [xbridge_rpc.get_transaction_list, xbridge_rpc.get_transaction_history_list,
                          xbridge_rpc.get_currency_list, xbridge_rpc.get_blockcount, xbridge_rpc.get_budget,
                          xbridge_rpc.get_node_list]
    for i in range(1, nb_of_runs):
        func_list = random.choice([no_param_func_list, xbridge_rpc.get_tx_info])
        # print("#%s" % str(i))
        func_str = ""
        if func_list == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            ts = time.time()
            picked_func()
            te = time.time()
            elapsed_Time = te - ts
        if func_list == xbridge_rpc.get_tx_info:
            xbridge_utils.generate_new_set_of_data(data_nature)
            picked_func = "get_tx_info"
            ts = time.time()
            xbridge_rpc.get_tx_info()
            te = time.time()
            elapsed_Time = te - ts
        total_elapsed_seconds += te - ts
        json_str = {"time": elapsed_Time, "API": picked_func}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_seq_polling_rpc_calls.xlsx", time_distribution)


"""
    - DEFINED SEQUENCE OF RPC CALLS TO GET INFORMATION - NO MARKET ACTIONS
    - GET_TX_LIST + GET_TRANSACTION_HISTORY
"""

def defined_seq_polling_rpc_calls(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        # print("#%s" % str(i))
        func_str = ""
        ts = time.time()
        if i % 2 == 0:
            xbridge_rpc.get_transaction_list()
            func_str = "get_transaction_list"
        else:
            xbridge_rpc.get_transaction_history_list()
            func_str = "get_transaction_history_list"
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": func_str}
        time_distribution.append(json_str)
    xbridge_utils.export_data("defined_seq_polling_rpc_calls.xlsx", time_distribution)


"""                       
    ***  GET_TRANSACTION_LIST ONLY ***
"""

def test_get_tx_list_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        # print("#%s" % str(i))
        ts = time.time()
        xbridge_rpc.get_transaction_list()
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "get_tx_list"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_list_rpc_load.xlsx", time_distribution)


"""                       
    ***  GET_TRANSACTION_HISTORY ONLY ***
"""

def test_get_tx_history_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        # print("#%s" % str(i))
        ts = time.time()
        xbridge_rpc.get_transaction_history_list()
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "get_tx_history"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_history_rpc_load.xlsx", time_distribution)


"""                       
    ***  GET_CURRENCY_LIST ONLY ***
"""

def test_get_currency_list_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        # print("#%s" % str(i))
        ts = time.time()
        xbridge_rpc.get_currency_list()
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "get_currency_list"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_currency_list_rpc_load.xlsx", time_distribution)

