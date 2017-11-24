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

class Blockchain_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # verifychain ( checklevel numblocks )
    # @unittest.skip("TEMPORARILY DISABLED - IN REVIEW")
    def test_verifychain_invalid(self):
        custom_set = [x for x in xbridge_utils.set_of_invalid_parameters if x is not None]
        custom_set = [x for x in custom_set if x is not isinstance(x, int)]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    optional_checklevel = random.choice(custom_set)
                    optional_numblocks = random.choice(custom_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.verifychain, optional_checklevel, optional_numblocks)
                    log_json = {"group": "test_verifychain_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_verifychain_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_verifychain_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_checklevel: %s' % str(optional_checklevel))
                    xbridge_logger.logger.info('optional_numblocks: %s' % str(optional_numblocks))

    # getrawmempool ( verbose )
    # Trello OK
    def test_getrawmempool_valid(self):
        log_json = ""
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(True), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(False), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(), list)
            log_json = {"group": "test_getrawmempool_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getrawmempool_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getrawmempool_valid FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('test_getrawmempool_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_getrawmempool_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    # getrawmempool ( verbose )
    def test_getrawmempool_invalid(self):
        # CAUTION ! we remove boolean values from the set since they are valid for this function
        set_without_bools = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    verbose = random.choice(set_without_bools)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getrawmempool, verbose)
                    log_json = {"group": "test_getrawmempool_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getrawmempool_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('\ntest_getrawmempool_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('verbose: %s' % str(verbose))
                    
    # gettxout "txid" n ( includemempool )
    @unittest.skip("TEMPORARILY DISABLED - IN TESTING")
    def test_gettxout_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    txid = random.choice(xbridge_utils.set_of_invalid_parameters)
                    n = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includemempool = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includemempool = None
                    else:
                        optional_includemempool = random.choice([xbridge_utils.set_of_invalid_parameters])
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.gettxout, txid, n, optional_includemempool)
                    log_json = {"group": "test_gettxout_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_gettxout_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('\ntest_gettxout_invalid FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('\ntest_gettxout_invalid ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_gettxout", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                            
    def test_get_blockcount(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_blockcount() , int)
            self.assertGreater(xbridge_rpc.get_blockcount(), 120000)
            log_json = {"group": "test_get_blockcount", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('\ntest_get_blockcount FAILED: %s' % ass_err)
            log_json = {"group": "test_get_blockcount", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)

    def test_get_difficulty(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getdifficulty(), Decimal)
            self.assertGreater(xbridge_rpc.rpc_connection.getdifficulty(), 100)
            log_json = {"group": "test_get_difficulty", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('\ntest_get_difficulty FAILED: %s' % ass_err)
            log_json = {"group": "test_get_difficulty", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)

    # getblockhash index
    def test_getblockhash_valid(self):
        try:
            regular_int = xbridge_utils.generate_random_int(1, 10000)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(0), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(regular_int), str)
            log_json = {"group": "test_getblockhash_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('\ntest_getblockhash_valid FAILED: %s' % ass_err)
            log_json = {"group": "test_getblockhash_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            xbridge_logger.logger.info('\ntest_getblockhash_valid ERROR: %s' % str(json_excpt))
            log_json = {"group": "test_getblockhash_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)

    # getblockhash index
    # TODO : other data types
    def test_getblockhash_invalid(self):
        try:
            regular_negative_int = xbridge_utils.generate_random_int(-1000, -1)
            large_negative_int = xbridge_utils.generate_random_int(-50000, -10000)
            very_large_positive_int = xbridge_utils.generate_random_int(100000000000000, 999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, regular_negative_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, large_negative_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, very_large_positive_int)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 0.0000000000001)
            random_negative_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
                                                              -0.0000000000000000000000000000000000000000000000000000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, random_negative_number)
            log_json = {"group": "test_get_difficulty", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            xbridge_logger.logger.info('\ngetblockhash FAILED: %s' % ass_err)
            log_json = {"group": "ngetblockhash", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('regular_negative_int: %s' % str(regular_negative_int))            
            xbridge_logger.logger.info('large_negative_int: %s' % str(large_negative_int))            
            xbridge_logger.logger.info('very_large_positive_int: %s' % str(very_large_positive_int))            
            xbridge_logger.logger.info('random_negative_number: %s' % str(random_negative_number))            
                        
    # gettxoutsetinfo
    def test_gettxoutsetinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.gettxoutsetinfo(), dict)
            log_json = {"group": "test_gettxoutsetinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_gettxoutsetinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_gettxoutsetinfo FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_gettxoutsetinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_gettxoutsetinfo ERROR: %s' % json_excpt)

    # getmempoolinfo
    def test_getmempoolinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getmempoolinfo(), dict)
            log_json = {"group": "test_getmempoolinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getmempoolinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getmempoolinfo FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getmempoolinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getmempoolinfo ERROR: %s' % json_excpt)

    # getbestblockhash
    def test_getbestblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbestblockhash(), str)
            log_json = {"group": "test_getbestblockhash", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getbestblockhash", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getbestblockhash FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getbestblockhash", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getbestblockhash ERROR: %s' % json_excpt)

    # getchaintips
    def test_getchaintips(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getchaintips(), list)
            log_json = {"group": "test_getchaintips", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getchaintips", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getchaintips FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getchaintips", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('\ntest_getchaintips ERROR: %s' % json_excpt)

# unittest.main()

"""
suite = unittest.TestSuite()
suite.addTest(Blockchain_UnitTest("test_getrawmempool_invalid"))
suite.addTest(Blockchain_UnitTest("test_getrawmempool_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""