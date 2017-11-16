import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random
from decimal import *

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils


class Utils_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # estimatefee nblocks
    def test_estimatefee(self):
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, int):
                        if basic_str in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999):
                            self.assertIsNone(xbridge_rpc.estimatepriority(basic_str))
                        else:
                            self.assertIsInstance(xbridge_rpc.estimatepriority(basic_str), Decimal)
                    else:
                        self.assertIsNone(xbridge_rpc.estimatefee(basic_str))
                    log_json = {"group": "test_estimatefee", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_estimatefee", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_estimatefee FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_str: %s \n' % basic_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_estimatefee", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_estimatefee ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('basic_str: %s \n' % basic_str)

    # estimatepriority nblocks
    def test_estimatepriority(self):
        # modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, int):
                        if basic_str in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999):
                            self.assertIsNone(xbridge_rpc.estimatepriority(basic_str))
                        else:
                            self.assertIsInstance(xbridge_rpc.estimatepriority(basic_str), Decimal)
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.estimatepriority, basic_str)
                    log_json = {"group": "test_estimatepriority", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_estimatepriority", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_estimatepriority FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_str: %s \n' % basic_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_estimatepriority", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_estimatepriority ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('basic_str: %s \n' % basic_str)

    # validateaddress "blocknetdxaddress"
    def test_validateaddress_invalid(self):
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, str):
                        self.assertIsInstance(xbridge_rpc.validateaddress(basic_str), dict)
                    else:
                        self.assertIsNone(xbridge_rpc.validateaddress(basic_str))
                    log_json = {"group": "test_validateaddress_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_validateaddress_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_validateaddress_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_str: %s \n' % str(basic_str))
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_validateaddress_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_validateaddress_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('basic_str: %s \n' % str(basic_str))

    # validateaddress "blocknetdxaddress"
    def test_validateaddress_valid(self):
        try:
            valid_block_address = xbridge_utils.generate_valid_blocknet_address()
            self.assertIsInstance(xbridge_rpc.validateaddress(valid_block_address), dict)
            log_json = {"group": "test_validateaddress_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_validateaddress_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_validateaddress_valid FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_block_address: %s \n' % valid_block_address)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_validateaddress_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_validateaddress_valid ERROR: %s' % json_excpt)
            xbridge_logger.logger.info('valid_block_address: %s \n' % valid_block_address)

    # verifymessage "blocknetdxaddress" "signature" "message"
    def test_verify_message_invalid(self):
        for i in range(50):
            log_json = ""
            with self.subTest("test_verify_message_invalid"):
                try:
                    blocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                    signature = random.choice(xbridge_utils.set_of_invalid_parameters)
                    message = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.verifymessage, blocknetdxaddress, signature, message)
                    self.assertIsNone(xbridge_rpc.verifymessage(blocknetdxaddress, signature, message))
                    log_json = {"group": "test_verify_message_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_verify_message_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_verify_message_invalid FAILED: %s' % ass_err)

   
# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_validateaddress_valid"))
suite.addTest(Misc_UnitTest("test_validateaddress_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""
