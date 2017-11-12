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
                - Specific tests with txid = c9a59af05356605a9c028ea7c0b9f535393d9ffe32cda4af23e3c9ccc0e5f64a
    """
    @unittest.skip("DISABLED - TX IS NOT AVAILABLE ANYMORE")
    def test_valid_tx_id_1(self):
        try:
            rst = xbridge_rpc.get_tx_info("c9a59af05356605a9c028ea7c0b9f535393d9ffe32cda4af23e3c9ccc0e5f64a")
            self.assertIsInstance(rst, list)
            self.assertIsInstance(rst[0], dict)
            self.assertEqual(rst[0]["from"], "LTC")
            self.assertEqual(rst[0]["to"], "SYS")
            self.assertEqual(rst[0]["fromAmount"], "0.1333")
            self.assertEqual(rst[0]["state"], "Open")
            log_json = {"group": "test_valid_tx_id_1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_valid_tx_id_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_valid_tx_id_1 valid unit test FAILED: %s' % ass_err)
        except IndexError as index_err:
            log_json = {"group": "test_valid_tx_id_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_valid_tx_id_1 valid unit test FAILED: %s' % index_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_valid_tx_id_1", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_valid_tx_id_1 unit test ERROR: %s' % json_excpt)

    def test_invalid_get_tx_info_1(self):
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertIsInstance(xbridge_rpc.get_tx_info(basic_garbage_str), list)
                    # self.assertRaises(JSONRPCException, xbridge_rpc.get_tx_info, basic_garbage_str)
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test ERROR: %s' % str(json_excpt))

    """
          - Character classes are chosen randomly
          - Size of the input parameter is chosen randomly too.
    """
    def test_invalid_get_tx_info_2(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_tx_info(self.random_length_str_with_random_char_class), list)
            log_json = {"group": "test_invalid_get_tx_info_2", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_get_tx_info_2", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('dxGetTxInfo unit test group 2 FAILED on parameter: %s', self.random_length_str_with_random_char_class)
                
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_get_tx_info_3(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_length) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        log_json = {"group": "test_invalid_get_tx_info_3", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_get_tx_info_3", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 3 FAILED on parameter: %s', generated_str)

    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def test_invalid_get_tx_info_4(self):
        string_lower_bound=9000
        string_upper_bound=11000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        log_json = {"group": "test_invalid_get_tx_info_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_get_tx_info_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 4 FAILED on parameter: %s', generated_str)

    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_get_tx_info_5(self):
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        log_json = {"group": "test_invalid_get_tx_info_5", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_get_tx_info_5", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_1 unit test FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('dxGetTxInfo unit test group 5 FAILED on parameter: %s', generated_str)

    def test_get_transaction_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_transaction_list(), list)
            log_json = {"group": "test_get_transaction_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transaction_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_list unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transaction_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_list unit test ERROR: %s' % json_err)

    def test_get_transaction_history_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_transaction_history_list(), list)
            log_json = {"group": "test_get_transaction_history_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transaction_history_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history_list unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transaction_history_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history_list unit test ERROR: %s' % json_err)

    def test_get_currency_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_currency_list(), dict)
            log_json = {"group": "test_get_currency_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_currency_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currency_list unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_currency_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currency_list unit test ERROR: %s' % json_err)


# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_autocombinerewards_valid"))
suite.addTest(get_Tx_Info_UnitTest("test_get_transaction_list"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""


