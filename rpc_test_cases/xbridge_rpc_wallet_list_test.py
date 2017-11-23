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

class wallet_List_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # listaddressgroupings
    def test_listaddressgroupings(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaddressgroupings(), list)
            log_json = {"group": "test_listaddressgroupings", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_listaddressgroupings", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listaddressgroupings FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('listaddressgroupings ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_listlockunspent", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    # listlockunspent
    def test_listlockunspent(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listlockunspent(), list)
            log_json = {"group": "test_listlockunspent", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_listlockunspent", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_listlockunspent FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_listlockunspent ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_listlockunspent", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            
    # listreceivedbyaccount (minconf includeempty includeWatchonly)
    def test_listreceivedbyaccount_valid(self):
        log_json = ""
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(), list)
            optional_minconf = xbridge_utils.generate_random_int(-9999999999, 9999999999)
            optional_includeempty = random.choice([True, False])
            optional_includeWatchonly = random.choice([True, False])
            self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(optional_minconf, optional_includeempty, optional_includeWatchonly), list)
            log_json = {"group": "test_listreceivedbyaccount_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_listreceivedbyaccount_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_listreceivedbyaccount_valid FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('optional_minconf: %s \n' % str(optional_minconf))
            xbridge_logger.logger.info('optional_includeempty: %s \n' % str(optional_includeempty))
            xbridge_logger.logger.info('optional_includeWatchonly: %s \n' % str(optional_includeWatchonly))
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_listreceivedbyaccount_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_listreceivedbyaccount_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_logger.logger.info('optional_minconf: %s \n' % str(optional_minconf))
            xbridge_logger.logger.info('optional_includeempty: %s \n' % str(optional_includeempty))
            xbridge_logger.logger.info('optional_includeWatchonly: %s \n' % str(optional_includeWatchonly))
            xbridge_utils.ERROR_LOG.append(log_json)
        
    # listreceivedbyaccount (minconf includeempty includeWatchonly)
    def test_listreceivedbyaccount_invalid(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:
                    optional_minconf = random.choice(custom_set)
                    optional_includeempty = random.choice(custom_set)
                    optional_includeWatchonly = random.choice(custom_set)
                    if isinstance(optional_minconf, int) and isinstance(optional_includeempty, bool) and isinstance(optional_includeWatchonly, bool):
                        continue
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.listreceivedbyaccount, optional_minconf, optional_includeempty, optional_includeWatchonly)
                    self.assertIsNone(xbridge_rpc.listreceivedbyaccount(optional_minconf, optional_includeempty, optional_includeWatchonly))
                    log_json = {"group": "test_listreceivedbyaccount_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listreceivedbyaccount_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listreceivedbyaccount_invalid FAILED: %s' % ass_err)
        
    # listreceivedbyaddress (minconf includeempty includeWatchonly)
    def test_listreceivedbyaddress_valid(self):
        log_json = ""
        try:
            self.assertIsInstance(xbridge_rpc.listreceivedbyaddress(), list)
            optional_minconf = xbridge_utils.generate_random_int(-9999999999, 9999999999)
            optional_includeempty = random.choice([True, False])
            optional_includeWatchonly = random.choice([True, False])
            self.assertIsInstance(xbridge_rpc.listreceivedbyaddress(optional_minconf, optional_includeempty, optional_includeWatchonly), list)
            log_json = {"group": "test_listreceivedbyaddress_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_listreceivedbyaddress_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_listreceivedbyaddress_valid FAILED: %s \n' % ass_err)
            xbridge_logger.logger.info('optional_minconf: %s \n' % optional_minconf)
            xbridge_logger.logger.info('optional_includeempty: %s \n' % optional_includeempty)
            xbridge_logger.logger.info('optional_includeWatchonly: %s \n' % optional_includeWatchonly)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_listreceivedbyaddress_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_listreceivedbyaddress_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_logger.logger.info('optional_minconf: %s \n' % optional_minconf)
            xbridge_logger.logger.info('optional_includeempty: %s \n' % optional_includeempty)
            xbridge_logger.logger.info('optional_includeWatchonly: %s \n' % optional_includeWatchonly)
            xbridge_utils.ERROR_LOG.append(log_json)    
        
    def test_listreceivedbyaddress_invalid(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    optional_minconf = random.choice(custom_set)
                    optional_includeempty = random.choice(custom_set)
                    optional_includeWatchonly = random.choice(custom_set)
                    if isinstance(optional_minconf, int) and isinstance(optional_includeempty, bool) and isinstance(optional_includeWatchonly, bool):
                        continue
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.listreceivedbyaddress, optional_minconf, optional_includeempty, optional_includeWatchonly)
                    self.assertIsNone(xbridge_rpc.listreceivedbyaddress(optional_minconf, optional_includeempty, optional_includeWatchonly))
                    log_json = {"group": "test_listreceivedbyaddress_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listreceivedbyaddress_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listreceivedbyaddress_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_minconf: %s' % str(optional_minconf))
                    xbridge_logger.logger.info('optional_includeempty: %s' % str(optional_includeempty))
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % str(optional_includeWatchonly))
                        
    # listtransactions ( "account" count from includeWatchonly)
    def test_listtransactions_valid(self):
        try:
            self.assertIsInstance(xbridge_rpc.listtransactions(), list)
        except AssertionError as ass_err:
            log_json = {"group": "test_listtransactions_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_listtransactions_valid FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_listtransactions_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_listtransactions_valid", "success": 0,  "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
        
    # listtransactions ( "account" count from includeWatchonly)
    # returns None instead of Exception ==> Trello
    def test_listtransactions_invalid(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        log_json = ""
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_account = random.choice(custom_set)
                    optional_count = random.choice(custom_set)
                    optional_from = random.choice(custom_set)
                    optional_includeWatchonly = random.choice(custom_set)
                    if (optional_account == "") and (optional_count == 0) and (optional_from == 0):
                        self.assertIsInstance(xbridge_rpc.listtransactions(optional_account, optional_count, optional_from, optional_includeWatchonly), list)
                    else:
                        # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.listtransactions, optional_account, optional_count, optional_from, optional_includeWatchonly)
                        self.assertIsNone(xbridge_rpc.listtransactions(optional_account, optional_count, optional_from, optional_includeWatchonly))
                    log_json = {"group": "test_listtransactions_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listtransactions_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('\ntest_listtransactions_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_account: %s' % str(optional_account))
                    xbridge_logger.logger.info('optional_count: %s' % str(optional_count))
                    xbridge_logger.logger.info('optional_from: %s' % str(optional_from))
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % str(optional_includeWatchonly))
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listtransactions_invalid ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listtransactions_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_logger.logger.info('optional_account: %s' % str(optional_account))
                    xbridge_logger.logger.info('optional_count: %s' % str(optional_count))
                    xbridge_logger.logger.info('optional_from: %s' % str(optional_from))
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % str(optional_includeWatchonly))
                    xbridge_utils.ERROR_LOG.append(log_json)
                    
    # listsinceblock ("blockhash" target-confirmations includeWatchonly)
    def test_listsinceblock_invalid(self):
        log_json = ""
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_blockhash = random.choice(custom_set)
                    optional_target_confirmations = random.choice(custom_set)
                    optional_includeWatchonly = random.choice(custom_set)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listsinceblock, optional_blockhash, optional_target_confirmations, optional_includeWatchonly)
                    log_json = {"group": "test_listsinceblock", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listsinceblock", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listsinceblock FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_blockhash: %s' % optional_blockhash)
                    xbridge_logger.logger.info('optional_target_confirmations: %s' % optional_target_confirmations)
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % optional_includeWatchonly)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listsinceblock ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listsinceblock", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('optional_blockhash: %s' % optional_blockhash)
                    xbridge_logger.logger.info('optional_target_confirmations: %s' % optional_target_confirmations)
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % optional_includeWatchonly)
    
    # listaccounts (minconf includeWatchonly)
    def test_listaccounts_valid_1(self):
        try:
            self.assertIsInstance(xbridge_rpc.listaccounts(), dict)
            log_json = {"group": "test_listaccounts_valid_1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_listaccounts_valid_1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)

    # listaccounts (minconf includeWatchonly)
    def test_listaccounts_valid_2(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    optional_minconf = xbridge_utils.generate_random_int(-9999999, 9999999)
                    optional_includeWatchonly = random.choice([True, False])
                    self.assertIsInstance(xbridge_rpc.listaccounts(), dict)
                    log_json = {"group": "test_listaccounts_valid_2", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listaccounts_valid_2", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listaccounts_valid_2 FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_minconf: %s' % str(optional_minconf))
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % str(optional_includeWatchonly))
    
    # listaccounts (minconf includeWatchonly)
    # returns None instead of Exception ==> Trello
    def test_listaccounts_invalid(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_minconf = random.choice(custom_set)
                    optional_includeWatchonly = random.choice(custom_set)
                    if isinstance(optional_minconf, int) and isinstance(optional_includeWatchonly, bool):
                        continue
                    # self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.listaccounts, optional_minconf, optional_includeWatchonly)
                    self.assertIsNone(xbridge_rpc.listaccounts(optional_minconf, optional_includeWatchonly))
                    log_json = {"group": "test_listaccounts_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listaccounts_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listaccounts_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_minconf: %s' % str(optional_minconf))
                    xbridge_logger.logger.info('optional_includeWatchonly: %s' % str(optional_includeWatchonly))
      
# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(wallet_List_UnitTest("test_autocombinerewards_valid"))
for i in range(150):
    suite.addTest(wallet_List_UnitTest("test_listtransactions_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

