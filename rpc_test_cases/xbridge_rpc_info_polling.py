import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

import sys
sys.path.insert(0,'..')
import xbridge_config

MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class Info_Polling_UnitTest(unittest.TestCase):
    def test_get_transaction_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_transaction_list(), list)
            log_json = {"group": "test_get_transaction_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transaction_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_list FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transaction_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_list ERROR: %s' % json_err)

    def test_get_transaction_history_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_transaction_history_list(), list)
            log_json = {"group": "test_get_transaction_history_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transaction_history_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history_list FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transaction_history_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history_list ERROR: %s' % json_err)

    def test_get_currency_list(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_currency_list(), dict)
            log_json = {"group": "test_get_currency_list", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_currency_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currency_list FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_currency_list", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currency_list ERROR: %s' % json_err)


# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_autocombinerewards_valid"))
suite.addTest(get_Tx_Info_UnitTest("test_get_transaction_list"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""


