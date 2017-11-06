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
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaccounts(), dict)
            logstr = {"group": "test_listaccounts", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_listaccounts", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listaccounts unit test FAILED')

    def test_listaddressgroupings(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaddressgroupings(), list)
            logstr = {"group": "test_listaddressgroupings", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_listaddressgroupings", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listaddressgroupings unit test FAILED')

    def test_listlockunspent(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listlockunspent(), list)
            logstr = {"group": "test_listlockunspent", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_listlockunspent", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listlockunspent unit test FAILED\n')
            
    def test_listsinceblock(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listsinceblock(xbridge_utils.ca_random_tx_id), dict)
            logstr = {"group": "test_listsinceblock", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_listsinceblock", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listsinceblock unit test FAILED\n')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

    def test_listreceivedbyaccount(self):
        log_json = ""
        # VALID COMBINATIONS
        with self.subTest("VALID COMBINATIONS"):
            try:
                # VALID COMBINATIONS - 1 PARAMETER
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int), list)
                # VALID COMBINATIONS - 2 PARAMETERS
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int, False), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, False), list)
                logstr = {"group": "test_listreceivedbyaccount", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                log_json = {"group": "test_listreceivedbyaccount", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaccount valid sub unit test group FAILED: \n')
                xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
                xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
        # INVALID COMBINATIONS
        with self.subTest("INVALID COMBINATIONS"):
            try:        
                # INVALID COMBINATIONS - 1 PARAMETER
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int)
                # INVALID COMBINATIONS - 2 PARAMETERS
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.positive_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.negative_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_large_positive_int, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.fixed_small_positive_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, xbridge_utils.invalid_random_positive_int, xbridge_utils.ca_random_tx_id)
                logstr = {"group": "test_listreceivedbyaccount", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                logstr = {"group": "test_listreceivedbyaccount", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaccount invalid sub unit test group FAILED: \n')
                xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                xbridge_logger.logger.info('positive_float: %s \n' % xbridge_utils.positive_float)
                xbridge_logger.logger.info('fixed_large_positive_int: %s \n' % xbridge_utils.fixed_large_positive_int)
                xbridge_logger.logger.info('fixed_small_positive_float: %s \n' % xbridge_utils.fixed_small_positive_float)
                xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)

    def test_listreceivedbyaddress(self):
        log_json = ""
        # VALID COMBINATIONS
        with self.subTest("VALID COMBINATIONS"):
            try:
                # VALID COMBINATIONS - 1 PARAMETER
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_positive_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_negative_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int), list)
                # VALID COMBINATIONS - 2 PARAMETERS
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_negative_int, False), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int, False), list)
                logstr = {"group": "listreceivedbyaddress", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                log_json = {"group": "listreceivedbyaddress", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaddress valid sub unit test group FAILED: \n')
                xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
                xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
        # INVALID COMBINATIONS
        with self.subTest("INVALID COMBINATIONS"):
            try:        
                # INVALID COMBINATIONS - 1 PARAMETER
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.positive_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.negative_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_large_positive_int)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_small_positive_float)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.invalid_random_positive_int)
                # INVALID COMBINATIONS - 2 PARAMETERS
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.positive_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.positive_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.positive_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.negative_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.negative_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.negative_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_large_positive_int, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_large_positive_int, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_large_positive_int, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_small_positive_float, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_small_positive_float, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.fixed_small_positive_float, xbridge_utils.ca_random_tx_id)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.invalid_random_positive_int, True)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.invalid_random_positive_int, False)
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, xbridge_utils.invalid_random_positive_int, xbridge_utils.ca_random_tx_id)
                log_json = {"group": "test_listreceivedbyaccount", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                log_json = {"group": "test_listreceivedbyaccount", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaddress invalid sub unit test group FAILED: \n')
                xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                xbridge_logger.logger.info('positive_float: %s \n' % xbridge_utils.positive_float)
                xbridge_logger.logger.info('fixed_large_positive_int: %s \n' % xbridge_utils.fixed_large_positive_int)
                xbridge_logger.logger.info('fixed_small_positive_float: %s \n' % xbridge_utils.fixed_small_positive_float)
                xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)


unittest.main()