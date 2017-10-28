import time
import random
from utils import xbridge_utils
from interface import xbridge_client


"""                       
        - RANDOM SEQUENCE 
        - VARIOUS CLIENT API CALLS
        - COMBINATIONS OF INVALID AND OUT-OF-BOUNDS DATA - VERY LONG CHARACTER CLASSES  
        - VALID DATA MAY OCCUR FOR SOME NUMERIC PARAMETERS BUT IT SHOULD BE RARE
        - GOAL HERE: STRESS TESTING
"""

# TODO: getservicenodelist
# TODO : CHECK_CREATE_TX
def test_random_sequence_long_inputs(nb_of_runs):    
    no_param_func_list = [xbridge_client.TIMED_CHECK_GET_TX_LIST, xbridge_client.TIMED_CHECK_GET_TX_HISTORY_LIST, xbridge_client.TIMED_CHECK_GET_CURRENCY_LIST]
    # These functions always have bad input
    invalid_usr_func_list = [xbridge_client.TIMED_CHECK_CANCEL_TX_LIST, xbridge_client.TIMED_CHECK_GET_TX_INFO, xbridge_client.TIMED_CHECK_ACCEPT_TX]
    raw_func_list = ["sendrawtransaction", "signrawtransaction", "getrawtransaction", "decoderawtransaction"]
    create_raw_tx_func_list = [xbridge_client.CREATE_RAW_TX]
    create_tx_func_list = [xbridge_client.CREATE_TX]
    func_list = [no_param_func_list, invalid_usr_func_list, raw_func_list, create_raw_tx_func_list, create_tx_func_list]
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    for j in range(10000, 10000+nb_of_runs):
        func_list = random.choice([no_param_func_list, invalid_usr_func_list, raw_func_list, create_raw_tx_func_list])
        if func_list == create_raw_tx_func_list:
            picked_func = "CREATE_RAW_TX"
            invalid_random_txid = xbridge_utils.generate_input_from_random_classes_combinations(j)
            vout_param = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999)
            address_amount_param = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999)
            ts = time.time()
            xbridge_client.CREATE_RAW_TX(invalid_random_txid, vout_param, address_amount_param)
            te = time.time()
            elapsed_Time = te - ts
        if func_list == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            elapsed_Time = picked_func()
        if func_list == invalid_usr_func_list:
            picked_func = random.choice(invalid_usr_func_list)
            elapsed_Time = picked_func(j)
        if func_list == raw_func_list:
            picked_func = random.choice(raw_func_list)
            garbage_input_str = xbridge_utils.generate_input_from_random_classes_combinations(j)
            elapsed_Time = xbridge_client.TIMED_GENERIC_RAW_TX(picked_func, garbage_input_str)
        print("run: %s - picked function : %s" % (str(j), picked_func))
        if elapsed_Time > 1.5:
                print("outlier - %s: %s - data: %s" % (str(elapsed_Time), picked_func, j) )
        total_elapsed_seconds += elapsed_Time
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_random_sequence_long_inputs.xlsx", time_distribution)


