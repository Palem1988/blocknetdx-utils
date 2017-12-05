import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_getinfo(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getinfo(), dict)
            log_json = {"group": "test_getinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    # signmessage "blocknetdxaddress" "message"
    # Please enter the wallet passphrase with walletpassphrase first.
    # TODO: valid test
    # True, False, returns None
    @unittest.skip("IN REVIEW")
    def test_signmessage_invalid(self):
        if xbridge_config.get_wallet_decryption_passphrase() == "":
            return
        valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
        random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
        xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False)
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_signmessage_invalid"):
                try:
                    invalid_blocknet_address = random.choice(custom_set)
                    message = random.choice(custom_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.signmessage, invalid_blocknet_address, message)
                    log_json = {"group": "test_signmessage_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_signmessage_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage_invalid FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info(
                            'invalid_blocknet_address: %s \n' % str(invalid_blocknet_address)[:MAX_LOG_LENGTH])
                        xbridge_logger.logger.info('param: %s \n' % str(message)[:MAX_LOG_LENGTH])
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_signmessage_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage_invalid ERROR: %s' % json_excpt)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % str(invalid_blocknet_address)[:MAX_LOG_LENGTH])
                        xbridge_logger.logger.info('param: %s \n' % str(message)[:MAX_LOG_LENGTH])

    # autocombinerewards <true/false> threshold
    def test_autocombinerewards_valid(self):
        try:
            if xbridge_config.get_wallet_decryption_passphrase() == "":
                return
            valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False)
            log_json = ""
            success_str = "Auto Combine Rewards Threshold Set"
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.VALID_DATA)            
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, -99999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, 0), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.valid_random_positive_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, -xbridge_utils.valid_random_positive_int), success_str)
            log_json = {"group": "test_autocombinerewards_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_autocombinerewards_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_autocombinerewards_valid FAILED: %s' % ass_err)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('fixed_positive_int: %s \n' % str(xbridge_utils.fixed_positive_int))
                xbridge_logger.logger.info('fixed_negative_int: %s \n' % str(xbridge_utils.fixed_negative_int))
                xbridge_logger.logger.info('valid_random_positive_int: %s \n' % str(xbridge_utils.valid_random_positive_int))
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_autocombinerewards_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_autocombinerewards_valid ERROR: %s' % json_excpt)

    # autocombinerewards <true/false> threshold
    def test_autocombinerewards_invalid(self):
        set_without_bools = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
        set_without_int = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("autocombinerewards combinations"):
                try:      
                    true_false = random.choice(set_without_bools)
                    threshold = random.choice(set_without_int)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, true_false, threshold)
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.autocombinerewards, true_false, threshold)
                    log_json = {"group": "test_autocombinerewards_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_autocombinerewards_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_autocombinerewards_invalid FAILED: %s' % ass_err)
                    if MAX_LOG_LENGTH > 0:
                        xbridge_logger.logger.info('true_false: %s' % str(true_false)[:MAX_LOG_LENGTH])
                        xbridge_logger.logger.info('threshold: %s' % str(threshold)[:MAX_LOG_LENGTH])

    # move "fromaccount" "toaccount" amount ( minconf "comment" )
    def test_move_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("move combinations"):
                try:      
                    fromAccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    toaccount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = None
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_comment = None
                    else:
                        optional_comment = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.move, fromAccount, toaccount, amount, optional_minconf, optional_comment)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.move, fromAccount, toaccount, amount,
                                      optional_minconf, optional_comment)
                    xbridge_logger.XLOG("test_move_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_move_invalid", 1, ass_err, [fromAccount, toaccount, amount, optional_minconf, optional_comment])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_move_invalid", 2, json_excpt, [fromAccount, toaccount, amount, optional_minconf, optional_comment])

    # lockunspent unlock [{"txid":"txid","vout":n},...]
    def test_lockunspent_invalid(self):
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    unlock_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    transactions = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.lockunspent, unlock_param, transactions)
                    xbridge_logger.XLOG("test_lockunspent_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_lockunspent_invalid", 1, ass_err, [unlock_param, transactions])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_move_invalid", 2, json_excpt, [unlock_param, transactions])


# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(20):
    suite.addTest(Misc_UnitTest("test_bip38encrypt_invalid"))
    suite.addTest(Misc_UnitTest("test_bip38decrypt_invalid"))
    # suite.addTest(Misc_UnitTest("test_signmessage_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

