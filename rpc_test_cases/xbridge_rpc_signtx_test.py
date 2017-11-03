"""
BLOCKNET API TESTING TOOLS
"""
import unittest
import time
import xbridge_logger

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""
def dxSign_RPC_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    # total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        elapsed_Time = 0
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        assert type(xbridge_rpc.sign_tx(xbridge_utils.ca_random_tx_id)) == dict
        te = time.time()
        elapsed_Time = te - ts
        # total_elapsed_seconds += elapsed_Time
        print("single API seq - dxSign - elapsedTime: %s" % (str(elapsed_Time)))
        json_str = {"time": elapsed_Time, "char_nb": len(xbridge_utils.ca_random_tx_id), "API": "dxSign"}
        time_distribution.append(json_str)
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "dxSign_RPC_sequence",
                         "API": "dxSign", "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("dxSign_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

"""

class signUnitTest(unittest.TestCase):
    def test_valid_tx_id_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.sign_tx("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc"), dict)
            # print("dxSign Valid Unit Test Group 1 OK")
        except AssertionError as e:
            # print("****** dxSign valid Unit Test Group 1 FAILED ******")
            xbridge_logger.logger.info('dxSign valid unit test group 1 FAILED')
    
    """
            - Basic tests
    """
    def test_invalid_cancel_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.sign_tx(" "), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx(""), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("[]"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("[[]]"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("{{}}"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("{[]}"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("[{[]}]"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("["), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("{"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("]"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("}"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("''"), dict)
            self.assertIsInstance(xbridge_rpc.sign_tx("'"), dict)
            # print("dxSign Unit Test Group 1 OK")
        except AssertionError as e:
            # print("****** dxSign Unit Test Group 1 FAILED ******")
            xbridge_logger.logger.info('dxSign unit test group 1 FAILED')

    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_cancel_2(self):
        run_count = 0
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_length) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.sign_tx(generated_str), dict)
                        run_count += 1
                    except AssertionError as e:
                        # print("****** dxSign Unit SUBTEST 2 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxSign unit test group 2 FAILED on parameter: %s', generated_str)
                        run_count += 1
        # print("UT Group 2 - total subtests completed with or without errors: %s" % str(run_count))

                    
    """
          - Same as before, but now the random strings are of random but always very long size [9 000-11 000]
    """
    def test_invalid_cancel_3(self):
        string_lower_bound=9000
        string_upper_bound=11000
        run_count = 0
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.sign_tx(generated_str), dict)
                        run_count += 1
                    except AssertionError as e:
                        # print("****** dxSign Unit SUBTEST 3 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxSign unit test group 3 FAILED on parameter: %s', generated_str)
                        run_count += 1
        # print("UT Group 3 - total subtests completed with or without errors: %s" % str(run_count))

                            
    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_cancel_4(self):
        run_count = 0
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.sign_tx(generated_str), dict)
                        run_count += 1
                    except AssertionError as e:
                        # print("****** dxSign Unit SUBTEST 4 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxSign unit test group 4 FAILED on parameter: %s', generated_str)
                        run_count += 1
        # print("UT Group 4 - total subtests completed with or without errors: %s" % str(run_count))


"""
def repeat_sign_tx_unit_tests(runs=1000):
    for j in (1, runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)
"""

"""
if __name__ == '__main__':
    unittest.main()
"""