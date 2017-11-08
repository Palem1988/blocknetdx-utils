import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *
import random

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

account_func_list = []

class wallet_get_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        
    def test_getunconfirmedbalance(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getunconfirmedbalance(), Decimal)
            log_json = {"group": "test_getunconfirmedbalance", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as e:
            log_json = {"group": "test_getunconfirmedbalance", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getunconfirmedbalance unit test FAILED')

    def test_getrawchangeaddress(self):
        try:
            log_json = ""
            new_address = xbridge_rpc.rpc_connection.getrawchangeaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            log_json = {"group": "test_getrawchangeaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as e:
            log_json = {"group": "test_getrawchangeaddress", "success": 0, "error": 1}
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
                    log_json = {"group": str(func_name), "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    def test_get_stake_threshold(self):
        try:
            log_json = ""
            rst = xbridge_rpc.rpc_connection.getstakesplitthreshold()
            self.assertIsInstance(rst, dict)
            self.assertIsInstance(rst["split stake threshold set to "], int)
            log_json = {"group": "test_get_stake_threshold", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_get_stake_threshold", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('get_stake_threshold unit test FAILED')

    def test_getnewaddress(self):
        try:
            log_json = ""
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            log_json = {"group": "test_getnewaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getnewaddress", "success": 0, "error": 1}
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
            log_json = {"group": "test_get_received_by_account", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_get_received_by_account", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('get_received_by_account unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

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
            log_json = {"group": "test_getreceivedbyaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getreceivedbyaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getreceivedbyaddress unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

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
            log_json = {"group": "test_getaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaccount unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

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
            log_json = {"group": "test_getaccountaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getaccountaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaccountaddress unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

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
            log_json = {"group": "test_getaddressesbyaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getaddressesbyaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

    def test_getaddressesbyaccount(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(xbridge_utils.ca_random_tx_id), list)
            log_json = {"group": "test_getaddressesbyaccount", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getaddressesbyaccount", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)

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
            log_json = {"group": "test_gettransaction", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_gettransaction", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('gettransaction unit test FAILED')

    # getbalance ( "account" minconf includeWatchonly )
    def test_getbalance(self):
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("move combinations"):
                try:      
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_account = ""
                    else:
                        optional_minconf = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        optional_includeWatchonly = random.choice([set_of_invalid_parameters])
                    self.assertIsInstance(xbridge_rpc.rpc_connection.getbalance(optional_account, optional_minconf, optional_includeWatchonly), Decimal)
                    log_json = {"group": "test_getbalance", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getbalance", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getbalance invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_getbalance unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_getbalance", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        
# unittest.main()
