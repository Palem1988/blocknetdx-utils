import unittest
import xbridge_logger

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils

from strgen import StringGenerator
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class signUnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
    
    @unittest.skip("Disabled -> fails")
    def test_valid_tx_id_1(self):
        try:
            """
                [I] 2017-Oct-31 23:42:48 [0xb8] rpc call <signrawtransaction>
                [I] 2017-Oct-31 23:42:48 [0xb8] HTTP: req  signrawtransaction {"method":"signrawtransaction","params":["01000000814ef9590108a03740afeb62f97908aba6d79ba512162a0448ead78c1d9acb808b658149140000000000ffffffff0290ab1e000000000017a9145abd1ae96433936b627d249c0c1a57770456323587b0a8db02000000001976a914a5a4651accd909fccaa66e34a7fb5c275c6270ef88ac00000000",null,null],"id":1}

                [I] 2017-Oct-31 23:42:48 [0xb8] HTTP: resp 200 {"result":{"hex":"01000000814ef9590108a03740afeb62f97908aba6d79ba512162a0448ead78c1d9acb808b65814914000000006a4730440220111cbcdb9ccdc0e17b65e7fa1e4ec265bf76dcba8202b304b3e34ac833c297b6022008d37ca8ca5ed54bb5d217f5bcdb19c8159059e437a7dbe665c2455b1cfb93fc0121036fa429dbb28304585ebfdae5688bbac546339e578ac4403dcafdc7e15b4f08e1ffffffff0290ab1e000000000017a9145abd1ae96433936b627d249c0c1a57770456323587b0a8db02000000001976a914a5a4651accd909fccaa66e34a7fb5c275c6270ef88ac00000000","complete":true},"error":null,"id":1}
                
            """
            self.assertIsInstance(xbridge_rpc.sign_tx("240c472714c1ff14e5f66a6c93ae6f0efb2f4eff593ae31435e829126a0006cc"), dict)
        except AssertionError as e:
            xbridge_logger.logger.info('dxSign valid unit test group 1 FAILED')
    
    @unittest.skip("IN TESTING")
    def test_invalid_sign_1(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsNone(xbridge_rpc.signrawtransaction(basic_garbage_str))
                    else:
                        self.assertRaises(JSONRPCException, xbridge_rpc.cancel_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_sign_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_sign_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_sign_1 FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_sign_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_sign_1 ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('param: %s \n' % basic_garbage_str)

    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    @unittest.skip("IN TESTING")
    def test_invalid_sign_2(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_length) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        # self.assertIsNone(xbridge_rpc.signrawtransaction(generated_str))
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.signrawtransaction,
                                          generated_str)
                        log_json = {"group": "test_invalid_sign_2", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_sign_2", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_sign_2 FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_sign_2", "success": 0, "failure": 0, "error": 1}
                        xbridge_logger.logger.info('test_invalid_sign_2 ERROR: %s' % json_excpt)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                        xbridge_utils.ERROR_LOG.append(log_json)

                    
    """
          - Same as before, but now the random strings are of random but always very long size [9 000-11 000]
    """
    @unittest.skip("IN TESTING")
    def test_invalid_sign_3(self):
        string_lower_bound=9000
        string_upper_bound=11000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException,
                                          xbridge_rpc.signrawtransaction,
                                          generated_str)
                        log_json = {"group": "test_invalid_sign_3", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_sign_3", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_sign_3 FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_sign_3", "success": 0, "failure": 0, "error": 1}
                        xbridge_logger.logger.info('test_invalid_sign_3 ERROR: %s' % json_excpt)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                        xbridge_utils.ERROR_LOG.append(log_json)

                            
    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    @unittest.skip("IN TESTING")
    def test_invalid_sign_4(self):
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException,
                                          xbridge_rpc.signrawtransaction,
                                          generated_str)
                        log_json = {"group": "test_invalid_sign_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "test_invalid_sign_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_sign_4 FAILED: %s' % ass_err)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_sign_4", "success": 0, "failure": 0, "error": 1}
                        xbridge_logger.logger.info('test_invalid_sign_4 ERROR: %s' % json_excpt)
                        xbridge_logger.logger.info('param: %s' % generated_str)
                        xbridge_utils.ERROR_LOG.append(log_json)


"""
if __name__ == '__main__':
    unittest.main()
"""

unittest.main()
