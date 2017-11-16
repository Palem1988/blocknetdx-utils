import unittest
import random
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class Network_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    def test_addnode_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_getaddednodeinfo_invalid"):
                try:
                    node = random.choice(xbridge_utils.set_of_invalid_parameters)
                    cmd = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsNone(xbridge_rpc.addnode(node, cmd))
                    log_json = {"group": "test_addnode_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_addnode_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_addnode_invalid FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_addnode_invalid ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_addnode_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)


    # getaddednodeinfo dns bool ( "node" )
    # getaddednodeinfo true
    # getaddednodeinfo true "192.168.0.201"
    # Returns information about the given added node, or all added nodes
    # If dns is false, only a list of added nodes will be provided, otherwise connected information will also be available.
    def test_getaddednodeinfo_invalid(self):
        log_json = ""
        self.assertIsInstance(xbridge_rpc.rpc_connection.getaddednodeinfo(True), list)
        self.assertIsInstance(xbridge_rpc.rpc_connection.getaddednodeinfo(False), list)
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_getaddednodeinfo_invalid"):
                try:
                    dns = random.choice(xbridge_utils.set_of_invalid_parameters)
                    node = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getaddednodeinfo, dns, node)
                    self.assertIsNone(xbridge_rpc.getaddednodeinfo(dns, node))
                    log_json = {"group": "test_getaddednodeinfo_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getaddednodeinfo_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getaddednodeinfo_invalid FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_getaddednodeinfo_invalid ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_getaddednodeinfo_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)

    def test_get_connection_count(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getconnectioncount(), int)
            self.assertGreater(xbridge_rpc.rpc_connection.getconnectioncount(), 1)
            log_json = {"group": "get_connectioncount", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('get_connection_count unit test FAILED: %s' % str(ass_err))
            log_json = {"group": "get_connectioncount", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "get_connectioncount", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('get_connectioncount unit test ERROR: %s' % str(json_excpt))

    def test_get_node_list(self):
        try:
            log_json = ""
            node_list = xbridge_rpc.get_node_list()
            self.assertIsInstance(node_list, list)
            self.assertGreater(len(node_list), 200)
            log_json = {"group": "get_node_list", "success": 1,  "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('get_node_list unit test FAILED: %s' % str(ass_err))
            log_json = {"group": "get_node_list", "success": 0,  "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('get_node_list unit test ERROR: %s' % str(json_excpt))
            log_json = {"group": "get_node_list", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    def test_get_version(self):
        try:
            log_json = ""
            version_nb = xbridge_rpc.get_core_version()
            self.assertIsInstance(version_nb, int)
            self.assertGreater(version_nb, 3073600)
            log_json = {"group": "get_version", "success": 1,  "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('get_version unit test FAILED: %s' % str(ass_err))
            log_json = {"group": "get_version", "success": 0,  "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('get_node_list unit test ERROR: %s' % str(json_excpt))
            log_json = {"group": "get_version", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    def test_get_peer_info(self):
        try:
            log_json = ""
            peer = xbridge_rpc.rpc_connection.getpeerinfo()
            self.assertIsInstance(peer, list)
            self.assertGreater(len(peer), 0)
            log_json = {"group": "getpeerinfo", "success": 1,  "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('getpeerinfo unit test FAILED: %s' % str(ass_err))
            log_json = {"group": "getpeerinfo", "success": 0,  "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('getpeerinfo unit test ERROR: %s' % str(json_excpt))
            log_json = {"group": "getpeerinfo", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

# unittest.main()
