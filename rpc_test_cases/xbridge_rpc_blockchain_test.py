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
            with self.subTest("combinations"):
                try:
                    optional_checklevel = random.choice(custom_set)
                    optional_numblocks = random.choice(custom_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.verifychain, optional_checklevel, optional_numblocks)
                    xbridge_logger.XLOG("test_verifychain_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_verifychain_invalid", 1, ass_err, [optional_checklevel, optional_numblocks])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_verifychain_invalid", 2, json_excpt, [optional_checklevel, optional_numblocks])

    # getrawmempool ( verbose )
    # Trello OK
    def test_getrawmempool_valid(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(True), dict)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(False), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getrawmempool(), list)
            xbridge_logger.XLOG("test_getrawmempool_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getrawmempool_valid", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getrawmempool_valid", 2, json_excpt)

    # getrawmempool ( verbose )
    def test_getrawmempool_invalid(self):
        # CAUTION ! we remove boolean values from the set since they are valid for this function
        set_without_bools = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
        for i in range(subTest_count):
            with self.subTest("combinations"):
                try:
                    verbose = random.choice(set_without_bools)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getrawmempool, verbose)
                    xbridge_logger.XLOG("test_getrawmempool_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_getrawmempool_invalid", 1, ass_err, [verbose])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_getrawmempool_invalid", 2, json_excpt, [verbose])
                    
    # gettxout "txid" n ( includemempool )
    @unittest.skip("TEMPORARILY DISABLED - IN TESTING")
    def test_gettxout_invalid(self):
        for i in range(subTest_count):
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
                    xbridge_logger.XLOG("test_gettxout_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_gettxout_invalid", 1, ass_err, [txid, n, optional_includemempool])

    def test_get_blockcount(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_blockcount() , int)
            self.assertGreater(xbridge_rpc.get_blockcount(), 120000)
            xbridge_logger.XLOG("test_get_blockcount", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_get_blockcount", 1, ass_err)

    def test_get_difficulty(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getdifficulty(), Decimal)
            self.assertGreater(xbridge_rpc.rpc_connection.getdifficulty(), 100)
            xbridge_logger.XLOG("test_get_difficulty", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_get_difficulty", 1, ass_err)

    # getblockhash index
    def test_getblockhash_valid(self):
        try:
            regular_int = xbridge_utils.generate_random_int(1, 10000)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(0), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(regular_int), str)
            xbridge_logger.XLOG("test_getblockhash_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getblockhash_valid", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getblockhash_valid", 2, json_excpt)

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
            xbridge_logger.XLOG("test_getblockhash_invalid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getblockhash_invalid", 1, ass_err, [regular_negative_int, large_negative_int, very_large_positive_int, random_negative_number])

    # gettxoutsetinfo
    def test_gettxoutsetinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.gettxoutsetinfo(), dict)
            xbridge_logger.XLOG("gettxoutsetinfo", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("gettxoutsetinfo", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("gettxoutsetinfo", 2, json_excpt)

    # getmempoolinfo
    def test_getmempoolinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getmempoolinfo(), dict)
            xbridge_logger.XLOG("test_getmempoolinfo", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getmempoolinfo", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getmempoolinfo", 2, json_excpt)

    # getbestblockhash
    def test_getbestblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbestblockhash(), str)
            xbridge_logger.XLOG("getbestblockhash", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("getbestblockhash", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("getbestblockhash", 2, json_excpt)

    # getchaintips
    def test_getchaintips(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getchaintips(), list)
            xbridge_logger.XLOG("test_getchaintips", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_getchaintips", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_getchaintips", 2, json_excpt)

# unittest.main()

"""
suite = unittest.TestSuite()
suite.addTest(Blockchain_UnitTest("test_getrawmempool_invalid"))
suite.addTest(Blockchain_UnitTest("test_getrawmempool_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""