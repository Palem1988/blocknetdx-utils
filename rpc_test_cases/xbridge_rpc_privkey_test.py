import unittest
import xbridge_logger
import random

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utils import xbridge_custom_exceptions

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class private_Key_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    # importprivkey "blocknetdxprivkey" ( "label" rescan )
    # @unittest.skip("disabled - not tested")
    def test_importprivkey_invalid(self):
        modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if x not in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999)]
        for basic_garbage_str in modified_set:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    blocknetdxprivkey = random.choice(modified_set)
                    optional_label = random.choice(modified_set)
                    optional_rescan = random.choice(modified_set)
                    if random.choice(["", modified_set]) == "":
                        optional_label = None
                    else:
                        optional_label = random.choice(modified_set)
                    if random.choice(["", modified_set]) == "":
                        optional_rescan = None
                    else:
                        optional_rescan = random.choice(modified_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.importprivkey, blocknetdxprivkey, optional_label, optional_rescan)
                    log_json = {"group": "test_importprivkey_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_importprivkey_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_importprivkey_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('blocknetdxprivkey: %s \n' % blocknetdxprivkey)
                    xbridge_logger.logger.info('optional_label: %s \n' % optional_label)
                    xbridge_logger.logger.info('optional_rescan: %s \n' % optional_rescan)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_importprivkey_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_importprivkey_invalid ERROR: %s' % str(json_excpt))

    # importprivkey "blocknetdxprivkey" ( "label" rescan )
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_importprivkey_valid(self):
        try:
            log_json = ""
            valid_blocknetdx_address = xbridge_utils.generate_valid_blocknet_address()
            self.assertIsInstance(xbridge_rpc.rpc_connection.importprivkey(valid_blocknetdx_address), dict)
            log_json = {"group": "test_importprivkey_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_importprivkey_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_importprivkey_valid FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_blocknetdx_address: %s \n' % valid_blocknetdx_address)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_importprivkey_valid", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_importprivkey_valid ERROR: %s' % str(json_excpt))
            xbridge_logger.logger.info('valid_blocknetdx_address: %s \n' % valid_blocknetdx_address)
    
     # dumpprivkey "blocknetdxaddress"
    def test_dumpprivkey_invalid(self):
        self.assertIsNone(xbridge_rpc.dumpprivkey(-9999999999999999999999999999999999999999999999999999999999999999))
        self.assertIsNone(xbridge_rpc.dumpprivkey(9999999999999999999999999999999999999999999999999999999999999999))
        modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if x not in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999)]
        for basic_garbage_str in modified_set:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsNone(xbridge_rpc.dumpprivkey(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.dumpprivkey, basic_garbage_str)
                    log_json = {"group": "test_dumpprivkey_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_dumpprivkey_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_dumpprivkey_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_dumpprivkey_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_dumpprivkey_invalid ERROR: %s' % str(json_excpt))

    # dumpprivkey "blocknetdxaddress"
    # FAILED: 'PnXVPpt8TR8P3ZYn6aUDPcvjPhcigsASAxy2c8NEjaKJky4McBG4' is not an instance of <class 'dict'>
    # basic_garbage_str: BcS8oz3HYNuJqSzYLkbGkjGzxVq6nhaJrC
    def test_dumpprivkey_valid(self):
        try:
            log_json = ""
            valid_blocknetdx_address = xbridge_utils.generate_valid_blocknet_address()
            self.assertIsInstance(xbridge_rpc.rpc_connection.dumpprivkey(valid_blocknetdx_address), str)
            log_json = {"group": "test_dumpprivkey_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_dumpprivkey_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_dumpprivkey_valid FAILED: %s' % ass_err)
            xbridge_logger.logger.info('basic_garbage_str: %s \n' % valid_blocknetdx_address)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_dumpprivkey_valid", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_dumpprivkey_valid ERROR: %s' % str(json_excpt))
    
# unittest.main()