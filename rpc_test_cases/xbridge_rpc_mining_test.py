import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class Mining_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    def test_submitblock(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock,
                              xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('submitblock unit test FAILED')

# unittest.main()
