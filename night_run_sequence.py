from utils import xbridge_utils

from test_cases import xbridge_client_get_tx_info_test
from test_cases import xbridge_client_accept_tx_test
from test_cases import xbridge_client_canceltx_test
from test_cases import xbridge_client_createtx_test


"""             INSTRUCTIONS

    - DO NOT RUN FOR NOW. Very early code.

    - All tests can be run from there.

    - Uncomment the test you want to run.
    
    - Adjust the number of runs you want.

    - Except for unit tests, all tests output an Excel file in the current directory with
    the timing distribution.

    - The higher the number of runs, the more robust the testing.

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

"""
xbridge_client_canceltx_test.test_cancel_load_v1(5)
xbridge_client_canceltx_test.test_cancel_load_v2(5)
xbridge_client_canceltx_test.test_cancel_load_v3(5)
"""
# Unit tests
from test_cases.xbridge_client_canceltx_test import *
# unittest.main()
xbridge_client_canceltx_test.repeat_cancel_tx_unit_tests(3)

