import time
import random
from utils import xbridge_utils
import unittest
from utils import xbridge_ref

from interface import xbridge_rpc

from rpc_test_cases import xbridge_rpc_misc_test

# Lists of function that will be run in an ordered or random way
no_param_func_list = [xbridge_rpc.rpc_connection.getpeerinfo,
                      xbridge_rpc.rpc_connection.listlockunspent,
                      xbridge_rpc.rpc_connection.listaddressgroupings,
                      xbridge_rpc.rpc_connection.listaccounts,
                      xbridge_rpc.get_core_version,
                      xbridge_rpc.get_transaction_list,
                      xbridge_rpc.get_transaction_history_list,
                      xbridge_rpc.get_currency_list,
                      xbridge_rpc.get_blockcount,
                      xbridge_rpc.get_budget,
                      xbridge_rpc.get_node_list,
                      xbridge_rpc.rpc_connection.getnettotals,
                      xbridge_rpc.rpc_connection.getnetworkinfo,
                      xbridge_rpc.rpc_connection.getstakingstatus,
                      xbridge_rpc.rpc_connection.getwalletinfo,
                      xbridge_rpc.rpc_connection.ping,
                      xbridge_rpc.rpc_connection.keypoolrefill
                      ]

txid_func_list = [xbridge_rpc.cancel_tx, xbridge_rpc.get_tx_info,
                  xbridge_rpc.decode_raw_tx,
                  xbridge_rpc.send_tx,
                  xbridge_rpc.sign_tx,
                  xbridge_rpc.rpc_connection.listsinceblock
                  ]

list_of_tests = []

test_suite = unittest.TestSuite()
testloader = unittest.TestLoader()
for class_name in xbridge_ref.unit_tests_class_names:
    # print(test._tests)
    testnames = testloader.getTestCaseNames(class_name)
    # print(len(testnames))
    for name in testnames:
      ## suite.addTest(testcase_klass(name, param=param))
      # print(name)
      list_of_tests.append((class_name, name))


def build_random_sequence(nb_of_runs=10):
    global list_of_tests
    suite = unittest.TestSuite()
    selected_Tests = []
    for i in range(1, 1+nb_of_runs):
        selected_Test = random.choice(list_of_tests)
        print(selected_Test)
        selected_Tests.append(selected_Test)
    return selected_Tests


def test_random_UT_sequence(nb_of_runs=10, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    elapsed_Time = 0
    run_count = 0
    # print("API call order will be random. Number of runs: %s" % (str(nb_of_runs)))
    selected_Tests = build_random_sequence(nb_of_runs)
    for selected_Test in selected_Tests:
        te = 0
        ts = 0
        suite = unittest.TestSuite()
        suite.addTest(selected_Test[0](selected_Test[1]))
        ts = time.time()
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        # sys.exit(not result.wasSuccessful())
        te = time.time()
        elapsed_Time = te - ts
        print("Random sequence test - %s (%s secs)" % (str(selected_Test[1]), str(elapsed_Time)))
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "random_sequence", "API": str(selected_Test[1]), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        # if elapsed_Time > 1.5:
        #    print("outlier - %s: %s - data: %s" % (str(elapsed_Time), selected_Test, j) )
        run_count += 1
        json_str = {"time": elapsed_Time, "API": str(selected_Test)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_RPC_calls_sequence.xlsx", time_distribution)


def random_RPC_calls_sequence(nb_of_runs=100, data_nature=3, char_min_size=1, char_max_size=12000):
    global no_param_func_list
    global txid_func_list
    time_distribution = []
    elapsed_Time = 0
    run_count = 0
    # print("API call order will be random. Number of runs: %s" % (str(nb_of_runs)))
    while run_count < nb_of_runs:
        te = 0
        ts = 0
        func_to_run = random.choice([no_param_func_list, txid_func_list, xbridge_rpc.create_tx, xbridge_rpc.accept_tx])
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        if func_to_run == xbridge_rpc.create_tx:
            picked_func = "create_Transaction"
            ts = time.time()
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            te = time.time()
        if func_to_run == xbridge_rpc.accept_tx:
            picked_func = "accept_Transaction"
            ts = time.time()
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            te = time.time()
        if func_to_run == no_param_func_list:
            picked_func = random.choice(no_param_func_list)
            ts = time.time()
            picked_func()
            te = time.time()
        if func_to_run == txid_func_list:
            picked_func = random.choice(txid_func_list)
            ts = time.time()
            picked_func(xbridge_utils.ca_random_tx_id)
            te = time.time()
        elapsed_Time = te - ts
        print("Random sequence test - %s (%s secs)" % (str(picked_func), str(elapsed_Time)))
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "random_sequence", "API": str(picked_func), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        # if elapsed_Time > 1.5:
        #    print("outlier - %s: %s - data: %s" % (str(elapsed_Time), picked_func, j) )
        run_count += 1
        # total_elapsed_seconds += elapsed_Time
        json_str = {"time": elapsed_Time, "API": str(picked_func)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_RPC_calls_sequence.xlsx", time_distribution)
    
    
"""                       
    ***  DEFINED SEQUENCE OF API CALLS ***
    ***  APIs ARE SELECTED SEQUENTIALLY FROM A LIST UNTIL WE REACH THE USER RUN COUNT PARAMETER ***

"""

def defined_order_RPC_calls_sequence(nb_of_runs=100, data_nature=3, char_min_size=1, char_max_size=12000):
    global no_param_func_list
    global txid_func_list
    merged_list = no_param_func_list.copy()
    merged_list.extend(txid_func_list)
    time_distribution = []
    total_elapsed_seconds = 0
    elapsed_Time = 0
    run_count = 0
    # print("API calls will be made in turn...Number of runs: %s" % (str(nb_of_runs)))
    while run_count < nb_of_runs:
        ts = 0
        te = 0
        func_to_run = merged_list[run_count % len(merged_list)]
        if func_to_run == xbridge_rpc.create_tx:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)       
            ts = time.time()
            xbridge_rpc.create_tx(xbridge_utils.c_src_Address, xbridge_utils.c_src_Token, xbridge_utils.source_nb, xbridge_utils.c_dest_Address, xbridge_utils.c_dest_Token, xbridge_utils.dest_nb)
            te = time.time()
        if func_to_run == xbridge_rpc.accept_tx:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
            ts = time.time()
            xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
            te = time.time()
        if func_to_run in no_param_func_list:
            ts = time.time()
            func_to_run()
            te = time.time()
        if func_to_run == txid_func_list:
            xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
            ts = time.time()
            func_to_run(xbridge_utils.ca_random_tx_id)
            te = time.time()
        elapsed_Time = te - ts
        print("Defined order sequence test - %s (%s secs)" % (str(func_to_run), str(elapsed_Time)))
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "defined_order_sequence", "API": str(func_to_run), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        run_count += 1
        json_str = {"time": elapsed_Time, "API": str(func_to_run)}
        time_distribution.append(json_str)
    xbridge_utils.export_data("defined_order_RPC_calls_sequence.xlsx", time_distribution)

# random_RPC_calls_sequence(nb_of_runs=1000)
# defined_order_RPC_calls_sequence(nb_of_runs=50)

# test_random_UT_sequence()
