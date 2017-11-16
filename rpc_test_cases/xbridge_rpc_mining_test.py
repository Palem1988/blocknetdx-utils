import unittest
import xbridge_logger
import random
from decimal import *

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class Mining_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # reservebalance [<reserve> [amount]]
    def test_reservebalance(self):
        for i in range(subTest_count):
            with self.subTest("test_reservebalance"):
                try:
                    reserve = random.choice(xbridge_utils.set_of_invalid_parameters)
                    amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if isinstance(reserve, bool) and reserve is True:
                        if (amount > 0):
                            self.assertIsInstance(xbridge_rpc.reservebalance(reserve, amount), dict)
                        else:
                            self.assertIsNone(xbridge_rpc.reservebalance(reserve, amount))
                    else:
                        self.assertIsNone(xbridge_rpc.reservebalance(reserve, amount))
                    log_json = {"group": "test_reservebalance", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_reservebalance", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_reservebalance FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('reserve: %s \n' % reserve)
                    xbridge_logger.logger.info('amount: %s \n' % amount)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_reservebalance", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_reservebalance ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('reserve: %s \n' % reserve)
                    xbridge_logger.logger.info('amount: %s \n' % amount)


    # submitblock "hexdata" ( "jsonparametersobject" )
    def test_submitblock(self):
        for i in range(subTest_count):
            with self.subTest("test_submitblock"):
                try:
                    hexdata = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_json_param = None
                    else:
                        optional_json_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.submitblock, hexdata, optional_json_param)
                    log_json = {"group": "test_submitblock", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_submitblock", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_submitblock FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('hexdata: %s \n' % hexdata)
                    xbridge_logger.logger.info('optional_json_param: %s \n' % optional_json_param)

    def test_getmininginfo(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getmininginfo(), dict)
            log_json = {"group": "test_getmininginfo", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getmininginfo", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmininginfo FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getmininginfo", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getmininginfo ERROR: %s' % str(json_excpt))

    # getnetworkhashps ( blocks height )
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_getnetworkhashps_invalid(self):
        for i in range(subTest_count):
            with self.subTest("test_getnetworkhashps_invalid"):
                try:
                    modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
                    modified_set = [x for x in modified_set if x is not None]
                    optional_blocks = random.choice(modified_set)
                    optional_height = random.choice(modified_set)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.getnetworkhashps, optional_blocks, optional_height)
                    log_json = {"group": "test_getnetworkhashps", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_getnetworkhashps", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getnetworkhashps FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('optional_blocks: %s \n' % optional_blocks)
                    xbridge_logger.logger.info('optional_height: %s \n' % optional_height)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_getnetworkhashps", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_getnetworkhashps unit test ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('optional_blocks: %s \n' % optional_blocks)
                    xbridge_logger.logger.info('optional_height: %s \n' % optional_height)

    # getnetworkhashps ( blocks height )
    def test_getnetworkhashps_valid(self):
        try:
            valid_int_1 = xbridge_utils.generate_random_int(1, 100000)
            valid_int_2 = xbridge_utils.generate_random_int(1, 100000)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getnetworkhashps(), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(valid_int_1, valid_int_1), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(valid_int_1, 0), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(0, valid_int_2), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(0, 0), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(valid_int_1, valid_int_2), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(-valid_int_1, valid_int_2), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(valid_int_1, -valid_int_2), int)
            self.assertIsInstance(xbridge_rpc.getnetworkhashps(-valid_int_1, -valid_int_2), int)
            log_json = {"group": "test_getnetworkhashps_valid", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getnetworkhashps_valid", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getnetworkhashps_valid FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_int_1: %s \n' % valid_int_1)
            xbridge_logger.logger.info('valid_int_2: %s \n' % valid_int_2)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getnetworkhashps_valid", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_getnetworkhashps_valid ERROR: %s' % str(json_excpt))
            xbridge_logger.logger.info('valid_int_1: %s \n' % valid_int_1)
            xbridge_logger.logger.info('valid_int_2: %s \n' % valid_int_2)

    # prioritisetransaction <txid> <priority delta> <fee delta>
    def test_prioritisetransaction(self):
        for i in range(subTest_count):
            with self.subTest("prioritisetransaction"):
                try:
                    # modified_set = xbridge_utils.set_of_invalid_parameters
                    txid = random.choice(xbridge_utils.set_of_invalid_parameters)
                    priority = random.choice(xbridge_utils.set_of_invalid_parameters)
                    fee = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.prioritisetransaction, txid, priority, fee)
                    log_json = {"group": "test_prioritisetransaction", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_prioritisetransaction", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_prioritisetransaction unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('txid: %s \n' % txid)
                    xbridge_logger.logger.info('priority: %s \n' % priority)
                    xbridge_logger.logger.info('fee: %s \n' % fee)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_prioritisetransaction", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_prioritisetransaction ERROR: %s' % str(json_excpt))


# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(50):
    suite.addTest(Mining_UnitTest("test_reservebalance"))
    # suite.addTest(Misc_UnitTest("test_validateaddress_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""