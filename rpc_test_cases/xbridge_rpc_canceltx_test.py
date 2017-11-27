import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator

class cancelUnitTest(unittest.TestCase):
    @unittest.skip("TEMPORARILY DISABLED - THE TXID IS NOT AVAILABLE ANYMORE")
    def test_valid_cancel_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.cancel_tx("c9a59af05356605a9c028ea7c0b9f535393d9ffe32cda4af23e3c9ccc0e5f64a"), dict)
            log_json = {"group": "test_valid_cancel_1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_valid_cancel_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_valid_cancel_1 FAILED: %s' % ass_err)
    
    @unittest.skip("TEMPORARILY DISABLED - IN REVIEW")
    def test_invalid_cancel_1(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsInstance(xbridge_rpc.cancel_tx(basic_garbage_str), dict)
                    else:
                        self.assertRaises(JSONRPCException, xbridge_rpc.cancel_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_cancel_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)

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
                        xbridge_logger.XLOG("test_invalid_cancel_2", 0)
                    except AssertionError as ass_err:
                        xbridge_logger.XLOG("test_invalid_cancel_2", 1, ass_err, [generated_str])
                    except JSONRPCException as json_excpt:
                        xbridge_logger.XLOG("test_invalid_cancel_2", 2, json_excpt, [generated_str])

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
                        xbridge_logger.XLOG("test_invalid_cancel_3", 0)
                    except AssertionError as ass_err:
                        xbridge_logger.XLOG("test_invalid_cancel_3", 1, ass_err, [generated_str])
                    except JSONRPCException as json_excpt:
                        xbridge_logger.XLOG("test_invalid_cancel_3", 2, json_excpt, [generated_str])

                            
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
                        xbridge_logger.XLOG("test_invalid_cancel_4", 0)
                    except AssertionError as ass_err:
                        xbridge_logger.XLOG("test_invalid_cancel_4", 1, ass_err, [generated_str])
                    except JSONRPCException as json_excpt:
                        xbridge_logger.XLOG("test_invalid_cancel_4", 2, json_excpt, [generated_str])

"""
if __name__ == '__main__':
    unittest.main()

unittest.main()
"""

