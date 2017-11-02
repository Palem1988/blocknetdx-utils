import time
import random

from utils import xbridge_utils
from interface import xbridge_rpc

"""
    - WE WANT TO TEST SCENARIOS IN WHICH USERS POLL CONSTANTLY THE DX TO GET INFORMATION.
    - THIS TEST WILL HAVE TO BE COMPLETED WITH THE APIs THAT ALLOW TO GET THE ORDERBOOK
    
"""

"""
    - UNORDERED SEQUENCE OF RPC CALLS TO GET INFORMATION - NO MARKET ACTIONS
    - GET_TX_LIST + GET_TRANSACTION_HISTORY + GET_TX_INFO
"""

def random_seq_polling_rpc_calls(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    no_param_func_list = [xbridge_rpc.get_transaction_list, xbridge_rpc.get_transaction_history_list,
                          xbridge_rpc.get_currency_list, xbridge_rpc.get_blockcount, xbridge_rpc.get_budget,
                          xbridge_rpc.get_node_list]
    for i in range(1, 1 + nb_of_runs):
        te = 0
        ts = 0
        func_list = random.choice([no_param_func_list, xbridge_rpc.get_tx_info])
        if func_list == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            ts = time.time()
            picked_func()
            te = time.time()
        if func_list == xbridge_rpc.get_tx_info:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
            picked_func = "get_tx_info"
            ts = time.time()
            xbridge_rpc.get_tx_info(xbridge_utils.ca_random_tx_id)
            te = time.time()
        elapsed_Time = te - ts
        print("Random sequence polling test - %s (%s secs)" % (str(picked_func), str(elapsed_Time)))
        full_json_str = {version: xbridge_rpc.get_core_version(), sequence: "random_polling_sequence", "API": str(picked_func), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_seq_polling_rpc_calls.xlsx", time_distribution)


"""
    - ALTERNATING SEQUENCE OF GET_TX_LIST + GET_TRANSACTION_HISTORY
"""

def defined_seq_polling_rpc_calls(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        te = 0
        ts = 0
        func_str = ""
        ts = time.time()
        if i % 2 == 0:
            xbridge_rpc.get_transaction_list()
            func_str = "get_TX_list"
        else:
            xbridge_rpc.get_transaction_history_list()
            func_str = "get_TX_History_List"
        te = time.time()
        elapsed_Time = te - ts
        print("Defined sequence polling test - %s (%s secs)" % (str(func_str), str(elapsed_Time)))
        full_json_str = {version: xbridge_rpc.get_core_version(), sequence: "defined_polling_sequence", "API": str(picked_func), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        json_str = {"time": elapsed_Time, "API": str(func_str)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("defined_seq_polling_rpc_calls.xlsx", time_distribution)


"""                       
    ***  GET_TRANSACTION_LIST ONLY ***
"""

def test_get_tx_list_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        te = 0
        ts = 0
        ts = time.time()
        xbridge_rpc.get_transaction_list()
        te = time.time()
        elapsed_Time = te - ts
        print("get_transaction_list only sequence test - %s (%s secs)" % (str(func_str), str(elapsed_Time)))
        full_json_str = {version: xbridge_rpc.get_core_version(), sequence: "get_TX_List_sequence", "API": "get_transaction_list", "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        json_str = {"time": elapsed_Time, "API": "get_tx_list"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_list_rpc_load.xlsx", time_distribution)


"""                       
    ***  GET_TRANSACTION_HISTORY ONLY ***
"""

def test_get_tx_history_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        te = 0
        ts = 0
        ts = time.time()
        xbridge_rpc.get_transaction_history_list()
        te = time.time()
        elapsed_Time = te - ts
        print("get_tx_history_list only sequence test - %s (%s secs)" % (str(func_str), str(elapsed_Time)))
        json_str = {"time": te - ts, "API": "get_tx_history"}
        time_distribution.append(json_str)
        full_json_str = {version: xbridge_rpc.get_core_version(), sequence: "get_tx_history_list sequence", "API": str(picked_func), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("test_get_tx_history_rpc_load.xlsx", time_distribution)


"""                       
    ***  GET_CURRENCY_LIST ONLY ***
"""

def test_get_currency_list_load(nb_of_runs=1000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        te = 0
        ts = 0
        ts = time.time()
        xbridge_rpc.get_currency_list()
        te = time.time()
        elapsed_Time = te - ts
        print("get_currency_list only test - %s (%s secs)" % (str(func_str), str(elapsed_Time)))
        json_str = {"time": te - ts, "API": "get_currency_list"}
        time_distribution.append(json_str)
        full_json_str = {version: xbridge_rpc.get_core_version(), sequence: "get_currency_list sequence", "API": str(picked_func), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("test_get_currency_list_rpc_load.xlsx", time_distribution)

