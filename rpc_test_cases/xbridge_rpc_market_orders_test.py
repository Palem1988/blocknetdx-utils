import time
import random
from utils import xbridge_utils
from interface import xbridge_rpc

"""
        - UNORDERED + ORDERED SEQUENCE OF MARKET ACTIONS
        - CANCELTX + ACCEPT_TX + CREATE_TX
"""


"""
        - RANDOM SEQUENCE
"""

def random_seq_market_actions_rpc_calls(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        func_list = [xbridge_rpc.create_tx, xbridge_rpc.accept_tx, xbridge_rpc.cancel_tx]
        selected_func = random.choice(func_list)
        func_str = ""
        ts = time.time()
        if selected_func == xbridge_rpc.create_tx:
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            func_str = "create_tx"
        if selected_func == xbridge_rpc.accept_tx:
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            func_str = "accept_tx"
        if selected_func == xbridge_rpc.cancel_tx:
            xbridge_rpc.cancel_tx(xbridge_utils.ca_random_tx_id)
            func_str = "cancel_tx"
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": func_str}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_market_actions_RPC_sequence.xlsx", time_distribution)


"""
        ***  ORDERED SEQUENCE OF MARKET ACTIONS ***
        ***  APIs ARE SELECTED SEQUENTIALLY FROM A LIST UNTIL WE REACH THE USER RUN COUNT PARAMETER ***
"""

def defined_seq_market_actions_rpc_calls(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        func_str = ""
        ts = time.time()
        if i % 3 == 0:
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            func_str = "create_tx"
        if i % 3 == 1:
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            func_str = "accept_tx"
        if i % 3 == 2:
            xbridge_rpc.cancel_tx(xbridge_utils.ca_random_tx_id)
            func_str = "cancel_tx"
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": func_str}
        time_distribution.append(json_str)
    xbridge_utils.export_data("defined_market_actions_RPC_sequence.xlsx", time_distribution)

