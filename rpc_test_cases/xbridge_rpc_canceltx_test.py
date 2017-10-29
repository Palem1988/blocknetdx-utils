import unittest
import time
import sys

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""
def dxCancel_RPC_sequence(nb_of_runs=1000, data_nature=xbridge_utils.RANDOM_VALID_INVALID, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        assert type(xbridge_rpc.cancel_tx(xbridge_utils.ca_random_tx_id)) == dict
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(xbridge_utils.ca_random_tx_id), "API": "dxCancel"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("dxCancel_RPC_sequence.xlsx", time_distribution)



"""                       ***  UNIT TESTS ***

    - Assertions currently take the following form ==> self.assertIsInstance(..., dict).
    More precise assertions may have to be written, when we have real data.

    - We test many combinations. But additional scenarios may have to be added.

"""

class cancel_Tx_UnitTest(unittest.TestCase):
    """
            - Basic tests
    """
    def test_invalid_cancel_1(self):
        self.assertIsInstance(xbridge_rpc.cancel_tx(" "), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(""), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("[]"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("[[]]"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("{{}}"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("{[]}"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("[{[]}]"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("["), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("{"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("]"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("}"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("''"), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx("'"), dict)

    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_cancel_2(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\w]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s]{64}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\p]{64}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{64}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\w\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\s]{64}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\W\w\h\a]{64}').render()), dict)


    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def test_invalid_cancel_3(self):
       # We pick from a single class at a time
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\w]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s]{9000:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\p]{9000:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\w\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\s]{9000:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\W\w\h\a]{9000:11000}').render()), dict)


    """
          - Same as before, but now the random input parameters are of random length [1-11 000]
    """
    def test_invalid_cancel_4(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\w]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s]{1:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\s\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\W\p]{1:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\w\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\a\s]{1:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_rpc.cancel_tx(StringGenerator('[\p\d\W\w\h\a]{1:11000}').render()), dict)


def repeat_cancel_tx_unit_tests(runs=1000):
    for j in (1, runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

# unittest.main()
