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

class wallet_File_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_importwallet_invalid(self):
        if xbridge_config.get_wallet_decryption_passphrase() == "":
            return
        # print("wallet passphrase: " + xbridge_config.get_wallet_decryption_passphrase())
        valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
        random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
        random_bool = random.choice([True, False])
        self.assertIsNone(xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False))
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.importwallet, basic_garbage_str)
                    xbridge_logger.XLOG("test_importwallet_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_importwallet_invalid", 1, ass_err, [basic_garbage_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_importwallet_invalid", 2, json_excpt, [basic_garbage_str])

    def test_backupwallet_invalid(self):
        if xbridge_config.get_wallet_decryption_passphrase() == "":
            return
        # print("wallet passphrase: " + xbridge_config.get_wallet_decryption_passphrase())
        valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
        random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
        random_bool = random.choice([True, False])
        self.assertIsNone(xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False))
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertIsNone(xbridge_rpc.rpc_connection.backupwallet, basic_garbage_str)
                    xbridge_logger.XLOG("test_backupwallet_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_backupwallet_invalid", 1, ass_err, [basic_garbage_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_backupwallet_invalid", 2, json_excpt, [basic_garbage_str])

# unittest.main()
