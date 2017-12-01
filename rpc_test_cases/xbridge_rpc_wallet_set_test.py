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

subTest_count = xbridge_config.get_conf_subtests_run_number()

class wallet_Set_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
        self.random_neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
            -0.0000000000000000000000000000000000000000000000000000000000001)
        self.random_large_positive_nb = xbridge_utils.generate_random_number(999999999999999999999999,
                                                                 99999999999999999999999999999999999999999999999999999999999999999999999999)
        self.random_large_positive_int = xbridge_utils.generate_random_number(999999999999999999999999,
                                                                             99999999999999999999999999999999999999999999999999999999999999999999999999)
        self.positive_float = 10.2
        self.sm_positive_nb = xbridge_utils.generate_random_number(0.00000000000000000000000000000000000000000000000000000001, 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)       
        self.valid_random_positive_number = xbridge_utils.generate_random_number(0, 1000)
        self.valid_random_positive_int = xbridge_utils.generate_random_int(0, 1000)
        self.valid_blocknet_address = xbridge_utils.generate_random_valid_address()
        self.invalid_blocknet_address = xbridge_utils.c_src_Address
        self.invalid_account_str = xbridge_utils.invalid_account_str
        self.valid_account_str = xbridge_utils.valid_account_str

    # settxfee amount
    def test_settxfee_valid(self):
        try:
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(0))
            random_valid_positive_nb = xbridge_utils.generate_random_number(0.01, 99999)
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(random_valid_positive_nb))
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(self.sm_positive_nb))
            xbridge_logger.XLOG("test_settxfee_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_settxfee_valid", 1, ass_err, [random_valid_positive_nb, self.sm_positive_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_settxfee_valid", 2, json_excpt, [random_valid_positive_nb, self.sm_positive_nb])

    # settxfee amount
    def test_settxfee_invalid_nbs(self):
        try:
            random_invalid_nb = xbridge_utils.generate_random_number(-9999999999999999999999999999999999, -0.00000000000000001)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.settxfee, random_invalid_nb)
            log_json = {"group": "test_settxfee_invalid_nbs", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_settxfee_invalid_nbs", 1, ass_err, [random_invalid_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_settxfee_invalid_nbs", 2, json_excpt, [random_invalid_nb])

    # settxfee amount
    def test_settxfee_invalid(self):
        set_without_numbers = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int) and not isinstance(x, float)]                    
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_senttoaddress_invalid_random"):
                try:
                    amount = random.choice(set_without_numbers)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.settxfee, amount)
                    xbridge_logger.XLOG("test_settxfee_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_settxfee_invalid", 1, ass_err, [amount])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_settxfee_invalid", 2, json_excpt, [amount])

    # Only int are accepted
    # Error: Unlock wallet to use this feature
    def test_setstakesplitthreshold_valid(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(0), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(self.valid_random_positive_int), dict)
            xbridge_logger.XLOG("test_setstakesplitthreshold_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_setstakesplitthreshold_valid", 1, ass_err, [self.valid_random_positive_int])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_setstakesplitthreshold_valid", 2, json_excpt, [self.valid_random_positive_int])
            
    def test_setstakesplitthreshold_invalid(self):
        try:
            if xbridge_config.get_wallet_decryption_passphrase() == "":
                return
            valid_passphrase = xbridge_config.get_wallet_decryption_passphrase()
            random_int = xbridge_utils.generate_random_int(-999999999999, 999999999999)
            xbridge_rpc.walletpassphrase(valid_passphrase, random_int, False)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_neg_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.sm_positive_nb)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, xbridge_utils.ca_random_tx_id)
            xbridge_logger.XLOG("test_setstakesplitthreshold_invalid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_setstakesplitthreshold_valid", 1, ass_err, [self.random_large_positive_int, self.random_neg_number, self.positive_float, 
                                                                                                                self.sm_positive_nb, xbridge_utils.ca_random_tx_id])

    def test_setaccount_invalid(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setaccount, self.invalid_blocknet_address, self.invalid_account_str)
            xbridge_logger.XLOG("test_setaccount", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_setstakesplitthreshold_valid", 1, ass_err, [self.random_large_positive_int, self.invalid_blocknet_address, self.invalid_account_str])
            
# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(1):
    suite.addTest(wallet_Set_UnitTest("test_settxfee_invalid"))
    # suite.addTest(Encrypt_UnitTest("test_walletpassphrasechange_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""