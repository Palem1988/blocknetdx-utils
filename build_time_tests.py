import unittest
import argparse

from utils import xbridge_utils
from interface import xbridge_rpc
import xbridge_logger
import xbridge_config

from rpc_test_cases import xbridge_rpc_accept_tx_test
from rpc_test_cases import xbridge_rpc_canceltx_test
from rpc_test_cases import xbridge_rpc_get_tx_info_test
from rpc_test_cases import xbridge_rpc_createtx_test
from rpc_test_cases import xbridge_rpc_market_orders_test
from rpc_test_cases import xbridge_rpc_heavy_polling_test
from rpc_test_cases import xbridge_rpc_sequence_test
from rpc_test_cases import xbridge_rpc_misc_test

from rpc_test_cases import xbridge_rpc_signtx_test
from rpc_test_cases import xbridge_rpc_sendtx_test

from rpc_test_cases import xbridge_rpc_blockchain_test
from rpc_test_cases import xbridge_rpc_blocknetdx_test
from rpc_test_cases import xbridge_rpc_network_test
from rpc_test_cases import xbridge_rpc_wallet_list_test
from rpc_test_cases import xbridge_rpc_wallet_set_test
from rpc_test_cases import xbridge_rpc_mining_test

"""
from test_cases import xbridge_client_get_tx_info_test
from test_cases import xbridge_client_accept_tx_test
from test_cases import xbridge_client_canceltx_test
from test_cases import xbridge_client_createtx_test
from test_cases import xbridge_client_sequence_test
"""

"""            
        *****************************************************************************************
        ******************************  SPECIFY THE OPTIONS HERE    *****************************
        *****************************************************************************************
"""

NUMBER_OF_WANTED_RUNS = 0
UNIT_TESTS_NB_OF_RUNS = 0

NUMBER_OF_WANTED_RUNS = xbridge_config.get_conf_sequence_run_number()
UNIT_TESTS_NB_OF_RUNS = xbridge_config.get_conf_unit_tests_run_number()

parser = argparse.ArgumentParser(description='API testing')
parser.add_argument('-s','--sequence', type=int, help='Number of sequence tests run')
parser.add_argument('-u','--unittest', type=int, help='Number of unit tests to run')

args = parser.parse_args()

if args.sequence is not None:
    NUMBER_OF_WANTED_RUNS = args.sequence

if args.unittest is not None:
    UNIT_TESTS_NB_OF_RUNS = args.unittest

"""            
        *****************************************************************************************
        ******************  SPECIFY HERE THE LIST RPC SEQUENCE TESTS TO RUN    ******************
        *****************************************************************************************
"""

# When data_nature is not specified, this will generate both valid and invalid data.

xbridge_rpc_sequence_test.random_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=10000, char_max_size=12000)
xbridge_rpc_sequence_test.random_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_sequence_test.random_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=1000)


xbridge_rpc_sequence_test.defined_order_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=5000, char_max_size=12000)
xbridge_rpc_sequence_test.defined_order_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_sequence_test.defined_order_RPC_calls_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=1000)


xbridge_rpc_canceltx_test.dxCancel_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_canceltx_test.dxCancel_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_canceltx_test.dxCancel_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_createtx_test.dxCreate_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_createtx_test.dxCreate_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_createtx_test.dxCreate_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_accept_tx_test.dxAccept_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_accept_tx_test.dxAccept_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_accept_tx_test.dxAccept_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_get_tx_info_test.dxGetTransactionInfo_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_get_tx_info_test.dxGetTransactionInfo_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_get_tx_info_test.dxGetTransactionInfo_RPC_sequence(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_heavy_polling_test.random_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_heavy_polling_test.random_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_heavy_polling_test.random_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_heavy_polling_test.defined_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_heavy_polling_test.defined_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_heavy_polling_test.defined_seq_polling_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_market_orders_test.random_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_market_orders_test.random_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_market_orders_test.random_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


xbridge_rpc_market_orders_test.defined_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=15000)
xbridge_rpc_market_orders_test.defined_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, data_nature=xbridge_utils.VALID_DATA)
xbridge_rpc_market_orders_test.defined_seq_market_actions_rpc_calls(nb_of_runs=NUMBER_OF_WANTED_RUNS, char_max_size=5000)


if NUMBER_OF_WANTED_RUNS > 0:
    xbridge_logger.logger.info('')
    print("******** Sequence tests are done ********")
    xbridge_utils.export_Full_Excel_Log()
    print("*****************************************")


"""            
        *****************************************************************************************
        ********************  SPECIFY HERE THE LIST RPC UNITS TESTS TO RUN    *******************
        *****************************************************************************************
"""

if UNIT_TESTS_NB_OF_RUNS < 1:
    xbridge_logger.logger.info('')
    print("No unit tests to run")
    exit(0)

xbridge_logger.logger.info('')
xbridge_logger.logger.info('Starting unit tests with version %s', str(xbridge_rpc.get_core_version()))

unit_tests_module_strings = [xbridge_rpc_createtx_test,
                             xbridge_rpc_canceltx_test,
                             xbridge_rpc_accept_tx_test,
                             xbridge_rpc_get_tx_info_test,
                             xbridge_rpc_misc_test,
                            xbridge_rpc_signtx_test,
                            xbridge_rpc_sendtx_test,
                            xbridge_rpc_blockchain_test,
                             xbridge_rpc_blocknetdx_test,
                             xbridge_rpc_network_test,
                            xbridge_rpc_wallet_list_test,
                             xbridge_rpc_wallet_set_test,
                            xbridge_rpc_mining_test
                             ]


for i in range(1, 1 + UNIT_TESTS_NB_OF_RUNS):
    suites = [unittest.TestLoader().loadTestsFromModule(modul) for modul in unit_tests_module_strings]
    test_suite = unittest.TestSuite(suites)
    testResult = unittest.TextTestRunner(verbosity=2).run(test_suite)

xbridge_logger.logger.info('')
xbridge_logger.logger.info('Unit tests are done !')

# xbridge_logger.logger.info('----------------------------------------------------------------------------------------------------------------------------------------------------------')
# xbridge_logger.logger.info('wasSuccessful: %s - testRuns: %s - Failures: %s - Errors: %s' % (str(testResult.wasSuccessful), str(testResult.testsRun), str(testResult.failures), str(testResult.errors)))
