import unittest
import xbridge_logger
import random
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

"""                       ***  UNIT TESTS ***
"""

class Mining_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_submitblock(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, basic_garbage_str)
                    log_json = {"group": "test_submitblock", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_submitblock", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_submitblock unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_submitblock", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_submitblock unit test ERROR: %s' % str(json_excpt))

    def test_getmininginfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getmininginfo(), dict)
            log_json = {"group": "test_getmininginfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getmininginfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmininginfo unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getmininginfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmininginfo unit test ERROR: %s' % str(json_excpt))

    # getnetworkhashps ( blocks height )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_getnetworkhashps_invalid(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
                    modified_set = [x for x in modified_set if x is not None]
                    optional_blocks = random.choice(modified_set)
                    optional_height = random.choice(modified_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getnetworkhashps, optional_blocks, optional_height)
                    log_json = {"group": "test_getnetworkhashps", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getnetworkhashps", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getnetworkhashps unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_blocks: %s \n' % optional_blocks)
                    xbridge_logger.logger.info('optional_height: %s \n' % optional_height)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_getnetworkhashps", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getnetworkhashps unit test ERROR: %s' % str(json_excpt))

    # getnetworkhashps ( blocks height )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_getnetworkhashps_valid(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getnetworkhashps(), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(xbridge_utils.fixed_positive_int, xbridge_utils.valid_random_positive_int), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(xbridge_utils.fixed_negative_int, xbridge_utils.valid_random_positive_int), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(xbridge_utils.valid_random_positive_int, xbridge_utils.valid_random_positive_int), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(0, 0), int)
            # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getnetworkhashps, xbridge_utils.fixed_large_positive_int, xbridge_utils.fixed_positive_int)
            log_json = {"group": "test_getnetworkhashps_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getnetworkhashps_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getnetworkhashps_valid FAILED: %s' % ass_err)
            # xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getnetworkhashps_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getnetworkhashps_valid unit test ERROR: %s' % str(json_excpt))


    # prioritisetransaction <txid> <priority delta> <fee delta>
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_prioritisetransaction(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    modified_set = xbridge_utils.set_of_invalid_parameters
                    # modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
                    # modified_set = [x for x in modified_set if x is not None]
                    txid = random.choice(modified_set)
                    priority = random.choice(modified_set)
                    fee = random.choice(modified_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.prioritisetransaction, txid, priority, fee)
                    log_json = {"group": "test_prioritisetransaction", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_prioritisetransaction", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_prioritisetransaction unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('txid: %s \n' % txid)
                    xbridge_logger.logger.info('priority: %s \n' % priority)
                    xbridge_logger.logger.info('fee: %s \n' % fee)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_prioritisetransaction", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_prioritisetransaction unit test ERROR: %s' % str(json_excpt))

# unittest.main()
