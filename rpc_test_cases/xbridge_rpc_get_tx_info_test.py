import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utils import xbridge_custom_exceptions

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator

import sys
sys.path.insert(0,'..')
import xbridge_config

MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

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
            xbridge_logger.logger.info('test_valid_tx_id_1 ERROR: %s' % json_excpt)

    def test_invalid_get_tx_info_1(self):
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertIsInstance(xbridge_rpc.get_tx_info(basic_garbage_str), list)
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_1 FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(basic_garbage_str)[:MAX_LOG_LENGTH])
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_get_tx_info_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_1 ERROR: %s' % str(json_excpt))
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(basic_garbage_str)[:MAX_LOG_LENGTH])

    def test_invalid_get_tx_info_2(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, str)]
        for basic_garbage_str in custom_set:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    # self.assertIsInstance(xbridge_rpc.get_tx_info, list)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.get_tx_info, basic_garbage_str)
                    log_json = {"group": "test_invalid_get_tx_info_2", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_get_tx_info_2", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_2 FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(basic_garbage_str)[:MAX_LOG_LENGTH])
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_get_tx_info_2", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_get_tx_info_2 ERROR: %s' % str(json_excpt))
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(basic_garbage_str)[:MAX_LOG_LENGTH])
                        
    """
          - Character classes are chosen randomly
          - Size of the input parameter is chosen randomly too.
    """
    def test_invalid_get_tx_info_3(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_tx_info(self.random_length_str_with_random_char_class), list)
            log_json = {"group": "test_invalid_get_tx_info_3", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_get_tx_info_3", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_get_tx_info_3 FAILED: %s' % ass_err)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('param: %s \n' % str(self.random_length_str_with_random_char_class)[:MAX_LOG_LENGTH])
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_invalid_get_tx_info_3", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_get_tx_info_3 ERROR: %s' % str(json_excpt))
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('param: %s \n' % str(self.random_length_str_with_random_char_class)[:MAX_LOG_LENGTH])
                
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_get_tx_info_4(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_length) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        log_json = {"group": "test_invalid_get_tx_info_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_get_tx_info_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_4 FAILED: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_get_tx_info_4", "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_4 ERROR: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])

    """
          - Same as before, but now the random strings are of random but always very high size [9 000-11 000]
    """
    def test_invalid_get_tx_info_5(self):
        string_lower_bound=9000
        string_upper_bound=11000
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
                        xbridge_logger.logger.info('test_invalid_get_tx_info_5 FAILED: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_get_tx_info_5", "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_5 ERROR: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])

    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_get_tx_info_6(self):
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    try:
                        clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.get_tx_info(generated_str), list)
                        log_json = {"group": "test_invalid_get_tx_info_6", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_get_tx_info_6", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_6 FAILED: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_get_tx_info_6", "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_get_tx_info_6 ERROR: %s' % str(json_excpt))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('param: %s \n' % str(generated_str)[:MAX_LOG_LENGTH])

    


# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_autocombinerewards_valid"))
suite.addTest(get_Tx_Info_UnitTest("test_invalid_get_tx_info_2"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""


