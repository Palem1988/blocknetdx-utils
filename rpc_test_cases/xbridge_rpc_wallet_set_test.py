import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class wallet_Set_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        self.random_neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
            -0.0000000000000000000000000000000000000000000000000000000000001)
        self.random_large_positive_nb = xbridge_utils.generate_random_number(999999999999999999999999,
                                                                 99999999999999999999999999999999999999999999999999999999999999999999999999)
        self.random_large_positive_int = xbridge_utils.generate_random_number(999999999999999999999999,
                                                                             99999999999999999999999999999999999999999999999999999999999999999999999999)
        self.fixed_negative_number = -10
        self.fixed_positive_number = 10
        self.positive_float = 10.2
        self.fixed_small_positive_number = 0.00000000000000000000000000000000000000000000000000000001
        self.valid_random_positive_number = xbridge_utils.generate_random_number(0, 1000)
        self.valid_random_positive_int = xbridge_utils.generate_random_int(0, 1000)
        # self.valid_blocknet_address = xbridge_rpc.rpc_connection.getnewaddress()
        self.valid_blocknet_address = xbridge_utils.generate_random_valid_address()
        self.invalid_blocknet_address = xbridge_utils.c_src_Address
        self.invalid_account_str = xbridge_utils.invalid_account_str
        self.valid_account_str = xbridge_utils.valid_account_str

    def test_setfee(self):
        try:
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(0))
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(self.fixed_positive_number))
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(self.fixed_small_positive_number))
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, self.fixed_negative_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, self.random_neg_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, self.random_large_positive_nb)
        except AssertionError:
            xbridge_logger.logger.info('****** test_setfee unit test FAILED ******')

    # Only int are accepted
    # Error: Unlock wallet to use this feature
    def test_set_stake_split_threshold(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(0), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(self.fixed_positive_number), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(self.valid_random_positive_int), dict)
            # Errors
            self.assertIsInstance(xbridge_rpc.rpc_connection.setstakesplitthreshold(self.fixed_negative_number), str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.random_neg_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.fixed_small_positive_number)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, self.positive_float)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setstakesplitthreshold, xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('****** set_stake_split_threshold unit test FAILED ******\n')
            xbridge_logger.logger.info('random_tx_id: \n %s \n' % xbridge_utils.ca_random_tx_id)

    def test_set_account(self):
        try:
            self.assertIsNone(xbridge_rpc.rpc_connection.setaccount(self.valid_blocknet_address, self.invalid_account_str))
            self.assertIsNone(xbridge_rpc.rpc_connection.setaccount(self.valid_blocknet_address, self.valid_account_str))
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setaccount, self.invalid_blocknet_address, self.invalid_account_str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.setaccount, self.invalid_blocknet_address, self.valid_account_str)
        except AssertionError:
            xbridge_logger.logger.info('****** setaccount unit test FAILED ****** \n')
            xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % self.invalid_blocknet_address)
            xbridge_logger.logger.info('valid_blocknet_address: %s \n' % self.valid_blocknet_address)
            xbridge_logger.logger.info('invalid_account_str: %s \n' % self.invalid_account_str)
            xbridge_logger.logger.info('valid_account_str: %s \n' % self.valid_account_str)

# unittest.main()
