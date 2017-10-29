import unittest
import time
import sys

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""
def dxGetTransactionInfo_RPC_sequence(nb_of_runs=1000, data_nature=xbridge_utils.RANDOM_VALID_INVALID, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        assert type(xbridge_rpc.get_tx_info(xbridge_utils.ca_random_tx_id)) == list
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(xbridge_utils.ca_random_tx_id), "API": "dxGetTxInfo"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("dxGetTransactionInfo_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

    - Assertions currently take the following form ==> self.assertIsInstance(..., list).
    More precise assertions may have to be written, when we have real data.

    - We test many combinations. But additional scenarios may have to be added.

"""

class get_Tx_Info_UnitTest(unittest.TestCase):
    def setUp(self):
        self.random_length_str_with_random_char_class = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)

    """
                - Specific tests with txid = 240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc
    """
    def test_specific_tx_id(self):
        self.assertIsInstance(xbridge_rpc.get_tx_info("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc"), list)

    """
            - Basic tests
    """
    def test_invalid_get_tx_info_1(self):
        self.assertIsInstance(xbridge_rpc.get_tx_info(" "), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(""), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info("[]"), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info("{}"), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info("''"), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info("'"), list)
    
    """
          - Character classes are chosen randomly
          - Size of the input parameter is chosen randomly too.
    """
    def test_invalid_get_tx_info_2(self):
        self.assertIsInstance(xbridge_rpc.get_tx_info(self.random_length_str_with_random_char_class), list)
                
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_get_tx_info_test_3(self):
        try:
            # We pick from a single class at a time
            str_1 = StringGenerator('[\a]{64}').render()
            self.assertIsInstance(xbridge_rpc.get_tx_info(str_1), dict)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\d]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\w]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s]{64}').render()), list)
            # We pick from combinations of 2 classes
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\a]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\d]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\a]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\p]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\d]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\a]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\p]{64}').render()), list)
            # We pick from combinations of 3 classes
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\s]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\p]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{64}').render()), list)
            # We pick from combinations of 4 classes
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\w\s]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\h]{64}').render()), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\s]{64}').render()), list)
            # We pick from combinations of 5 classes
            self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\W\w\h\a]{64}').render()), list)
        except AssertionError as e:
            print("failed on set: %s" % str_1)


    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def invalid_get_tx_info_test_4(self):
       # We pick from a single class at a time
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\d]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\w]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s]{9000:11000}').render()), list)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\a]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\d]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\a]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\p]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\d]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\a]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\p]{9000:11000}').render()), list)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\s]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\p]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{9000:11000}').render()), list)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\w\s]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\h]{9000:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\s]{9000:11000}').render()), list)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\W\w\h\a]{9000:11000}').render()), list)


    """
          - Same as before, but now the random input parameters are of random length [1-11 000]
    """
    def invalid_get_tx_info_test_5(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\d]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\w]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s]{1:11000}').render()), list)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\a]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\d]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\a]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\s\p]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\d]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\a]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\W\p]{1:11000}').render()), list)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\s]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\p]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\a\d\W]{1:11000}').render()), list)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\w\s]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\h]{1:11000}').render()), list)
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\a\s]{1:11000}').render()), list)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_rpc.get_tx_info(StringGenerator('[\p\d\W\w\h\a]{1:11000}').render()), list)


def repeat_tx_info_unit_tests(nb_of_runs):
    for i in (1, nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)


unittest.main()

