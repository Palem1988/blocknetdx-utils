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
        self.fixed_small_positive_number = 0.00000000000000000000000000000000000000000000000000000001
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
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(self.fixed_small_positive_number))
            log_json = {"group": "test_settxfee_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_settxfee_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_settxfee_valid FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('random_valid_positive_nb: %s \n' % random_valid_positive_nb)
            xbridge_logger.logger.info('fixed_small_positive_number: %s \n' % self.fixed_small_positive_number)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_settxfee_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_settxfee_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('random_valid_positive_nb: %s \n' % random_valid_positive_nb)
            xbridge_logger.logger.info('fixed_small_positive_number: %s \n' % self.fixed_small_positive_number)

    # settxfee amount
    def test_settxfee_invalid_nbs(self):
        try:
            random_invalid_nb = xbridge_utils.generate_random_number(-0.00000000000000001,
                                                                     -9999999999999999999999999999999999)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.settxfee, random_invalid_nb)
            log_json = {"group": "test_settxfee_invalid_nbs", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_settxfee_invalid_nbs", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_settxfee_invalid_nbs FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('random_invalid_nb: %s \n' % random_invalid_nb)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_settxfee_invalid_nbs ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_settxfee_invalid_nbs", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('random_invalid_nb: %s \n' % random_invalid_nb)

    # settxfee amount
    def test_settxfee_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_senttoaddress_invalid_random"):
                try:
                    custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int) and not isinstance(x, float)]
                    amount = random.choice(custom_set)
                    # self.assertRaises(JSONRPCException, xbridge_rpc.settxfee, amount)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.settxfee, amount)
                    log_json = {"group": "test_settxfee_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_settxfee_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_settxfee_invalid FAILED: %s \n' % ass_err)
                    xbridge_logger.logger.info('amount: %s \n' % amount)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_settxfee_invalid ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('amount: %s \n' % amount)
                    log_json = {"group": "test_setfee", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)

    # Only int are accepted
    # Error: Unlock wallet to use this feature
    def test_setstakesplitthreshold_valid(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(0), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(self.valid_random_positive_int), dict)
            log_json = {"group": "test_setstakesplitthreshold_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_setstakesplitthreshold_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_setstakesplitthreshold_valid FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % self.valid_random_positive_int)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_setstakesplitthreshold_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_setstakesplitthreshold_valid", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % self.valid_random_positive_int)
            
    def test_setstakesplitthreshold_invalid(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_neg_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.fixed_small_positive_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, xbridge_utils.ca_random_tx_id)
            log_json = {"group": "test_setstakesplitthreshold_invalid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_setstakesplitthreshold_invalid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_setstakesplitthreshold_invalid FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('random_tx_id: \n %s \n' % xbridge_utils.ca_random_tx_id)

    def test_setaccount(self):
        try:
            self.assertIsNone(xbridge_rpc.rpc_connection.setaccount(self.valid_blocknet_address, self.invalid_account_str))
            self.assertIsNone(xbridge_rpc.rpc_connection.setaccount(self.valid_blocknet_address, self.valid_account_str))
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setaccount, self.invalid_blocknet_address, self.invalid_account_str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setaccount, self.invalid_blocknet_address, self.valid_account_str)
            log_json = {"group": "test_setaccount", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_setaccount", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_setaccount FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % self.invalid_blocknet_address)
            xbridge_logger.logger.info('valid_blocknet_address: %s \n' % self.valid_blocknet_address)
            xbridge_logger.logger.info('invalid_account_str: %s \n' % self.invalid_account_str)
            xbridge_logger.logger.info('valid_account_str: %s \n' % self.valid_account_str)


# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(1):
    suite.addTest(wallet_Set_UnitTest("test_settxfee_invalid"))
    # suite.addTest(Encrypt_UnitTest("test_walletpassphrasechange_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

