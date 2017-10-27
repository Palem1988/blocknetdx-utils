import unittest
import time
import sys

from interface import xbridge_client
from utils import xbridge_utils

from strgen import StringGenerator


'''                       ***  PRELIMINARY REMARKS ***

    - Only dxGetTransactionInfo is tested here.

    - The number of wanted runs has to be changed in the functions.

    - Python 3.6 is used. Untested on Python 2.7.
'''

"""
    - Here, the length of the garbage data is very high and increased.
    The "j" parameter in the "generate_garbage_input" function is the length of the garbage input we want.

    - export_data() function generates :
        1) an Excel File with the recorded timing information.
        2) a small descriptive table with mean, standard deviation, and some quantiles (25%, 50%, 75%).

"""
def test_get_tx_info_load_v1(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    end_run = 10000+nb_of_runs
    for j in range(10000, end_run):
        garbage_input_str = xbridge_utils.generate_garbage_input(j)
        ts = time.time()
        assert type(xbridge_client.CHECK_GET_TX_INFO(garbage_input_str)) == list
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxGetTxInfo"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_info_load_v1.xlsx", time_distribution)


"""
    - Here, the length of garbage parameters is random.
"""
def test_get_tx_info_load_v2(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        garbage_input_str = xbridge_utils.generate_garbage_input(int(xbridge_utils.generate_random_number(1, 10000)))
        ts = time.time()
        assert type(xbridge_client.CHECK_GET_TX_INFO(garbage_input_str)) == list
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxGetTxInfo"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_info_load_v2.xlsx", time_distribution)


"""
    - Here, The length of the random parameter is kept fixed, we just increase the number of iterations ==> Pure load test, when resources are available.
"""
def test_get_tx_info_load_v3(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        garbage_input_str = xbridge_utils.generate_garbage_input(64)
        ts = time.time()
        assert type(xbridge_client.CHECK_GET_TX_INFO(garbage_input_str)) == list
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxGetTxInfo"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_get_tx_info_load_v3.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

    - Assertions currently take the following form ==> self.assertIsInstance(..., dict).
    More precise assertions may have to be written, when we have real data.

    - We test many combinations. But additional scenarios may have to be added.

"""

class get_Tx_Info_UnitTest(unittest.TestCase):
    def setUp(self):
        self.random_length_str_with_random_char_class = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)
    
    """
            - Basic tests
    """
    def test_invalid_get_tx_info_1(self):
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(" "), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(""), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO("[]"), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO("{}"), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO("''"), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO("'"), list)
    
    """
          - Character classes are chosen randomly
          - Size of the input parameter is chosen randomly too.
    """
    def test_invalid_get_tx_info_2(self):
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(self.random_length_str_with_random_char_class), list)
                
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def invalid_get_tx_info_test_3(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a]{64}').render()), list)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\w]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s]{64}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\p]{64}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{64}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\w\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\s]{64}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\W\w\h\a]{64}').render()), dict)


    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def invalid_get_tx_info_test_4(self):
       # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\w]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s]{9000:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\p]{9000:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\w\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\s]{9000:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\W\w\h\a]{9000:11000}').render()), dict)


    """
          - Same as before, but now the random input parameters are of random length [1-11 000]
    """
    def invalid_get_tx_info_test_5(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\w]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s]{1:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\s\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\W\p]{1:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\w\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\a\s]{1:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_GET_TX_INFO(StringGenerator('[\p\d\W\w\h\a]{1:11000}').render()), dict)


def repeat_tx_info_unit_tests(nb_of_runs):
    for i in (1, nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

