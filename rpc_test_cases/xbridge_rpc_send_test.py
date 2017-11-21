import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class send_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # multisend <command>
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_multisend_valid(self):
        log_json = ""
        valid_blocknet_address = xbridge_utils.generate_valid_blocknet_address()
        with self.subTest("valid multisends commands"):
            try:
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("print"), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("enableall"), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("disable"), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("disable", valid_blocknet_address), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("deactivate"), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("deactivate", valid_blocknet_address), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("delete", valid_blocknet_address), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("clear"), dict)
                log_json = {"group": "test_multisend_valid", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_multisend", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend unit test FAILED: %s' % ass_err)
                xbridge_logger.logger.info('multisend("print") FAILED \n')

    # multisend <command>
    def test_multisend_invalid(self):
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

    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_invalid_random(self):
        send_address_list = [xbridge_rpc.rpc_connection.sendtoaddress, xbridge_rpc.rpc_connection.sendtoaddressix]
        for send_address_func in send_address_list:
            for i in range(subTest_count):
                log_json = ""
                with self.subTest("sendfrom combinations"):
                    try:      
                        fromAccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                        toblocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                        amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                        self.assertRaises(JSONRPCException, send_address_func, fromAccount, toblocknetdxaddress, amount)
                        log_json = {"group": send_address_func, "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "sendtoaddress", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('%s invalid unit subtest FAILED: %s' % (str(send_address_func), ass_err))
                    except JSONRPCException as json_excpt:
                        xbridge_logger.logger.info('%s unit test ERROR: %s' % (str(send_address_func), str(json_excpt)))
                        log_json = {"group": "sendtoaddress", "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)

    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    def test_senttoaddress_invalid_fixed(self):
        send_address_list = [xbridge_rpc.sendtoaddress, xbridge_rpc.sendtoaddressix]
        valid_blocknet_address = xbridge_utils.generate_valid_blocknet_address()
        for send_address_func in send_address_list:
            with self.subTest("test_senttoaddress_invalid_fixed"):
                try:
                    log_json = ""
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException,
                        send_address_func, valid_blocknet_address, -xbridge_utils.valid_random_positive_float)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException,
                                      send_address_func, valid_blocknet_address, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, "", "")
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, 0)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, False, xbridge_utils.ca_random_tx_id)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.send_address_func, True, xbridge_utils.ca_random_tx_id)
                    log_json = {"group": "test_senttoaddress_invalid_fixed", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_senttoaddress_invalid_fixed", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s invalid unit test FAILED: %s' % (send_address_func, ass_err))
                    xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                    xbridge_logger.logger.info('invalid_random_positive_int: %s \n' % xbridge_utils.invalid_random_positive_int)
                    xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                    xbridge_logger.logger.info('invalid_random_positive_float: %s \n' % xbridge_utils.invalid_random_positive_float)
                    xbridge_logger.logger.info('valid_random_positive_float: %s \n' % xbridge_utils.valid_random_positive_float)
                    xbridge_logger.logger.info('fixed_positive_float: %s \n' % xbridge_utils.fixed_positive_float)
                    xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)

    # sendfrom "fromaccount" "toblocknetdxaddress" amount ( minconf "comment" "comment-to" )
    def test_sendfrom_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("sendfrom combinations"):
                try:      
                    fromAccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    toblocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                    amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment = ""
                    else:
                        optional_comment = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment_to = ""
                    else:
                        optional_comment_to = random.choice(xbridge_utils.set_of_invalid_parameters)
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


# unittest.main()

"""
print(xbridge_rpc.rpc_connection.walletpassphrase("mypwd", 60, False))

suite = unittest.TestSuite()
for i in range(1):
    suite.addTest(send_UnitTest("test_senttoaddress_valid"))
    # suite.addTest(Encrypt_UnitTest("test_walletpassphrasechange_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

