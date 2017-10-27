import unittest
import time
import sys

from interface import xbridge_client
from utils import xbridge_utils

from strgen import StringGenerator


'''                       ***  PRELIMINARY REMARKS ***

    - Only dxCancelTransaction is tested here.
'''

"""
    - Here, the length of the garbage data is very high and increased.
    The "j" parameter in the "generate_garbage_input" function is the length of the garbage input we want.

    - Non-numerical parameters are only garbage data.

    - export_data() function generates :
        1) an Excel File with the recorded timing information.
        2) a small descriptive table with mean, standard deviation, and some quantiles (25%, 50%, 75%).

"""

def test_cancel_load_v1():
    time_distribution = []
    total_elapsed_seconds = 0
    for j in range(10000, 11000):
        garbage_input_str = xbridge_utils.generate_garbage_input(j)
        ts = time.time()
        assert type(xbridge_client.CHECK_CANCEL_TX(garbage_input_str)) == dict
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxCancel"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_cancel_load_v1.xlsx", time_distribution)


"""
    - Here, the length of garbage parameters is random.
"""
def test_cancel_load_v2():
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 50000):
        garbage_input_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 10000))
        ts = time.time()
        assert type(xbridge_client.CHECK_CANCEL_TX(garbage_input_str)) == dict
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxCancel"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_cancel_load_v2.xlsx", time_distribution)


"""
    - Here, The length of the random parameter is kept fixed, we just increase the number of iterations ==> Pure load test, when resources are available.
"""
def test_cancel_load_v3():
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, 50000):
        garbage_input_str = xbridge_utils.generate_garbage_input(64)
        ts = time.time()
        assert type(xbridge_client.CHECK_CANCEL_TX(garbage_input_str)) == dict
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": len(garbage_input_str), "API": "dxCancel"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_cancel_load_v3.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

    - Assertions currently take the following form ==> self.assertIsInstance(..., dict).
    More precise assertions may have to be written, when we have real data.

    - We test many combinations. But additional scenarios may have to be added.

"""

class CancelUnitTest(unittest.TestCase):
    """
            - Basic tests
    """
    def invalid_cancel_test_1(self):
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(" "), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(""), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("[]"), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("{}"), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("''"), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("'"), dict)

    def invalid_cancel_test_1(self):
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("d63f5ed682ad744b176af1d58e9602219a40ab9bf3b506baeca81b975d999b38"), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("d63f5ed682ad744b176af1d58e9602219a40ab9bf3b506baeca81b975d999b38-------------"), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX("d63f5ed682ad744b176af1d58e9602219a40ab9bf3b506baeca81b975-------------d999b38"), dict)


    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def invalid_cancel_test_2(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\w]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s]{64}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\d]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\a]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\p]{64}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\p]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{64}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\w\s]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\h]{64}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\s]{64}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\W\w\h\a]{64}').render()), dict)


    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def invalid_cancel_test_3(self):
       # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\w]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s]{9000:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\d]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\a]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\p]{9000:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\p]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{9000:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\w\s]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\h]{9000:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\s]{9000:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\W\w\h\a]{9000:11000}').render()), dict)


    """
          - Same as before, but now the random input parameters are of random length [1-11 000]
    """
    def invalid_cancel_test_4(self):
        # We pick from a single class at a time
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\w]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s]{1:11000}').render()), dict)
        # We pick from combinations of 2 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\s\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\d]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\a]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\W\p]{1:11000}').render()), dict)
        # We pick from combinations of 3 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\p]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\a\d\W]{1:11000}').render()), dict)
        # We pick from combinations of 4 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\w\s]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\h]{1:11000}').render()), dict)
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\a\s]{1:11000}').render()), dict)
        # We pick from combinations of 5 classes
        self.assertIsInstance(xbridge_client.CHECK_CANCEL_TX(StringGenerator('[\p\d\W\w\h\a]{1:11000}').render()), dict)


def repeat_cancel_tx_unit_tests(nb_of_runs):
    for i in (1, nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)
