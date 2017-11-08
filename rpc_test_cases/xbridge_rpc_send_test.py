import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

valid_multisend_cmds = ["print"]

# THIS SET HAS TO STAY AT THE MODULE LEVEL
set_of_invalid_parameters = ["", " ",
                    0, -xbridge_utils.fixed_large_positive_int, xbridge_utils.fixed_large_positive_int, xbridge_utils.fixed_small_positive_float, 
                    True, False,
                    xbridge_utils.ca_random_tx_id,
                    xbridge_utils.fixed_positive_int,
                    xbridge_utils.invalid_random_positive_int,
                    xbridge_utils.invalid_random_positive_float,
                    -xbridge_utils.invalid_random_positive_int,
                    -xbridge_utils.invalid_random_positive_float,
                    xbridge_utils.valid_random_positive_float,
                    xbridge_utils.fixed_positive_float,
                    -xbridge_utils.valid_random_positive_float,
                    -xbridge_utils.fixed_positive_float,
                    ]

# WE COMPLETE THE LIST
set_of_invalid_parameters.extend(basic_garbage_list)
        
class send_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # multisend <command>
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_multisend(self):
        log_json = ""
        # VALID
        with self.subTest("valid multisends commands"):
            try:
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("print"), list)
                log_json = {"group": "test_multisend", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_multisend", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend unit test FAILED: %s' % ass_err)
                xbridge_logger.logger.info('multisend("print") FAILED \n')
        # INVALID FIXED GARBAGE
        for basic_garbage_str in xbridge_utils.basic_garbage_list:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.multisend, basic_garbage_str, basic_garbage_str)
                    log_json = {"group": "test_signmessage", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_multisend", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_multisend unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_multisend unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_multisend", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        # INVALID RANDOM GARBAGE
        with self.subTest("random garbage"):
            try:
                self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.multisend, basic_garbage_str, basic_garbage_str)
                log_json = {"group": "test_multisend", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_multisend", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend unit test FAILED: %s' % ass_err)
                xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
            except JSONRPCException as json_excpt:
                xbridge_logger.logger.info('test_multisend unit test ERROR: %s' % str(json_excpt))
                log_json = {"group": "test_multisend", "success": 0,  "failure": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
            
            
    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_invalid(self):
        send_address_list = [xbridge_rpc.rpc_connection.sendtoaddress, xbridge_rpc.rpc_connection.sendtoaddressix]
        global set_of_invalid_parameters
        for send_address_func in send_address_list:
            # PARAMETER ORDER AND TYPE RANDOMNIZATION FOR INCREASED ENTROPY
            for i in range(1, 51):
                log_json = ""
                with self.subTest("sendfrom combinations"):
                    try:      
                        fromAccount = random.choice(set_of_invalid_parameters)
                        toblocknetdxaddress = random.choice(set_of_invalid_parameters)
                        amount = random.choice(set_of_invalid_parameters)
                        self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, fromAccount, toblocknetdxaddress, amount)
                        log_json = {"group": send_address_func, "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": send_address_func, "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('%s invalid unit subtest FAILED: %s' % (str(send_address_func), ass_err))
                    except JSONRPCException as json_excpt:
                        xbridge_logger.logger.info('%s unit test ERROR: %s' % (str(send_address_func), str(json_excpt))
                        log_json = {"group": send_address_func, "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
            with self.subTest("invalid sendtoaddress"):
                try:
                    log_json = ""
                    # THE TESTS WE WANT TO RUN EACH TIME
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", "")
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.ca_random_tx_id)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.ca_random_tx_id)
                    log_json = {"group": send_address_func, "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": send_address_func, "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s invalid unit test FAILED: %s' % (send_address_func, ass_err))
                    """
                    xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                    xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)
                    xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                    xbridge_logger.logger.info('invalid_random_positive_float: %s \n' % xbridge_utils.invalid_random_positive_float)
                    xbridge_logger.logger.info('valid_random_positive_float: %s \n' % xbridge_utils.valid_random_positive_float)
                    xbridge_logger.logger.info('fixed_positive_float: %s \n' % xbridge_utils.fixed_positive_float)
                    xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
                    """
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('%s unit test ERROR: %s' % (str(send_address_func), str(json_excpt)))
                    log_json = {"group": "test_multisend", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
            
            
    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    # JSONRPCException: -5: Invalid BlocknetDX address
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_valid(self):
        send_address_list = [xbridge_rpc.rpc_connection.sendtoaddress, xbridge_rpc.rpc_connection.sendtoaddressix]
        # valid_blocknet_address = xbridge_rpc.rpc_connection.getnewaddress()
        valid_blocknet_address = xbridge_utils.generate_random_valid_address()
        for send_address_func in send_address_list:
            log_json = ""
            with self.subTest("valid sendtoaddress"):
                try:        
                    self.assertIsInstance(send_address_func(valid_blocknet_address, xbridge_utils.valid_random_positive_int), dict)
                    self.assertIsInstance(send_address_func(valid_blocknet_address, xbridge_utils.valid_random_positive_float), dict)
                    self.assertIsInstance(send_address_func(valid_blocknet_address, xbridge_utils.fixed_positive_int), dict)
                    self.assertIsInstance(send_address_func(valid_blocknet_address, xbridge_utils.fixed_positive_float), dict)
                    # TESTME
                    # NEGATIVE NUMBERS
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, -xbridge_utils.xbridge_utils.valid_random_positive_float), dict)
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, -xbridge_utils.xbridge_utils.fixed_positive_int), dict)
                    # 0 SEND
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, 0), dict)
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.send_address_func(valid_blocknet_address, 0), dict)
                    log_json = {"group": send_address_func, "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": send_address_func, "success": 0, "failure": 1, "error": 0}
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
        global set_of_invalid_parameters
        # PARAMETER ORDER AND TYPE RANDOMNIZATION FOR INCREASED ENTROPY
        for i in range(1, 51):
            log_json = ""
            with self.subTest("sendfrom combinations"):
                try:      
                    fromAccount = random.choice(set_of_invalid_parameters)
                    toblocknetdxaddress = random.choice(set_of_invalid_parameters)
                    amount = random.choice(set_of_invalid_parameters)
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_comment = ""
                    else:
                        optional_comment = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_comment_to = ""
                    else:
                        optional_comment_to = random.choice([set_of_invalid_parameters])
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, fromAccount, toblocknetdxaddress, amount, optional_minconf, optional_comment, optional_comment_to)
                    log_json = {"group": "sendfrom", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "sendfrom", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('sendfrom invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('sendfrom unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "sendfrom", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        try:
            # OK
            # WE WANT TO TEST THESE EVERYTIME
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, " ", " ", " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.sendfrom, "", "", 0)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), -9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), 9999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, random.choice([True, False]), random.choice([True, False]), 0)
            # OK
            # WE WANT TO TEST THIS EVERYTIME
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, xbridge_utils.ca_random_tx_id, xbridge_utils.ca_random_tx_id, xbridge_utils.valid_random_positive_float)
            # NOT OK
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.ca_random_tx_id)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.invalid_random_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.invalid_random_positive_int)           
            log_json = {"group": "sendfrom", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "sendfrom", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('sendfrom invalid unit test FAILED: %s' % ass_err)     
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('sendfrom invalid unit test ERROR: %s' % str(json_excpt))
            log_json = {"group": "sendfrom", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)                
            
# unittest.main()