"""                       
        - THIS FUNCTION MAY LOOK THE PREVIOUS ONE, BUT IT IS NOT DOING THE SAME THING
        - RANDOM SEQUENCE 
        - PARAMETERS ARE MADE IN SUCH A WAY THAT I WILL RANDOMLY MIXES VALID / INVALID / OUT-OF-BOUNDS PARAMETERS
        - INPUT PARAMETERS MAY BE OF ANY SIZE
        - VARIOUS CLIENT API CALLS
"""
# TODO: getservicenodelist, ["getblockcount"]
def test_random_sequence_valid_invalid_inputs(nb_of_runs):    
    no_param_func_list = [xbridge_client.TIMED_CHECK_GET_TX_LIST, xbridge_client.TIMED_CHECK_GET_TX_HISTORY_LIST, xbridge_client.TIMED_CHECK_GET_CURRENCY_LIST]
    # These functions will be fed valid input
    valid_usr_func_list = [xbridge_client.CHECK_CANCEL_TX, xbridge_client.CHECK_GET_TX_INFO, xbridge_client.CHECK_ACCEPT_TX]
    # These functions will be with bad input
    invalid_usr_func_list = [xbridge_client.TIMED_CHECK_CANCEL_TX_LIST, xbridge_client.TIMED_CHECK_GET_TX_INFO, xbridge_client.TIMED_CHECK_ACCEPT_TX]
    raw_func_list = ["sendrawtransaction", "signrawtransaction", "getrawtransaction", "decoderawtransaction"]
    create_raw_tx_func_list = [xbridge_client.CREATE_RAW_TX]
    create_tx_func_list = [xbridge_client.CREATE_TX]
    func_list = [no_param_func_list, valid_usr_func_list, invalid_usr_func_list, raw_func_list, create_raw_tx_func_list, create_tx_func_list]
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    # At each run, generate a mix of valid / invalid / out-of-bounds data
    for j in range(1, nb_of_runs):
        func_list = random.choice([no_param_func_list, invalid_usr_func_list, raw_func_list, create_raw_tx_func_list])
        VALID_INVALID_PICK = random.choice(["valid", "invalid"])
        if func_list == create_raw_tx_func_list:
            picked_func = "CREATE_RAW_TX"
            if VALID_INVALID_PICK == "invalid":
                random_txid = xbridge_utils.generate_input_from_random_classes_combinations(1, 200)
                vout_param = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999)
                address_amount_param = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999)
            else:
                random_txid = xbridge_utils.generate_random_valid_txid()
                vout_param = xbridge_utils.generate_random_number(0.000000000000000000000000000000000000000000000000000000000000000000000001, 10000000)
                address_amount_param = xbridge_utils.generate_random_number(0.000000000000000000000000000000000000000000000000000000000000000000000001, 10000000)
            ts = time.time()
            xbridge_client.CREATE_RAW_TX(random_txid, vout_param, address_amount_param)
            te = time.time()
            elapsed_Time = te - ts
        if func_list == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            elapsed_Time = picked_func()
        if func_list == invalid_usr_func_list:
            picked_func = random.choice(invalid_usr_func_list)
            elapsed_Time = picked_func(j)
        # valid scenarios
        if func_list == valid_usr_func_list:
            picked_func = random.choice(valid_usr_func_list)
            random_txid = xbridge_utils.generate_random_valid_txid()
            if picked_func == xbridge_client.CHECK_ACCEPT_TX:
                random_src_Address = xbridge_utils.generate_random_valid_address()
                random_dest_Address = xbridge_utils.generate_random_valid_address()
                picked_func(random_txid, random_src_Address, random_dest_Address)
            else:
                picked_func(random_txid)
        # valid and invalid scenarios
        if func_list == raw_func_list:
            picked_func = random.choice(raw_func_list)
            if VALID_INVALID_PICK == "invalid":
                txid = xbridge_utils.generate_input_from_random_classes_combinations(1, 200)
            else:
                txid = xbridge_utils.generate_random_valid_txid()
            elapsed_Time = xbridge_client.TIMED_GENERIC_RAW_TX(picked_func, txid)
        print("run: %s - picked function : %s" % (str(j), picked_func))
        if elapsed_Time > 1.5:
                print("outlier - %s: %s - data: %s" % (str(elapsed_Time), picked_func, j) )
        total_elapsed_seconds += elapsed_Time
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_random_sequence_valid_invalid_inputs.xlsx", time_distribution)
    
    
"""                       
    ***  DEFINED SEQUENCE OF API CALLS ***
    ***  USER FACING APIS Only ***

"""

def test_defined_order_sequence():
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    for i in range(1, 2):
        for j in range(10000, 11000):
            print("#%s" % str(i))
            elapsed_Time = xbridge_client.TIMED_CHECK_CANCEL_TX_LIST(j)
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxCancel"}
            time_distribution.append(json_str)
            elapsed_Time = xbridge_client.TIMED_CHECK_GET_TX_LIST()
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxTransactionList"}
            time_distribution.append(json_str)
            elapsed_Time = xbridge_client.TIMED_CHECK_GET_TX_INFO(j)
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxTransactionInfo"}
            time_distribution.append(json_str)
            elapsed_Time = xbridge_client.TIMED_CHECK_GET_CURRENCY_LIST()
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxCurrencyList"}
            time_distribution.append(json_str)
            elapsed_Time = xbridge_client.TIMED_CHECK_ACCEPT_TX(j)
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxAcceptTransaction"}
            time_distribution.append(json_str)
            elapsed_Time = xbridge_client.TIMED_CHECK_GET_TX_HISTORY_LIST()
            total_elapsed_seconds += elapsed_Time
            json_str = {"time": elapsed_Time, "API": "dxTransactionHistory"}
            time_distribution.append(json_str)
    xbridge_utils.export_data("test_defined_order_sequence.xlsx", time_distribution)



