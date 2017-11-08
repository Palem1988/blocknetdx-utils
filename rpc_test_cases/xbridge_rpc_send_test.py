import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

valid_multisend_cmds = ["print"]

class send_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # multisend <command>
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_multisend(self):
        log_json = ""
        # VALID
        with self.subTest("valid multisends commands"):
            try:
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("print"), list)
                log_json = {"group": "test_multisend", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                log_json = {"group": "test_multisend", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend unit test FAILED')
                xbridge_logger.logger.info('multisend("print") FAILED \n')
        # INVALID FIXED GARBAGE
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.multisend(basic_garbage_str, basic_garbage_str))
                    log_json = {"group": "test_signmessage", "success": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError:
                    log_json = {"group": "test_multisend", "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_multisend unit test FAILED')
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
        # INVALID RANDOM GARBAGE
        with self.subTest("random garbage"):
            try:
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.multisend(basic_garbage_str, basic_garbage_str))
                log_json = {"group": "test_multisend", "success": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError:
                log_json = {"group": "test_multisend", "success": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend unit test FAILED')
                xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
            
            
    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_invalid(self):
        send_address_list = [xbridge_utils.sendtoaddress, xbridge_utils.sendtoaddressix]
        for send_address_func in send_address_list:
            log_json = ""
            with self.subTest("invalid sendtoaddress"):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", "")
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", xbridge_utils.fixed_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", xbridge_utils.fixed_negative_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", xbridge_utils.invalid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.ca_random_tx_id)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.ca_random_tx_id)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.invalid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.invalid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.invalid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, -xbridge_utils.invalid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.fixed_positive_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.invalid_random_positive_float)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, -xbridge_utils.invalid_random_positive_float)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_float)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.fixed_positive_float)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.ca_random_tx_id)
                    log_json = {"group": send_address_func, "success": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError:
                    log_json = {"group": send_address_func, "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s invalid unit test FAILED' % send_address_func)
                    xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                    xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)
                    xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                    xbridge_logger.logger.info('invalid_random_positive_float: %s \n' % xbridge_utils.invalid_random_positive_float)
                    xbridge_logger.logger.info('valid_random_positive_float: %s \n' % xbridge_utils.valid_random_positive_float)
                    xbridge_logger.logger.info('fixed_positive_float: %s \n' % xbridge_utils.fixed_positive_float)
                    xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
            
            
    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_valid(self):
        send_address_list = [xbridge_utils.sendtoaddress, xbridge_utils.sendtoaddressix]
        valid_blocknet_address = xbridge_utils.rpc_connection.getnewaddress()
        for send_address_func in send_address_list:
            log_json = ""
            with self.subTest("valid sendtoaddress"):
                try:        
                    self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, xbridge_utils.xbridge_utils.valid_random_positive_int), dict)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, xbridge_utils.xbridge_utils.valid_random_positive_float), dict)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, xbridge_utils.xbridge_utils.fixed_positive_int), dict)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, xbridge_utils.xbridge_utils.fixed_positive_float), dict)
                    # NEGATIVE NUMBERS
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, -xbridge_utils.xbridge_utils.valid_random_positive_float), dict)
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, -xbridge_utils.xbridge_utils.fixed_positive_int), dict)
                    # 0 SEND
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, 0), dict)
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, 0), dict)
                    log_json = {"group": send_address_func, "success": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError:
                    log_json = {"group": send_address_func, "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s invalid unit test FAILED' % send_address_func)
                    xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                    xbridge_logger.logger.info('valid_random_positive_float: %s \n' % xbridge_utils.valid_random_positive_float)
                    xbridge_logger.logger.info('fixed_positive_float: %s \n' % xbridge_utils.fixed_positive_float)
                    xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
            
    # sendfrom "fromaccount" "toblocknetdxaddress" amount ( minconf "comment" "comment-to" )
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_sendfrom_invalid(self):
        log_json = ""
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, " ", " ", " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", 0)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", xbridge_utils.fixed_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", xbridge_utils.fixed_negative_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), -9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), 9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), 0)
            # NOT OK
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, -xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.fixed_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.invalid_random_positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, -xbridge_utils.invalid_random_positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.fixed_positive_float)
            # OK
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_float)
            log_json = {"group": "sendfrom", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "sendfrom", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('sendfrom invalid unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
            xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
            xbridge_logger.logger.info('invalid_random_positive_float: %s \n' % xbridge_utils.invalid_random_positive_float)
            xbridge_logger.logger.info('valid_random_positive_float: %s \n' % xbridge_utils.valid_random_positive_float)
            xbridge_logger.logger.info('fixed_positive_float: %s \n' % xbridge_utils.fixed_positive_float)
            xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)        
            
# unittest.main()
