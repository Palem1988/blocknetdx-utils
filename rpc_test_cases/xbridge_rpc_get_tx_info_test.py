import unittest
import time
import sys
import xbridge_logger

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""

def dxGetTransactionInfo_RPC_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    for i in range(1, 1 + nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        assert type(xbridge_rpc.get_tx_info(xbridge_utils.ca_random_tx_id)) == list
        te = time.time()
        elapsed_Time = te - ts
        print("single API sequence - dxGetTxInfo (%s secs.)" % (str(elapsed_Time)))
        json_str = {"time": elapsed_Time, "char_nb": len(xbridge_utils.ca_random_tx_id), "API": "dxGetTxInfo"}
        time_distribution.append(json_str)
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "dxGetTxInfo_sequence", "API": "dxGetTxInfo", "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("dxGetTransactionInfo_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

"""

class get_Tx_Info_UnitTest(unittest.TestCase):
    def setUp(self):
        self.random_length_str_with_random_char_class = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)

    """
                - Specific tests with txid = 240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc
    """
    def test_valid_tx_id_1(self):
        self.assertIsInstance(xbridge_rpc.get_tx_info("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc"), list)
        print("dxGetTxInfo Valid Unit Test OK")

    """
            - Basic tests
    """
    def test_invalid_get_tx_info_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_tx_info(" "), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info(""), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("[]"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("{}"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("''"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("'"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("["), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("{"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("]"), list)
            self.assertIsInstance(xbridge_rpc.get_tx_info("}"), list)
            print("dxGetTxInfo Unit Test 1 OK")
        except AssertionError as e:
            print("****** dxGetTxInfo Unit Test 1 FAILED ******")
            xbridge_logger.logger.info('dxGetTxInfo unit test group 1 FAILED')

    """
          - Character classes are chosen randomly
          - Size of the input parameter is chosen randomly too.
    """
    def test_invalid_get_tx_info_2(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_tx_info(self.random_length_str_with_random_char_class), list)
            print("dxGetTxInfo Unit Test 2 OK")
        except AssertionError as e:
            print("****** dxGetTxInfo Unit Test 2 FAILED ******")
            xbridge_logger.logger.info('dxGetTxInfo unit test group 2 FAILED on parameter: %s', self.random_length_str_with_random_char_class)
                
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_get_tx_info_3(self):
        run_count = 0
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_length) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        run_count += 1
                    except AssertionError as e:
                        print("****** dxGetTxInfo Unit Test 3 FAILED ON PARAMETER %s ******" % generated_str)
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 3 FAILED on parameter: %s', generated_str)
                        run_count += 1
        print("UT Group 3 - total subtests completed with or without errors: %s" % str(run_count))

    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def test_invalid_get_tx_info_4(self):
        run_count = 0
        string_lower_bound=9000
        string_upper_bound=11000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        run_count += 1
                    except AssertionError as e:
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 4 FAILED on parameter: %s', generated_str)
                        run_count += 1
        print("UT Group 4 - total subtests completed with or without errors: %s" % str(run_count))


    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_get_tx_info_5(self):
        run_count = 0
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        run_count += 1
                    except AssertionError as e:
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 5 FAILED on parameter: %s', generated_str)
                        run_count += 1
        print("UT Group 5 - total subtests completed with or without errors: %s" % str(run_count))


def repeat_tx_info_unit_tests(nb_of_runs):
    for i in (1, 1+nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

