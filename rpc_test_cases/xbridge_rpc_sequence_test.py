import time
import random
from utils import xbridge_utils
from interface import xbridge_rpc


"""                       
        - RANDOM SEQUENCE 
        - INPUT PARAMETERS MAY BE OF ANY SIZE
        - VARIOUS RPC CALLS
        - THE LIST OF RPC CALLS CAN BE EASILY ADJUSTED IF NECESSARY
"""

# TODO: getservicenodelist
def test_random_sequence_(nb_of_runs, data_nature, char_min_size, char_max_size):
    no_param_func_list = [xbridge_rpc.get_transaction_list, xbridge_rpc.get_transaction_history_list, xbridge_rpc.get_currency_list, xbridge_rpc.getblockcount]
    txid_func_list = [xbridge_rpc.cancel_tx, xbridge_rpc.get_tx_info, xbridge_rpc.decode_raw_tx, xbridge_rpc.send_tx, xbridge_rpc.sign_tx]
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    for j in range(1, nb_of_runs):
        func_list = random.choice([no_param_func_list, txid_func_list, xbridge_rpc.create_tx, xbridge_rpc.accept_tx])
        xbridge_utils.generate_new_set_of_data(data_nature)
        if func_list == xbridge_rpc.create_tx:
            picked_func = "create_tx"
            ts = time.time()
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            te = time.time()
            elapsed_Time = te - ts
        if func_list == xbridge_rpc.accept_tx:
            picked_func = "accept_tx"
            ts = time.time()
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            te = time.time()
            elapsed_Time = te - ts
        if func_list == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            ts = time.time()
            picked_func()
            te = time.time()
            elapsed_Time = te - ts
        if func_list == txid_func_list:
            picked_func = random.choice(txid_func_list)
            ts = time.time()
            picked_func(xbridge_utils.ca_random_tx_id)
            te = time.time()
            elapsed_Time = te - ts
        print("run: %s - picked function : %s" % (str(j), picked_func))
        if elapsed_Time > 1.5:
            print("outlier - %s: %s - data: %s" % (str(elapsed_Time), picked_func, j) )
        total_elapsed_seconds += elapsed_Time
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_rpc_random_sequence_valid_invalid_inputs.xlsx", time_distribution)
    
    
"""                       
    ***  DEFINED SEQUENCE OF API CALLS ***
    ***  USER FACING APIS Only ***

"""

def test_defined_order_sequence(nb_of_runs, data_nature):
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    for i in range(1, nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature)
        print("defined order RPC sequence #%s" % str(i))
        ts = time.time()
        xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb,
                              xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
        te = time.time()
        elapsed_Time = te - ts
        json_str = {"time": elapsed_Time, "API": "create_tx"}
        time_distribution.append(json_str)
        # accept_tx
        ts = time.time()
        xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
        te = time.time()
        elapsed_Time = te - ts
        json_str = {"time": elapsed_Time, "API": "create_tx"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_defined_order_sequence.xlsx", time_distribution)
