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
    def test_get_transactions(self):
        try:
            self.assertIsInstance(xbridge_rpc.dxGetTransactions(), list)
            log_json = {"group": "test_get_transactions", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transactions", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transactions FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transactions", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transactions ERROR: %s' % json_err)

    def test_get_transaction_history(self):
        try:
            self.assertIsInstance(xbridge_rpc.dxGetTransactionsHistory(), list)
            log_json = {"group": "test_get_transaction_history", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_transaction_history", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_transaction_history", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_transaction_history ERROR: %s' % json_err)

    def test_get_currencies(self):
        try:
            self.assertIsInstance(xbridge_rpc.dxGetCurrencies(), dict)
            log_json = {"group": "test_get_currencies", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_currencies", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currencies FAILED: %s' % ass_err)
        except JSONRPCException as json_err:
            log_json = {"group": "test_get_currencies", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_currencies ERROR: %s' % json_err)


# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Info_Polling_UnitTest("test_get_transaction_list"))
suite.addTest(Info_Polling_UnitTest("test_get_transactions"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""


