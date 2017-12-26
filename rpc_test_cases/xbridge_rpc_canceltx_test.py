import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

from strgen import StringGenerator

import sys
sys.path.insert(0,'..')
import xbridge_config

MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class cancelUnitTest(unittest.TestCase):
    # @unittest.skip("TEMPORARILY DISABLED - IN REVIEW")
    def test_invalid_cancel_1(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsInstance(xbridge_rpc.cancel_tx(basic_garbage_str), dict)
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.cancel_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_cancel_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_cancel_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1 ERROR: %s' % str(json_excpt))
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)

    # @unittest.skip("TEMPORARILY DISABLED - IN REVIEW")
    def test_invalid_cancel_1b(self):
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsInstance(xbridge_rpc.cancel_tx(basic_garbage_str), dict)
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.cancel_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_cancel_1b", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_cancel_1b", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1b FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_cancel_1b", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_cancel_1b ERROR: %s' % str(json_excpt))
                    if MAX_LOG_LENGTH > 0:
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

"""
suite = unittest.TestSuite()
for i in range(50):
    suite.addTest(cancelUnitTest("test_invalid_cancel_1b"))
    # suite.addTest(cancelUnitTest("test_invalid_cancel_2"))
    # suite.addTest(accept_Tx_Test("test_invalid_accept_tx_0a_noseq"))
# suite.addTest(accept_Tx_Test("test_getrawmempool_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""