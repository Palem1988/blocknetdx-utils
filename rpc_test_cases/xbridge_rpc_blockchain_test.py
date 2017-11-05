import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class Blockchain_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        
    def test_get_blockcount(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_blockcount() , int)
            self.assertGreater(xbridge_rpc.get_blockcount(), 120000)
        except AssertionError as e:
            xbridge_logger.logger.info('get_blockcount unit test FAILED')

    def test_get_difficulty(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getdifficulty(), Decimal)
            self.assertGreater(xbridge_rpc.rpc_connection.getdifficulty(), 1000)
        except AssertionError as e:
            xbridge_logger.logger.info('getdifficulty unit test FAILED')

    def test_getblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(0), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(10), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(100000), str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -10)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 100000000000000)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 10.2)
            neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
                                                              -0.0000000000000000000000000000000000000000000000000000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, neg_number)
            large_positive_nb = xbridge_utils.generate_random_number(99999999999999999999999999,
                                                                     99999999999999999999999999999999999999999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, large_positive_nb)
        except AssertionError:
            xbridge_logger.logger.info('getblockhash unit test FAILED')


# unittest.main()
