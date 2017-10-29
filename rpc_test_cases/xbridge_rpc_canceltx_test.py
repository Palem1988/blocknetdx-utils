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
        try:
            string_length=64
            nb_of_runs = 3
            for i in range(1, 1+nb_of_runs):
                for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
                    for sub_item in itm:
                        clss_str = sub_item + "{" + str(string_length) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.cancel_tx(generated_str), dict)
        except AssertionError as e:
            print("dxCancel RPC unit test failed on set: %s" % generated_str)


    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def test_invalid_cancel_3(self):
        try:
            string_lower_bound=9000
            string_upper_bound=11000
            nb_of_runs = 3
            for i in range(1, 1+nb_of_runs):
                for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
                    for sub_item in itm:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), dict)
        except AssertionError as e:
            print("dxCancel RPC unit test failed on set: %s" % generated_str)


    """
          - Same as before, but now the random input parameters are of random length [1-11 000]
    """
    def test_invalid_cancel_4(self):
        try:
            string_lower_bound=1
            string_upper_bound=4000
            nb_of_runs = 3
            for i in range(1, 1+nb_of_runs):
                for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
                    for sub_item in itm:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), dict)
        except AssertionError as e:
            print("dxCancel RPC unit test failed on set: %s" % generated_str)

"""
def repeat_cancel_tx_unit_tests(runs=1000):
    for j in (1, runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

unittest.main()
"""