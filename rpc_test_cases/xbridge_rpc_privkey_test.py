import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS FOR ALL WALLET RELATED FUNCTIONS STARTING WITH GET ***
"""

class private_Key_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    # importprivkey "blocknetdxprivkey" ( "label" rescan )
    # @unittest.skip("disabled - not tested")
    def test_importprivkey(self):
        try:
            log_json = ""
            valid_blocknetdx_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(xbridge_rpc.rpc_connection.dumpprivkey(valid_blocknetdx_address), dict)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.importprivkey, xbridge_utils.ca_random_tx_id)
            logstr = {"group": "test_importprivkey", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_importprivkey", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_importprivkey unit test FAILED')
            xbridge_logger.logger.info('valid_blocknetdx_address: %s \n' % valid_blocknetdx_address)
            xbridge_logger.logger.info('invalid_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

    # dumpprivkey "blocknetdxaddress"
    def test_dumpprivkey(self):
        try:
            log_json = ""
            valid_blocknetdx_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(xbridge_rpc.rpc_connection.dumpprivkey(valid_blocknetdx_address), dict)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.dumpprivkey, xbridge_utils.ca_random_tx_id)
            logstr = {"group": "test_dumpprivkey", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_dumpprivkey", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_dumpprivkey unit test FAILED')
            xbridge_logger.logger.info('valid_blocknetdx_address: %s \n' % valid_blocknetdx_address)
            xbridge_logger.logger.info('invalid_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)


# unittest.main()
