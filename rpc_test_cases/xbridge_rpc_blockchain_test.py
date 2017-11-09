import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *
import random

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class Blockchain_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
        
    def test_get_blockcount(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_blockcount() , int)
            self.assertGreater(xbridge_rpc.get_blockcount(), 120000)
        except AssertionError as e:
            xbridge_logger.logger.info('get_blockcount unit test FAILED')

    def test_get_difficulty(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getdifficulty(), Decimal)
            self.assertGreater(xbridge_rpc.rpc_connection.getdifficulty(), 1000)
        except AssertionError as e:
            xbridge_logger.logger.info('getdifficulty unit test FAILED')

    def test_getblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(0), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(10), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(100000), str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -10)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 100000000000000)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 10.2)
            neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
                                                              -0.0000000000000000000000000000000000000000000000000000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, neg_number)
            large_positive_nb = xbridge_utils.generate_random_number(99999999999999999999999999,
                                                                     99999999999999999999999999999999999999999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, large_positive_nb)
        except AssertionError:
            xbridge_logger.logger.info('getblockhash unit test FAILED')

    # getrawmempool ( verbose )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_getrawmempool(self):
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    verbose = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getrawmempool, verbose)
                    log_json = {"group": "test_getrawmempool", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getrawmempool", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getrawmempool invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_getrawmempool unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_getrawmempool", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)

    # gettxout "txid" n ( includemempool )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_gettxout(self):
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    txid = random.choice(xbridge_utils.set_of_invalid_parameters)
                    n = random.choice(xbridge_utils.set_of_invalid_parameters)
                    optional_includemempool = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_includemempool = ""
                    else:
                        optional_includemempool = random.choice([xbridge_utils.set_of_invalid_parameters])
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getrawmempool, txid, n, optional_includemempool)
                    # self.assertIsInstance(xbridge_rpc.rpc_connection.gettxout(txid, n, optional_includemempool), dict)
                    log_json = {"group": "test_gettxout", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_gettxout", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_gettxout invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_gettxout unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_gettxout", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)

    # gettxoutsetinfo
    def test_gettxoutsetinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.gettxoutsetinfo(), dict)
            log_json = {"group": "test_gettxoutsetinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_gettxoutsetinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_gettxoutsetinfo valid unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_gettxoutsetinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_gettxoutsetinfo unit test ERROR: %s' % json_excpt)

    # getmempoolinfo
    def test_getmempoolinfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getmempoolinfo(), dict)
            log_json = {"group": "test_getmempoolinfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getmempoolinfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmempoolinfo valid unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getmempoolinfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmempoolinfo unit test ERROR: %s' % json_excpt)

    # getbestblockhash
    def test_getbestblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getbestblockhash(), str)
            log_json = {"group": "test_getbestblockhash", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getbestblockhash", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getbestblockhash valid unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getbestblockhash", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getbestblockhash unit test ERROR: %s' % json_excpt)

    # getchaintips
    def test_getchaintips(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getchaintips(), list)
            log_json = {"group": "test_getchaintips", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getchaintips", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getchaintips valid unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getchaintips", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getchaintips unit test ERROR: %s' % json_excpt)

    # verifychain ( checklevel numblocks )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_verifychain(self):
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_checklevel = ""
                    else:
                        optional_checklevel = random.choice([xbridge_utils.set_of_invalid_parameters])
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_numblocks = ""
                    else:
                        optional_numblocks = random.choice([xbridge_utils.set_of_invalid_parameters])
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.verifychain, optional_checklevel, optional_numblocks)
                    log_json = {"group": "test_verifychain", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_verifychain", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_verifychain invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_verifychain unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_verifychain", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)


# unittest.main()
