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
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class send_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # multisend <command>
    def test_multisend_valid_1(self):
        log_json = ""
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("print"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("enableall"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("disable"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("deactivate"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("clear"), dict)
            log_json = {"group": "test_multisend_valid_1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_multisend_valid_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_multisend_valid_1 FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_multisend_valid_1 ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_multisend_valid_1", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    @unittest.skip("IN REVIEW")
    def test_multisend_valid_2(self):
            log_json = ""
            valid_blocknet_address = xbridge_utils.generate_valid_blocknet_address()
            try:
                # self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("disable", valid_blocknet_address), list)
                # self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("deactivate", valid_blocknet_address), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.multisend("delete", valid_blocknet_address), list)
                log_json = {"group": "test_multisend_valid_2", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_multisend_valid_2", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('test_multisend_valid_2 FAILED: %s' % ass_err)
                if MAX_LOG_LENGTH > 0:
                    xbridge_logger.logger.info('param: %s \n' % str(valid_blocknet_address)[:MAX_LOG_LENGTH])
            except JSONRPCException as json_excpt:
                xbridge_logger.logger.info('test_multisend_valid_2 ERROR: %s' % str(json_excpt))
                log_json = {"group": "test_multisend_valid", "success": 0, "failure": 0, "error": 1}
                xbridge_utils.ERROR_LOG.append(log_json)
                if MAX_LOG_LENGTH > 0:
                    xbridge_logger.logger.info('param: %s \n' % str(valid_blocknet_address)[:MAX_LOG_LENGTH])

    # multisend <command>
    @unittest.skip("TEMPORARILY DISABLED - IN REVIEW")
    def test_multisend_invalid(self):
        for i in range(subTest_count):
            with self.subTest("comb"):
                try:
                    random_elt = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.multisend, random_elt)
                    log_json = {"group": "test_multisend_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_multisend_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_multisend_invalid FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(random_elt)[:MAX_LOG_LENGTH])
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_multisend_invalid ERROR: %s' % str(json_excpt))
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('param: %s \n' % str(random_elt)[:MAX_LOG_LENGTH])
                    log_json = {"group": "test_multisend_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)

    # sendtoaddress "blocknetdxaddress" amount ( "comment" "comment-to" )
    # sendtoaddressix "blocknetdxaddress" amount ( "comment" "comment-to" )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_senttoaddress_invalid_random(self):
        send_address_list = [xbridge_rpc.sendtoaddress, xbridge_rpc.sendtoaddressix]
        for send_address_func in send_address_list:
            for i in range(subTest_count):
                log_json = ""
                with self.subTest("test_senttoaddress_invalid_random"):
                    try:
                        blocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                        amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                        if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                            optional_comment = None
                        else:
                            optional_comment = random.choice(xbridge_utils.set_of_invalid_parameters)
                        if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                            optional_comment_to = None
                        else:
                            optional_comment_to = random.choice(xbridge_utils.set_of_invalid_parameters)
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException,
                                          send_address_func, blocknetdxaddress, amount, optional_comment, optional_comment_to)
                        log_json = {"group": send_address_func, "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        log_json = {"group": "sendtoaddress", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('%s FAILED: %s' % (str(send_address_func), ass_err))
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('blocknetdxaddress: %s' % str(blocknetdxaddress)[:MAX_LOG_LENGTH])
                            xbridge_logger.logger.info('amount: %s' % str(amount)[:MAX_LOG_LENGTH])
                            xbridge_logger.logger.info('optional_comment: %s' % str(optional_comment)[:MAX_LOG_LENGTH])
                            xbridge_logger.logger.info('optional_comment_to: %s' % str(optional_comment_to)[:MAX_LOG_LENGTH])
                    except JSONRPCException as json_excpt:
                        xbridge_logger.logger.info('%s ERROR: %s' % (str(send_address_func), str(json_excpt)))
                        log_json = {"group": "sendtoaddress", "success": 0,  "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('blocknetdxaddress: %s' % str(blocknetdxaddress)[:MAX_LOG_LENGTH])
                        if MAX_LOG_LENGTH > 0:
                            xbridge_logger.logger.info('amount: %s' % str(amount)[:MAX_LOG_LENGTH])
                            xbridge_logger.logger.info('optional_comment: %s' % str(optional_comment)[:MAX_LOG_LENGTH])
                            xbridge_logger.logger.info('optional_comment_to: %s' % str(optional_comment_to)[:MAX_LOG_LENGTH])

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
                    self.assertRaises(JSONRPCException, send_address_func, "", "")
                    self.assertRaises(JSONRPCException, send_address_func, False, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, send_address_func, True, -9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, send_address_func, False, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, send_address_func, True, 9999999999999999999999999999999999999)
                    self.assertRaises(JSONRPCException, send_address_func, False, 0)
                    self.assertRaises(JSONRPCException, send_address_func, True, 0)
                    self.assertRaises(JSONRPCException, send_address_func, False, xbridge_utils.ca_random_tx_id)
                    self.assertRaises(JSONRPCException, send_address_func, True, xbridge_utils.ca_random_tx_id)
                    log_json = {"group": "test_senttoaddress_invalid_fixed", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_senttoaddress_invalid_fixed", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s invalid unit test FAILED: %s' % (str(send_address_func), str(ass_err)))
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('random_tx_id: %s \n' % str(xbridge_utils.ca_random_tx_id)[:MAX_LOG_LENGTH])

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
                        optional_minconf = None
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment = None
                    else:
                        optional_comment = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment_to = None
                    else:
                        optional_comment_to = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.sendfrom, fromAccount, toblocknetdxaddress, amount, optional_minconf, optional_comment, optional_comment_to)
                    xbridge_logger.XLOG("test_sendfrom_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_sendfrom_invalid", 1, ass_err, [fromAccount, toblocknetdxaddress, amount, optional_minconf, optional_comment,optional_comment_to])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_sendfrom_invalid", 2, json_excpt, [fromAccount, toblocknetdxaddress, amount, optional_minconf, optional_comment,optional_comment_to])


# unittest.main()

"""
print(xbridge_rpc.rpc_connection.walletpassphrase("mypwd", 60, False))

suite = unittest.TestSuite()
for i in range(1):
    suite.addTest(send_UnitTest("test_multisend_valid_1"))
    # suite.addTest(Encrypt_UnitTest("test_walletpassphrasechange_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""
