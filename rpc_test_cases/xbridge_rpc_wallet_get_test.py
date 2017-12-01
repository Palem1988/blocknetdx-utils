import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *
import random

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getnettotals,
                        xbridge_rpc.rpc_connection.getnetworkinfo,
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo
                    ]

class wallet_get_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
        
    def test_group_no_param_return_dict_batch(self):
        for func_name in no_param_returns_dict_func_list:
            with self.subTest("batch test of no_param_returns_dict_func_list"):
                try:
                    log_json = ""
                    result = func_name()
                    self.assertIsInstance(result, dict)
                    log_json = {"group": str(func_name), "success": 1, "failure": 0, "error": 0}
                except AssertionError as ass_err:
                    log_json = {"group": str(func_name), "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s FAILED: %s' % (str(func_name), str(ass_err)))
                except JSONRPCException as json_excpt:
                    log_json = {"group": func_name, "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('%s ERROR: %s' % str(json_excpt), str(ass_err))

    def test_getunconfirmedbalance(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getunconfirmedbalance(), Decimal)
            xbridge_logger.XLOG("test_getunconfirmedbalance", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getunconfirmedbalance", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getunconfirmedbalance", 2, json_excpt)

    def test_getrawchangeaddress(self):
        try:
            log_json = ""
            new_address = xbridge_rpc.rpc_connection.getrawchangeaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            xbridge_logger.XLOG("test_getrawchangeaddress", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getrawchangeaddress", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getrawchangeaddress", 2, json_excpt)
            
    def test_get_stake_threshold(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getstakesplitthreshold(), dict)
            xbridge_logger.XLOG("test_get_stake_threshold", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_get_stake_threshold", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_get_stake_threshold", 2, json_excpt)

    def test_getnewaddress(self):
        try:
            log_json = ""
            xbridge_rpc.rpc_connection.keypoolrefill(1000)
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            self.assertEqual(len(new_address), 34)
            xbridge_logger.XLOG("test_getnewaddress", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getnewaddress", 1, ass_err, [new_address])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getnewaddress", 2, json_excpt, [new_address])

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
                    xbridge_logger.XLOG("test_get_received_by_account", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getreceivedbyaddress", 1, ass_err, [basic_garbage_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_getreceivedbyaddress", 2, json_excpt, [basic_garbage_str])

    def test_getreceivedbyaddress(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, basic_garbage_str)
                    xbridge_logger.XLOG("test_getreceivedbyaddress", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getreceivedbyaddress", 1, ass_err, [basic_garbage_str])

    def test_getaccount(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, basic_garbage_str)
                    xbridge_logger.XLOG("test_getaccount", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getaccount", 1, ass_err, [basic_garbage_str])

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
                    xbridge_logger.XLOG("test_getaccountaddress", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getaccountaddress", 1, ass_err, [basic_garbage_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_getaccountaddress", 2, json_excpt, [basic_garbage_str])

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
                    xbridge_logger.XLOG("test_getaddressesbyaccount", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getaddressesbyaccount", 1, ass_err, [basic_garbage_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_getaddressesbyaccount", 2, json_excpt, [basic_garbage_str])

    def test_gettransaction(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettransaction, basic_garbage_str)
                    xbridge_logger.XLOG("test_gettransaction", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_gettransaction", 1, ass_err, [basic_garbage_str])

    # getbalance ( "account" minconf includeWatchonly )
    def test_getbalance(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_getbalance"):
                try:      
                    modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if x not in (9999999999999999999999999999999999999999999999999999999999999999, -9999999999999999999999999999999999999999999999999999999999999999)]
                    if random.choice(["", modified_set]) == "":
                        optional_account = None
                    else:
                        optional_account = random.choice(modified_set)
                    if random.choice(["", modified_set]) == "":
                        optional_minconf = None
                    else:
                        optional_minconf = random.choice(modified_set)
                    if random.choice(["", modified_set]) == "":
                        optional_includeWatchonly = None
                    else:
                        optional_includeWatchonly = random.choice(modified_set)
                    if isinstance(optional_minconf, int):
                        self.assertIsInstance(xbridge_rpc.getbalance(optional_account, optional_minconf, optional_includeWatchonly), Decimal)
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getbalance, optional_account, optional_minconf, optional_includeWatchonly)
                    xbridge_logger.XLOG("test_getbalance", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getbalance", 1, ass_err, [optional_account, optional_minconf, optional_includeWatchonly])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_getbalance", 2, json_excpt, [optional_account, optional_minconf, optional_includeWatchonly])
                    
# unittest.main()
