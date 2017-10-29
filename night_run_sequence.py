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

"""                 CLIENT DX_GET_TRANSACTION_INFO
"""


""" RUNS FINE

xbridge_client_get_tx_info_test.test_get_tx_info_load_v1(5)
xbridge_client_get_tx_info_test.test_get_tx_info_load_v2(5)
xbridge_client_get_tx_info_test.test_get_tx_info_load_v3(5)
xbridge_client_get_tx_info_test.repeat_tx_info_unit_tests(2)

"""

"""                 RPC DX_GET_TRANSACTION_INFO
"""

""" RUNS FINE
xbridge_rpc_get_tx_info_test.test_get_tx_info_load_v1(5)
xbridge_rpc_get_tx_info_test.test_get_tx_info_load_v2(5)
from rpc_test_cases.xbridge_rpc_get_tx_info_test import *
xbridge_rpc_get_tx_info_test.repeat_tx_info_unit_tests(2)
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

"""                 RPC DX_CANCEL_TX
"""

""" RUNS FINE
xbridge_rpc_canceltx_test.test_cancel_load_v1(5)
xbridge_rpc_canceltx_test.test_cancel_load_v2(5)
xbridge_rpc_canceltx_test.test_cancel_load_v3(5)
from rpc_test_cases.xbridge_rpc_canceltx_test import *
xbridge_rpc_canceltx_test.repeat_cancel_tx_unit_tests(4)
"""


""" RUNS FINE
xbridge_client_sequence_test.test_random_sequence_valid_invalid_inputs(10)
xbridge_client_sequence_test.test_random_sequence_long_inputs(10)
"""

