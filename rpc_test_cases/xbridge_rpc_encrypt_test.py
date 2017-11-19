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

class Encrypt_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # walletpassphrase "passphrase" timeout ( anonymizeonly )
    @unittest.skip("IN TESTING")
    def test_walletpassphrasechange_valid(self):
        try:
            log_json = ""
            random_str = random.choice([xbridge_utils.invalid_str_from_random_classes_1,
                                        xbridge_utils.invalid_str_from_random_classes_2,
                                        xbridge_utils.invalid_str_from_random_classes_3,
                                        xbridge_utils.invalid_str_from_random_classes_4])
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            if random.choice(["", random.choice([True, False])]) == "":
                random_bool = None
            else:
                random_bool = random.choice([True, False])
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.walletpassphrase,
                              random_str, random_int, random_bool)
            log_json = {"group": "test_walletpassphrasechange_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_walletpassphrasechange_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_walletpassphrasechange_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('random_str: %s' % random_str)
            xbridge_logger.logger.info('random_int: %s' % str(random_int))
            xbridge_logger.logger.info('random_bool: %s' % random_bool)

    # walletpassphrase "passphrase" timeout ( anonymizeonly )
    @unittest.skip("IN TESTING")
    def test_walletpassphrase_invalid(self):
        try:
            log_json = ""
            random_str = random.choice([xbridge_utils.invalid_str_from_random_classes_1,
                                        xbridge_utils.invalid_str_from_random_classes_2,
                                        xbridge_utils.invalid_str_from_random_classes_3,
                                        xbridge_utils.invalid_str_from_random_classes_4])
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            if random.choice(["", random.choice([True, False])]) == "":
                random_bool = None
            else:
                random_bool = random.choice([True, False])
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.walletpassphrase, random_str, random_int, random_bool)
            log_json = {"group": "test_walletpassphrase", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_walletpassphrase", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_walletpassphrase", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('random_str: %s' % random_str)
            xbridge_logger.logger.info('random_int: %s' % str(random_int))
            xbridge_logger.logger.info('random_bool: %s' % random_bool)

    # walletpassphrase "passphrase" timeout ( anonymizeonly )
    @unittest.skip("IN TESTING")
    def test_walletpassphrase_valid(self):
        try:
            log_json = ""
            valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            random_bool = random.choice([True, False])
            self.assertIsNone(xbridge_rpc.walletpassphrase(valid_passphrase, random_int, random_bool))
            log_json = {"group": "test_walletpassphrase", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_walletpassphrase", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_walletpassphrase", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('random_str: %s' % valid_passphrase)
            xbridge_logger.logger.info('random_int: %s' % str(random_int))
            xbridge_logger.logger.info('random_bool: %s' % random_bool)

    @unittest.skip("NEED A SPECIAL FLAG SO IT DOES NOT SHUTDOWN")
    def test_encryptwallet_noseq(self):
        try:
            log_json = ""
            random_str = random.choice([xbridge_utils.invalid_str_from_random_classes_1, 
                                        xbridge_utils.invalid_str_from_random_classes_2, 
                                        xbridge_utils.invalid_str_from_random_classes_3, 
                                        xbridge_utils.invalid_str_from_random_classes_4])
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.rpc_connection.encryptwallet, random_str)
            log_json = {"group": "test_encryptwallet", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_encryptwallet", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_encryptwallet", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
    
    def test_bip38encrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38encrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38encrypt, invalid_blocknet_address)
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38encrypt_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38encrypt_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
    
    def test_bip38decrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38decrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38decrypt,
                                      invalid_blocknet_address)
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38decrypt_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38decrypt_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
    
    
# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(20):
    suite.addTest(Encrypt_UnitTest("test_bip38encrypt_invalid"))
    suite.addTest(Encrypt_UnitTest("test_bip38decrypt_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

