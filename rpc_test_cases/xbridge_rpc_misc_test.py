import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS FOR ALL WALLET RELATED FUNCTIONS STARTING WITH GET ***
"""

# OK
no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getnettotals,
                        xbridge_rpc.rpc_connection.getnetworkinfo,
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo
                    ]

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
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getunconfirmedbalance(), Decimal)
            logstr = {"group": "test_getunconfirmedbalance", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as e:
            logstr = {"group": "test_getunconfirmedbalance", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getunconfirmedbalance unit test FAILED')

    def test_getrawchangeaddress(self):
        try:
            log_json = ""
            new_address = xbridge_rpc.rpc_connection.getrawchangeaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            logstr = {"group": "test_getrawchangeaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as e:
            logstr = {"group": "test_getrawchangeaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getrawchangeaddress unit test FAILED')

    # @unittest.skip("disabled")
    # Tested OK
    def test_group_no_param_return_dict_batch(self):
        for func_name in no_param_returns_dict_func_list:
            with self.subTest("batch test of no_param_returns_dict_func_list"):
                try:
                    log_json = ""
                    result = func_name()
                    # print("%s: %s" % (func_name, result))
                    self.assertIsInstance(result, dict)
                except AssertionError as e:
                    logstr = {"group": str(func_name), "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    def test_get_stake_threshold(self):
        try:
            log_json = ""
            rst = xbridge_rpc.rpc_connection.getstakesplitthreshold()
            self.assertIsInstance(rst, dict)
            self.assertIsInstance(rst["split stake threshold set to "], int)
            logstr = {"group": "test_get_stake_threshold", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_get_stake_threshold", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('get_stake_threshold unit test FAILED')

    def test_getnewaddress(self):
        try:
            log_json = ""
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            logstr = {"group": "test_getnewaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getnewaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getnewaddress unit test FAILED')

    # TypeError: <class 'decimal.Decimal'> is not JSON serializable
    def test_get_received_by_account(self):
        try:
            log_json = ""
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
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(xbridge_utils.ca_random_tx_id), Decimal)
            logstr = {"group": "test_get_received_by_account", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_get_received_by_account", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('get_received_by_account unit test FAILED')

    def test_getreceivedbyaddress(self):
        try:
            log_json = ""
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
            logstr = {"group": "test_getreceivedbyaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getreceivedbyaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getreceivedbyaddress unit test FAILED')

    def test_getaccount(self):
        try:
            log_json = ""
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
            logstr = {"group": "test_getaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaccount unit test FAILED')

    def test_getaccountaddress(self):
        try:
            log_json = ""
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
            logstr = {"group": "test_getaccountaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getaccountaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaccountaddress unit test FAILED')

    def test_getaddressesbyaccount(self):
        try:
            log_json = ""
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
            logstr = {"group": "test_getaddressesbyaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getaddressesbyaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')

    def test_getaddressesbyaccount(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(xbridge_utils.ca_random_tx_id), list)
            logstr = {"group": "test_getaddressesbyaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getaddressesbyaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')

    def test_gettransaction(self):
        try:
            log_json = ""
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, xbridge_utils.ca_random_tx_id)
            logstr = {"group": "test_gettransaction", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_gettransaction", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('gettransaction unit test FAILED')

    # TypeError: <class 'decimal.Decimal'> is not JSON serializable
    def test_getbalance(self):
        try:
            log_json = ""
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
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance(xbridge_utils.ca_random_tx_id), Decimal)
            logstr = {"group": "test_getbalance", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            logstr = {"group": "test_getbalance", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getbalance unit test FAILED')


# unittest.main()
