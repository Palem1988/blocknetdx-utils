import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *
import random

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

"""                       ***  UNIT TESTS FOR ALL WALLET RELATED FUNCTIONS STARTING WITH GET ***
"""

no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getnettotals,
                        xbridge_rpc.rpc_connection.getnetworkinfo,
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo
                    ]

class wallet_get_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        
    # @unittest.skip("disabled")
    def test_group_no_param_return_dict_batch(self):
        for func_name in no_param_returns_dict_func_list:
            with self.subTest("batch test of no_param_returns_dict_func_list"):
                try:
                    log_json = ""
                    result = func_name()
                    self.assertIsInstance(result, dict)
                except AssertionError as e:
                    log_json = {"group": str(func_name), "success": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

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
            xbridge_rpc.rpc_connection.keypoolrefill(1000)
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            log_json = {"group": "test_getnewaddress", "success": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_getnewaddress", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('getnewaddress unit test FAILED')

    def test_get_received_by_account(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        if basic_garbage_str == "*":
                            self.assertIsNone(xbridge_rpc.getreceivedbyaccount(basic_garbage_str))
                        else:
                            self.assertIsInstance(xbridge_rpc.getreceivedbyaccount(basic_garbage_str), Decimal)
                    elif basic_garbage_str in (-9999999999999999999999999999999999999999999999999999999999999999 , 9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.getreceivedbyaccount(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getreceivedbyaccount, basic_garbage_str)
                    log_json = {"group": "test_get_received_by_account", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_get_received_by_account", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_get_received_by_account unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_get_received_by_account", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_get_received_by_account unit test ERROR: %s' % str(json_excpt))

    def test_getreceivedbyaddress(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, basic_garbage_str)
                    log_json = {"group": "test_getreceivedbyaddress", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getreceivedbyaddress", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getreceivedbyaddress unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)

    def test_getaccount(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, basic_garbage_str)
                    log_json = {"group": "test_getaccount", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getaccount", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getaccount unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)

    def test_getaccountaddress(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsInstance(xbridge_rpc.getaccountaddress(basic_garbage_str), Decimal)
                    elif basic_garbage_str in (-9999999999999999999999999999999999999999999999999999999999999999 , 9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.getaccountaddress(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getaccountaddress, basic_garbage_str)
                    log_json = {"group": "test_getaccountaddress", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getaccountaddress", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getaccountaddress unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)

    def test_getaddressesbyaccount(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if isinstance(basic_garbage_str, str):
                        self.assertIsInstance(xbridge_rpc.getaddressesbyaccount(basic_garbage_str), Decimal)
                    elif basic_garbage_str in (-9999999999999999999999999999999999999999999999999999999999999999,
                                               9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.getaddressesbyaccount(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getaddressesbyaccount, basic_garbage_str)
                    log_json = {"group": "test_getaddressesbyaccount", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getaddressesbyaccount", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getaddressesbyaccount unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)

    def test_gettransaction(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, basic_garbage_str)
                    log_json = {"group": "test_gettransaction", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_gettransaction", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_gettransaction unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)

    # getbalance ( "account" minconf includeWatchonly )
    def test_getbalance(self):
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_account = ""
                    else:
                        optional_account = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if any(optional_account, optional_minconf, optional_includeWatchonly) in (9999999999999999999999999999999999999999999999999999999999999999, -9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.getbalance(optional_account, optional_minconf, optional_includeWatchonly))
                    else:
                        if isinstance(optional_minconf, int):
                            self.assertIsInstance(xbridge_rpc.getbalance(optional_account, optional_minconf, optional_includeWatchonly), Decimal)
                        else:
                            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getbalance, optional_account, optional_minconf, optional_includeWatchonly)
                    log_json = {"group": "test_getbalance", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getbalance", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getbalance invalid unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_account: %s' % optional_account)
                    xbridge_logger.logger.info('optional_minconf: %s' % optional_minconf)
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % optional_includeWatchonly)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_getbalance unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_getbalance", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        
# unittest.main()
