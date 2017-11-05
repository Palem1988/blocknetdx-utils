import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class wallet_List_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    def test_listaccounts(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaccounts(), dict)
        except AssertionError:
            xbridge_logger.logger.info('listaccounts unit test FAILED')

    def test_listaddressgroupings(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaddressgroupings(), list)
        except AssertionError:
            xbridge_logger.logger.info('listaddressgroupings unit test FAILED')

    def test_listlockunspent(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.listlockunspent(), list)
        except AssertionError:
            xbridge_logger.logger.info('listlockunspent unit test FAILED')

    def test_listsinceblock(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.listsinceblock(xbridge_utils.ca_random_tx_id), dict)
        except AssertionError:
            xbridge_logger.logger.info('listsinceblock unit test FAILED')

    @unittest.skip("TODO")
    def test_listreceivedbyaddress(self):
        try:
            pass
            # self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.ca_random_tx_id), dict)
        except AssertionError:
            xbridge_logger.logger.info('listreceivedbyaddress unit test FAILED')

    # Same structure with listreceivedbyaddress
    def test_listreceivedbyaccount(self):
        try:
            # valid with only one param
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int), list)
            # valid with two params
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int, True), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int, False), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, True), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, False), list)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int)
            # with second parameter => TODO
            """
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int)
            """
        except AssertionError:
            xbridge_logger.logger.info('listreceivedbyaccount unit test FAILED')

# unittest.main()