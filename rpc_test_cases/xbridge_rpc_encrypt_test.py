import unittest, time
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

    # walletpassphrasechange "oldpassphrase" "newpassphrase"
    def test_walletpassphrasechange_valid(self):
        try:
            if xbridge_config.get_wallet_decryption_passphrase() == "":
                return
            current_valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
            random_valid_new_passphrase = xbridge_utils.generate_random_valid_passphrase()
            xbridge_rpc.walletpassphrasechange(current_valid_passphrase, random_valid_new_passphrase)
            xbridge_logger.XLOG("test_walletpassphrasechange_valid", 0)
            self.assertIsNone(xbridge_rpc.walletpassphrasechange(random_valid_new_passphrase, current_valid_passphrase))
            xbridge_logger.XLOG("test_walletpassphrasechange_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_walletpassphrasechange_valid", 1, ass_err, [current_valid_passphrase, random_valid_new_passphrase])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_walletpassphrasechange_valid", 2, json_excpt, [current_valid_passphrase, random_valid_new_passphrase])
        
    # walletpassphrasechange "oldpassphrase" "newpassphrase"
    def test_walletpassphrasechange_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_walletpassphrasechange_invalid"):
                try:
                    old_pwd = random.choice(xbridge_utils.set_of_invalid_parameters)
                    new_pwd = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.walletpassphrasechange, old_pwd, new_pwd)
                    xbridge_logger.XLOG("test_walletpassphrasechange_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_walletpassphrasechange_invalid", 1, ass_err, [old_pwd, new_pwd])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_walletpassphrasechange_invalid", 2, json_excpt, [old_pwd, new_pwd])

    # walletpassphrase "passphrase" timeout ( anonymizeonly )
    # @unittest.skip("IN TESTING")
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
            xbridge_logger.XLOG("test_walletpassphrase_invalid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_walletpassphrasechange_invalid", 1, ass_err, [random_str, random_int, random_bool])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_walletpassphrasechange_invalid", 2, json_excpt, [random_str, random_int, random_bool])

    # This test group tests walletpassphrase + dump + walletlock
    # walletpassphrase "passphrase" timeout ( anonymizeonly )
    # @unittest.skip("WAITING FOR API RETURN VALUES TO BE FIXED")
    def test_walletpassphrase_valid(self):
        try:
            log_json = ""
            if xbridge_config.get_wallet_decryption_passphrase() == "":
                return
            valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            self.assertIsNone(xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False))
            time_str = time.strftime("%Y%m%d-%H%M%S")
            dumped_wallet_str = xbridge_config.get_conf_log_dir() + time_str + "_dumped_wallet.dat"
            self.assertIsNone(xbridge_utils.rpc_connection.dumpwallet(dumped_wallet_str))
            self.assertIsNone(xbridge_rpc.walletlock())
            xbridge_logger.XLOG("test_walletpassphrase_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_walletpassphrase_valid", 1, ass_err, [dumped_wallet_str])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_walletpassphrase_valid", 2, json_excpt, [dumped_wallet_str])

    """
    @unittest.skip("DO NOT TEST")
    def test_encryptwallet_noseq(self):
        try:
            log_json = ""
            random_str = random.choice([xbridge_utils.invalid_str_from_random_classes_1, 
                                        xbridge_utils.invalid_str_from_random_classes_2, 
                                        xbridge_utils.invalid_str_from_random_classes_3, 
                                        xbridge_utils.invalid_str_from_random_classes_4])
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.rpc_connection.encryptwallet, random_str)
            xbridge_logger.XLOG("test_encryptwallet_noseq", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_encryptwallet_noseq", 1, ass_err, [random_str])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_encryptwallet_noseq", 2, json_excpt, [random_str])
    """

    def test_bip38encrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38encrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38encrypt, invalid_blocknet_address)
                    xbridge_logger.XLOG("test_bip38encrypt_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_bip38encrypt_invalid", 1, ass_err, [invalid_blocknet_address])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_bip38encrypt_invalid", 2, json_excpt, [invalid_blocknet_address])
    
    def test_bip38decrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38decrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38decrypt,
                                      invalid_blocknet_address)
                    xbridge_logger.XLOG("test_bip38decrypt_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_bip38decrypt_invalid", 1, ass_err, [invalid_blocknet_address])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_bip38decrypt_invalid", 2, json_excpt, [invalid_blocknet_address])
    
# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(50):
    suite.addTest(Encrypt_UnitTest("test_walletpassphrase_valid"))
    suite.addTest(Encrypt_UnitTest("test_walletpassphrase_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""