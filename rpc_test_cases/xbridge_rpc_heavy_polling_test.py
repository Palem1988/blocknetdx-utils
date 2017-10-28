import time

from utils import xbridge_utils
from interface import xbridge_rpc


"""
    - WE WANT TO TEST SCENARIOS IN WHICH USERS POLL CONSTANTLY THE DX TO GET INFORMATION.
    - SO WE FOCUS ON GET_TX_LIST + GET_TRANSACTION_HISTORY + CHECK_GET_CURRENCY_LIST
    - THIS TEST WILL HAVE TO BE COMPLETED WITH THE APIs THAT ALLOW TO GET THE ORDERBOOK
    
    SCENARIOS GROUPS THAT ARE TESTED HERE:
    - ORDERED SEQUENCE
    - UNORDERED RANDOM SEQUENCE
    - SINGLE APLI SEQUENCE
    
"""


"""
    - DEFINED SEQUENCE OF API CALLS TO GET INFORMATION - NO MARKET ACTIONS
    - GET_TX_LIST + GET_TRANSACTION_HISTORY
    - ORDERED API CALL SEQUENCE
"""
def defined_seq_get_info_api_calls(nb_of_runs):
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
    xbridge_utils.export_data("defined_seq_get_info_rpc_calls.xlsx", time_distribution)


"""                       
    ***  GET_TRANSACTION_LIST ONLY ***
"""

def test_get_tx_list_load(nb_of_runs):
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

def test_get_tx_history_load(nb_of_runs):
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

def test_get_currency_list_load(nb_of_runs):
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

