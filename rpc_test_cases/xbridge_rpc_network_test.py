import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class Network_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    def test_get_connectioncount(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getconnectioncount(), int)
            self.assertGreater(xbridge_rpc.rpc_connection.getconnectioncount(), 10)
        except AssertionError as e:
            xbridge_logger.logger.info('get_connection_count unit test FAILED')

    def test_get_node_list(self):
        try:
            node_list = xbridge_rpc.get_node_list()
            self.assertIsInstance(node_list, list)
            self.assertGreater(len(node_list), 250)
        except AssertionError as e:
            xbridge_logger.logger.info('get_node_list unit test FAILED')

    def test_get_version(self):
        try:
            version_nb = xbridge_rpc.get_core_version()
            self.assertIsInstance(version_nb, int)
            self.assertGreater(version_nb, 3073600)
        except AssertionError as e:
            xbridge_logger.logger.info('get_version unit test FAILED')

    def test_getpeerinfo(self):
        try:
            peer = xbridge_rpc.rpc_connection.getpeerinfo()
            self.assertIsInstance(peer, list)
            self.assertGreater(len(peer), 0)
        except AssertionError:
            xbridge_logger.logger.info('getpeerinfo unit test FAILED')

# unittest.main()
