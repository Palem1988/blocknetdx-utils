import unittest
import random

import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class wallet_List_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)

    # listaddressgroupings
    def test_listaddressgroupings(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaddressgroupings(), list)
            log_json = {"group": "test_listaddressgroupings", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_listaddressgroupings", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listaddressgroupings unit test FAILED')

    # listlockunspent
    def test_listlockunspent(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listlockunspent(), list)
            log_json = {"group": "test_listlockunspent", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_listlockunspent", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listlockunspent unit test FAILED\n')
            
    # listreceivedbyaccount ( minconf includeempty includeWatchonly)
    def test_listreceivedbyaccount(self):
        log_json = ""
        # VALID COMBINATIONS
        with self.subTest("VALID COMBINATIONS"):
            try:
                # VALID COMBINATIONS - 1 PARAMETER
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int), list)
                # VALID COMBINATIONS - 2 PARAMETERS
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.fixed_negative_int, False), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaccount(xbridge_utils.valid_random_positive_int, False), list)
                log_json = {"group": "test_listreceivedbyaccount", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_listreceivedbyaccount", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaccount valid sub unit test group FAILED: %s \n' % ass_err)
                xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
                xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
        # INVALID COMBINATIONS
        for i in range(1, 51):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeempty = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeempty = ""
                    else:
                        includeempty = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaccount, optional_minconf, optional_includeempty, optional_includeWatchonly)
                    log_json = {"group": "test_listreceivedbyaccount", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listreceivedbyaccount", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listreceivedbyaccount invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listreceivedbyaccount unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listreceivedbyaccount", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        
    # listreceivedbyaddress ( minconf includeempty includeWatchonly)
    def test_listreceivedbyaddress(self):
        log_json = ""
        # VALID COMBINATIONS
        with self.subTest("VALID COMBINATIONS"):
            try:
                # VALID COMBINATIONS - 1 PARAMETER
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_positive_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_negative_int), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int), list)
                # VALID COMBINATIONS - 2 PARAMETERS
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.fixed_negative_int, False), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int, True), list)
                self.assertIsInstance(xbridge_rpc.rpc_connection.listreceivedbyaddress(xbridge_utils.valid_random_positive_int, False), list)
                log_json = {"group": "test_listreceivedbyaddress", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_listreceivedbyaddress", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('listreceivedbyaddress valid sub unit test group FAILED: %s \n' % ass_err)
                xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
                xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
                xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
        # INVALID COMBINATIONS
        for i in range(1, 51):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeempty = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeempty = ""
                    else:
                        includeempty = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listreceivedbyaddress, optional_minconf, optional_includeempty, optional_includeWatchonly)
                    log_json = {"group": "test_listreceivedbyaddress", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listreceivedbyaddress", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listreceivedbyaddress invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listreceivedbyaddress unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listreceivedbyaddress", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        
    # listtransactions ( "account" count from includeWatchonly)
    def test_listtransactions_invalid(self):
        log_json = ""
        for i in range(1, 51):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_account = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_count = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_from = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_account = ""
                    else:
                        optional_account = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_count = ""
                    else:
                        optional_count = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_from = ""
                    else:
                        optional_from = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.listtransactions, optional_account, optional_count, optional_from, optional_includeWatchonly)
                    log_json = {"group": "test_listtransactions_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listtransactions_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listtransactions_invalid invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listtransactions_invalid unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listtransactions_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    
    # listsinceblock ( "blockhash" target-confirmations includeWatchonly)
    def test_listsinceblock(self):
        log_json = ""
        for i in range(1, 51):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_blockhash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_target_confirmations = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_blockhash = ""
                    else:
                        optional_blockhash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_target_confirmations = ""
                    else:
                        optional_target_confirmations = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_from = ""
                    else:
                        optional_from = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.listsinceblock(optional_blockhash, optional_target_confirmations, optional_includeWatchonly), dict)
                    log_json = {"group": "test_listsinceblock", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listsinceblock", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listsinceblock invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listsinceblock unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listsinceblock", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        """
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listsinceblock(xbridge_utils.ca_random_tx_id), dict)
            log_json = {"group": "test_listsinceblock", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_listsinceblock", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listsinceblock unit test FAILED\n')
            xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
        """

    # listaccounts ( minconf includeWatchonly)
    def test_listaccounts(self):
        log_json = ""
        for i in range(1, 51):
            log_json = ""
            with self.subTest("subtest combinations"):
                try:      
                    optional_minconf = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_blockhash = random.choice([xbridge_utils.set_of_invalid_parameters])
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includeWatchonly = ""
                    else:
                        optional_includeWatchonly = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.listaccounts(optional_minconf, optional_includeWatchonly), dict)
                    log_json = {"group": "test_listaccounts", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_listaccounts", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_listaccounts invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_listaccounts unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_listaccounts", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
        """
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.listaccounts(), dict)
            log_json = {"group": "test_listaccounts", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError:
            log_json = {"group": "test_listaccounts", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('listaccounts unit test FAILED')
        """


# unittest.main()