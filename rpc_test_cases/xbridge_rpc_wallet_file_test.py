import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS FOR ALL WALLET RELATED FUNCTIONS STARTING WITH GET ***
"""

class wallet_File_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    def test_importwallet(self):
        try:
            log_json = ""
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importwallet, xbridge_utils.ca_random_tx_id)
            logstr = {"group": "test_importwallet", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_importwallet", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_importwallet unit test FAILED')
            xbridge_logger.logger.info('invalid_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)    
    
    def test_backupwallet(self):
        try:
            log_json = ""
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet(""))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet(" "))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("----"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("{"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("}"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("["))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("]"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("[]"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet("{}"))
            self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet(xbridge_utils.ca_random_tx_id))
            log_json = {"group": "backupwallet", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "backupwallet", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('backupwallet unit test FAILED')
            xbridge_logger.logger.info('invalid_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

unittest.main()
