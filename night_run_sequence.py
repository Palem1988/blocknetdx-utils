import unittest
import io

from utils import xbridge_utils

from test_cases import xbridge_client_get_tx_info_test
from test_cases import xbridge_client_accept_tx_test
from test_cases import xbridge_client_canceltx_test
from test_cases import xbridge_client_createtx_test
from test_cases import xbridge_client_sequence_test

from rpc_test_cases import xbridge_rpc_accept_tx_test
from rpc_test_cases import xbridge_rpc_canceltx_test
from rpc_test_cases import xbridge_rpc_get_tx_info_test
from rpc_test_cases import xbridge_rpc_createtx_test
from rpc_test_cases import xbridge_rpc_market_orders_test
from rpc_test_cases import xbridge_rpc_heavy_polling_test
from rpc_test_cases import xbridge_rpc_sequence_test


"""             INSTRUCTIONS

    - All tests can be run from there.

    - Uncomment the test you want to run.
    
    - Adjust the number of runs you want.

    - Except for unit tests, all tests output an Excel file in the current directory with
    the timing distribution.

    - The higher the number of runs, the more robust the testing.

"""


"""            
        *************************************************************
        ******************   RPC SEQUENCE TESTS    ******************
        *************************************************************
"""

# When data_nature is not specified, this will generate both valid and invalid data.

NUMBER_OF_WANTED_RUNS = 0

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



"""            
        *******************************************************************
        ******************   RPC UNIT TESTS LAUNCHERS    ******************
        *******************************************************************
"""

"""                 RPC DX_CANCEL_TX
"""

stream = io.StringIO()
runner = unittest.TextTestRunner(stream=stream)
full_Test_Suite = unittest.TestSuite()

for i in range(1,3):
    full_Test_Suite.addTest(xbridge_rpc_canceltx_test.cancel_UnitTest())
    full_Test_Suite.addTest(xbridge_rpc_get_tx_info_test.get_Tx_Info_UnitTest())

testResult = runner.run(full_Test_Suite)
xbridge_utils.logger.info('wasSuccessful: %s - testRuns: %s - Failures: %s - Errors: %s', % (str(testResult.wasSuccessful), str(testResult.testsRun), str(testResult.failures), str(testResult.errors))


"""
stream.seek(0)
print('Test output\n', stream.read())
"""



"""                 RPC DX_GET_TRANSACTION_INFO
"""

""" RUNS FINE
from rpc_test_cases.xbridge_rpc_get_tx_info_test import *
xbridge_rpc_get_tx_info_test.repeat_tx_info_unit_tests(2)
"""


""" TESTME
from rpc_test_cases.xbridge_rpc_get_createtx_test import *
xbridge_rpc_get_createtx_test.repeat_tx_info_unit_tests(2)
"""



"""            
        *******************************************************************
        **********************   CLIENT LAUNCHERS    **********************
        *******************************************************************
"""



"""             INSTRUCTIONS

    - DO NOT RUN FOR NOW.

"""


"""                 CLIENT DX_GET_TRANSACTION_INFO
"""


""" RUNS FINE

xbridge_client_get_tx_info_test.test_get_tx_info_load_v1(5)
xbridge_client_get_tx_info_test.test_get_tx_info_load_v2(5)
xbridge_client_get_tx_info_test.test_get_tx_info_load_v3(5)
xbridge_client_get_tx_info_test.repeat_tx_info_unit_tests(2)

"""


""" RUNS FINE

xbridge_client_createtx_test.test_createtx_garbage_load_v1(5)
xbridge_client_createtx_test.test_createtx_garbage_load_v2(5)
xbridge_client_createtx_test.test_createtx_valid_load(5)
# Unit tests
xbridge_client_createtx_test.repeat_create_tx_unit_tests(5)
"""


""" RUNS FINE

xbridge_client_accept_tx_test.test_accept_garbage_load_v1(5)
xbridge_client_accept_tx_test.test_accept_garbage_load_v2(5)
xbridge_client_accept_tx_test.test_accept_valid_load(5)
# Unit tests
xbridge_client_accept_tx_test.repeat_accept_tx_unit_tests(5)
"""

"""                 CLIENT DX_CANCEL_TX

"""


""" RUNS FINE
xbridge_client_canceltx_test.test_cancel_load_v1(5)
xbridge_client_canceltx_test.test_cancel_load_v2(5)
xbridge_client_canceltx_test.test_cancel_load_v3(5)
# Unit tests
from test_cases.xbridge_client_canceltx_test import *
# unittest.main()
xbridge_client_canceltx_test.repeat_cancel_tx_unit_tests(3)
"""

