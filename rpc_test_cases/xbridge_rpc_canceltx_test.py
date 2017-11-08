"""
BLOCKNET API TESTING TOOLS
"""
import unittest
import time
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""
def dxCancel_RPC_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    # total_elapsed_seconds = 0
    for i in range(1, 1 + nb_of_runs):
        elapsed_Time = 0
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        assert type(xbridge_rpc.cancel_tx(xbridge_utils.ca_random_tx_id)) == dict
        te = time.time()
        elapsed_Time = te - ts
        # total_elapsed_seconds += elapsed_Time
        print("single API seq - dxCancel - elapsedTime: %s" % (str(elapsed_Time)))
        json_str = {"time": elapsed_Time, "char_nb": len(xbridge_utils.ca_random_tx_id), "API": "dxCancel"}
        time_distribution.append(json_str)
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "dxCancel_RPC_sequence",
                         "API": "dxCancel", "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("dxCancel_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

"""

class cancelUnitTest(unittest.TestCase):
    def test_valid_cancel_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.cancel_tx("c9a59af05356605a9c028ea7c0b9f535393d9ffe32cda4af23e3c9ccc0e5f64a"), dict)
            log_json = {"group": "test_valid_cancel_1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_valid_cancel_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_valid_cancel_1 unit test group 1 FAILED: %s' % ass_err)
    
    """
            - Basic tests
    """
    def test_invalid_cancel_1(self):
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertIsInstance(xbridge_rpc.rpc_connection.cancel_tx(basic_garbage_str), dict)
                    log_json = {"group": "test_invalid_cancel_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 unit test ERROR: %s' % str(json_excpt))
        
        except AssertionError as e:
                xbridge_logger.logger.info('dxCancel unit test group 1 FAILED')

    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_cancel_2(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_length) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.cancel_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_cancel_2", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        # print("****** dxCancel Unit SUBTEST 2 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxCancel unit test group 2 FAILED on parameter: %s', generated_str)
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
                        self.assertIsInstance(xbridge_rpc.cancel_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_cancel_3", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        # print("****** dxCancel Unit SUBTEST 3 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxCancel unit test group 3 FAILED on parameter: %s', generated_str)
                        log_json = {"group": "test_invalid_cancel_3", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
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
                        self.assertIsInstance(xbridge_rpc.cancel_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_cancel_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        # print("****** dxCancel Unit SUBTEST 4 FAILED ON PARAMETER: %s ******" % generated_str)
                        xbridge_logger.logger.info('dxCancel unit test group 4 FAILED on parameter: %s', generated_str)
                        log_json = {"group": "test_invalid_cancel_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
        # print("UT Group 4 - total subtests completed with or without errors: %s" % str(run_count))


"""
def repeat_cancel_tx_unit_tests(runs=1000):
    for j in (1, runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)
"""

"""
if __name__ == '__main__':
    unittest.main()
"""