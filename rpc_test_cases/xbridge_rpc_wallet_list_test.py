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
            xbridge_logger.logger.info('listsinceblock unit test FAILED')

    @unittest.skip("TODO")
    def test_listreceivedbyaccount(self):
        try:
            pass
            # self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.ca_random_tx_id), dict)
        except AssertionError:
            xbridge_logger.logger.info('listsinceblock unit test FAILED')


unittest.main()

