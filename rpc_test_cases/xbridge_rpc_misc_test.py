import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS FOR ALL WALLET RELATED FUNCTIONS STARTING WITH GET ***
"""

class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    @unittest.skip("disabled - not tested")
    def test_signmessage(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("", ""), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage(" "), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("----"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("{"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("}"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("["), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("]"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("{"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("}"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("[]"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("{}"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage("{}"), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.test_signmessage(xbridge_utils.ca_random_tx_id), dict)
            log_json = {"group": "test_signmessage", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_signmessage", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_signmessage unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
            
    # VALID COMBINATIONS
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_autocombinerewards_valid(self):
        try:
            log_json = ""
            success_str = "Auto Combine Rewards Threshold Set"
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.VALID_DATA)            
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, -99999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, 0), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.fixed_negative_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.fixed_positive_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.valid_random_positive_int), success_str)
            log_json = {"group": "autocombinerewards", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "autocombinerewards", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('autocombinerewards valid unit test FAILED')
            xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
            xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)

    # INVALID COMBINATIONS : GARBAGE + OUT-OF-BOUNDS DATA + DATA WE EXPECT THE FUNCTION TO REJECT
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_autocombinerewards_invalid(self):
        try:
            log_json = ""
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA)            
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, "", "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, "", xbridge_utils.fixed_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, "", xbridge_utils.fixed_negative_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, "", xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, False, -9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, True, -9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, False, 9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, True, 9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, False, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, True, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, True, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, False, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, xbridge_utils.ca_random_tx_id, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, xbridge_utils.ca_random_tx_id, -xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, xbridge_utils.ca_random_tx_id, xbridge_utils.fixed_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, xbridge_utils.ca_random_tx_id, xbridge_utils.ca_random_tx_id)
            log_json = {"group": "autocombinerewards", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "autocombinerewards", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('autocombinerewards invalid unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
            xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)
            
            
# unittest.main()
