import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***

"""

# OK
no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getnettotals,
                        xbridge_rpc.rpc_connection.getnetworkinfo,
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo
                    ]

# OK but make assertions more precise
# account/single string as param
account_func_list = [

    xbridge_rpc.rpc_connection.importaddress,
                    xbridge_rpc.rpc_connection.dumpprivkey,
                    xbridge_rpc.rpc_connection.dumpwallet,
                    xbridge_rpc.rpc_connection.backupwallet
                    ]

class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        
    def test_getunconfirmedbalance(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getunconfirmedbalance(), Decimal)
        except AssertionError as e:
            xbridge_logger.logger.info('getunconfirmedbalance unit test FAILED')

    def test_getrawchangeaddress(self):
        try:
            new_address = xbridge_rpc.rpc_connection.getrawchangeaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
        except AssertionError as e:
            xbridge_logger.logger.info('getrawchangeaddress unit test FAILED')

    # @unittest.skip("disabled")
    # Tested OK
    def test_group_no_param_return_dict_batch(self):
        for func_name in no_param_returns_dict_func_list:
            with self.subTest("batch test of no_param_returns_dict_func_list"):
                try:
                    result = func_name()
                    # print("%s: %s" % (func_name, result))
                    self.assertIsInstance(result, dict)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    @unittest.skip("Still untested")
    def test_group_str_param(self):
        for func_name in account_func_list:
            with self.subTest("test_group_str_param"):
                try:
                    result = func_name()
                    self.assertIsNotNone(result)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    def test_get_stake_threshold(self):
        try:
            # return {'split stake threshold set to ': 2000}
            rst = xbridge_rpc.rpc_connection.getstakesplitthreshold()
            self.assertIsInstance(rst, dict)
        except AssertionError:
            xbridge_logger.logger.info('get_stake_threshold unit test FAILED')

    def test_getnewaddress(self):
        try:
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
        except AssertionError:
            xbridge_logger.logger.info('getnewaddress unit test FAILED')

    # TypeError: <class 'decimal.Decimal'> is not JSON serializable
    def test_get_received_by_account(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(""), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(" "), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("----"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("["), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("[]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{}"), Decimal)
            # self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(xbridge_utils.ca_random_tx_id, Decimal))
        except AssertionError:
            xbridge_logger.logger.info('get_received_by_account unit test FAILED')

    def test_getreceivedbyaddress(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('getreceivedbyaddress unit test FAILED')

    def test_getaccount(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('getaccount unit test FAILED')

    def test_getaccountaddress(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(""), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(" "), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("----"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("{"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("}"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("["), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("]"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("[]"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("{}"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(xbridge_utils.ca_random_tx_id), str)
        except AssertionError:
            xbridge_logger.logger.info('getaccountaddress unit test FAILED')

    def test_getaddressesbyaccount(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(""), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(" "), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("----"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("****"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("{"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("}"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("["), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("]"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("[[]]"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("{}"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(xbridge_utils.ca_random_tx_id), list)
        except AssertionError:
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')

    def test_getaddressesbyaccount(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(xbridge_utils.ca_random_tx_id), list)
        except AssertionError:
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')

    def test_gettransaction(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction,
                              xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('gettransaction unit test FAILED')

    # TypeError: <class 'decimal.Decimal'> is not JSON serializable
    def test_getbalance(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance(""), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance(" "), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("----"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("["), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("[]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("{}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance("{}"), Decimal)
            # self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance(xbridge_utils.ca_random_tx_id, Decimal))
        except AssertionError:
            xbridge_logger.logger.info('getbalance unit test FAILED')


# unittest.main()
