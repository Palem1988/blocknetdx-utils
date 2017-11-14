import unittest
import xbridge_logger

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utils import xbridge_custom_exceptions

class sendUnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_invalid_send_1(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if basic_garbage_str in (9999999999999999999999999999999999999999999999999999999999999999, -9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.send_tx(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.send_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_send_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    xbridge_logger.logger.info('test_invalid_send_1 unit test FAILED: %s' % ass_err)
                    log_json = {"group": "test_invalid_send_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_send_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_send_1 unit test ERROR: %s' % str(json_excpt))

    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_send_2(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_length) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsNone(xbridge_rpc.send_tx(generated_str))
                        log_json = {"group": "test_invalid_send_2", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_send_2", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_send_2 FAILED on parameter: %s', ass_err)
                        xbridge_logger.logger.info('param: %s', generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_send_2", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_send_2 unit test ERROR: %s' % str(json_excpt))

    """
          - Same as before, but now the random strings are of random but always very long size [9 000-11 000]
    """
    def test_invalid_send_3(self):
        string_lower_bound=9000
        string_upper_bound=11000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsNone(xbridge_rpc.send_tx(generated_str))
                        log_json = {"group": "test_invalid_send_3", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        xbridge_logger.logger.info('test_invalid_send_3 FAILED on parameter: %s', ass_err)
                        xbridge_logger.logger.info('param: %s', generated_str)
                        log_json = {"group": "test_invalid_send_3", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_send_3", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_send_1 unit test ERROR: %s' % str(json_excpt))

    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_send_4(self):
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsNone(xbridge_rpc.send_tx(generated_str))
                        log_json = {"group": "test_invalid_send_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        xbridge_logger.logger.info('test_invalid_send_4 FAILED on parameter: %s', ass_err)
                        xbridge_logger.logger.info('param: %s', generated_str)
                        log_json = {"group": "test_invalid_send_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_send_4", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_send_1 unit test ERROR: %s' % str(json_excpt))


"""
if __name__ == '__main__':
    unittest.main()

unittest.main()
"""

