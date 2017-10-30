from utils import xbridge_utils

from test_cases import xbridge_client_get_tx_info_test
from test_cases import xbridge_client_accept_tx_test
from test_cases import xbridge_client_canceltx_test
from test_cases import xbridge_client_createtx_test
from test_cases import xbridge_client_sequence_test

from rpc_test_cases import xbridge_rpc_accept_tx_test
from rpc_test_cases import xbridge_rpc_canceltx_test
from rpc_test_cases import xbridge_rpc_get_tx_info_test


"""             INSTRUCTIONS

    - DO NOT RUN FOR NOW. Very early code.

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


random_RPC_sequence(nb_of_runs=50000, data_nature=INVALID_DATA, char_min_size=10000, char_max_size=12000)
random_RPC_sequence(nb_of_runs=50000, data_nature=VALID_DATA)
random_RPC_sequence(nb_of_runs=50000, char_max_size=1000)


defined_order_RPC_sequence(nb_of_runs=30000, data_nature=INVALID_DATA, char_min_size=5000, char_max_size=12000)
defined_order_RPC_sequence(nb_of_runs=30000, data_nature=VALID_DATA)
defined_order_RPC_sequence(nb_of_runs=30000, char_max_size=1000)


dxCancel_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxCancel_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxCancel_RPC_sequence(nb_of_runs=20000, char_max_size=5000)


dxCreate_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxCreate_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxCreate_RPC_sequence(nb_of_runs=20000, char_max_size=5000)


dxAccept_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxAccept_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxAccept_RPC_sequence(nb_of_runs=20000, char_max_size=5000)


dxAccept_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxAccept_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxAccept_RPC_sequence(nb_of_runs=20000, char_max_size=5000)


dxGetTransactionInfo_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxGetTransactionInfo_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxGetTransactionInfo_RPC_sequence(nb_of_runs=20000, char_max_size=5000)



"""            
        *******************************************************************
        ******************   RPC UNIT TESTS LAUNCHERS    ******************
        *******************************************************************
"""

"""                 RPC DX_CANCEL_TX
"""

""" RUNS FINE
from rpc_test_cases.xbridge_rpc_canceltx_test import *
xbridge_rpc_canceltx_test.repeat_cancel_tx_unit_tests(4)
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

