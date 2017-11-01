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

no_param_func_list = [xbridge_rpc.get_transaction_list, xbridge_rpc.get_transaction_history_list, xbridge_rpc.get_currency_list, xbridge_rpc.get_blockcount, xbridge_rpc.get_budget, xbridge_rpc.get_node_list]
txid_func_list = [xbridge_rpc.cancel_tx, xbridge_rpc.get_tx_info, xbridge_rpc.decode_raw_tx, xbridge_rpc.send_tx, xbridge_rpc.sign_tx]
    

def random_RPC_calls_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    global no_param_func_list
    global txid_func_list
    time_distribution = []
    # total_elapsed_seconds = 0
    elapsed_Time = 0
    run_count = 0
    while run_count < nb_of_runs:
        func_to_run = random.choice([no_param_func_list, txid_func_list, xbridge_rpc.create_tx, xbridge_rpc.accept_tx])
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        if func_to_run == xbridge_rpc.create_tx:
            picked_func = "create_tx"
            ts = time.time()
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run == xbridge_rpc.accept_tx:
            picked_func = "accept_tx"
            ts = time.time()
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            ts = time.time()
            picked_func()
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run == txid_func_list:
            picked_func = random.choice(txid_func_list)
            ts = time.time()
            picked_func(xbridge_utils.ca_random_tx_id)
            te = time.time()
            elapsed_Time = te - ts
        print("random_seq - picked function : %s" % (picked_func))
        # if elapsed_Time > 1.5:
        #    print("outlier - %s: %s - data: %s" % (str(elapsed_Time), picked_func, j) )
        run_count += 1
        # total_elapsed_seconds += elapsed_Time
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_rpc_random_sequence.xlsx", time_distribution)
    
    
"""                       
    ***  DEFINED SEQUENCE OF API CALLS ***
    ***  APIs ARE SELECTED SEQUENTIALLY FROM A LIST UNTIL WE REACH THE USER RUN COUNT PARAMETER ***

"""

def defined_order_RPC_calls_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    global no_param_func_list
    global txid_func_list
    merged_list = no_param_func_list.copy()
    merged_list.extend(txid_func_list)
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    run_count = 0
    while run_count < nb_of_runs:
        func_to_run = merged_list[run_count % len(merged_list)]
        print("defined order RPC sequence #%s" % str(func_to_run))
        if func_to_run == xbridge_rpc.create_tx:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)       
            ts = time.time()
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run == xbridge_rpc.accept_tx:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
            ts = time.time()
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run in no_param_func_list:
            ts = time.time()
            func_to_run()
            te = time.time()
            elapsed_Time = te - ts
        if func_to_run == txid_func_list:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
            ts = time.time()
            func_to_run(xbridge_utils.ca_random_tx_id)
            te = time.time()
            elapsed_Time = te - ts
        run_count += 1
        json_str = {"time": elapsed_Time, "API": str(func_to_run)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_rpc_defined_order_sequence.xlsx", time_distribution)



# random_RPC_calls_sequence(nb_of_runs=1000)
defined_order_RPC_calls_sequence(nb_of_runs=1000)