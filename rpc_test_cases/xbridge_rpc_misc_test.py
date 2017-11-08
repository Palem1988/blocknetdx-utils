import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

set_of_invalid_parameters = ["", " ",
                    0, -xbridge_utils.fixed_large_positive_int, xbridge_utils.fixed_large_positive_int, xbridge_utils.fixed_small_positive_float, 
                    True, False,
                    xbridge_utils.ca_random_tx_id,
                    xbridge_utils.fixed_positive_int,
                    xbridge_utils.invalid_random_positive_int,
                    xbridge_utils.invalid_random_positive_float,
                    -xbridge_utils.invalid_random_positive_int,
                    -xbridge_utils.invalid_random_positive_float,
                    xbridge_utils.valid_random_positive_float,
                    xbridge_utils.fixed_positive_float,
                    -xbridge_utils.valid_random_positive_float,
                    -xbridge_utils.fixed_positive_float,
                    ]

# WE COMPLETE THE LIST
set_of_invalid_parameters.extend(basic_garbage_list)

class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # signmessage "blocknetdxaddress" "message"
    # Please enter the wallet passphrase with walletpassphrase first.
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_signmessage(self):
        log_json = ""
        global set_of_invalid_parameters
        #valid_blocknet_address = xbridge_rpc.rpc_connection.getnewaddress()
        for i in range(1, 51):
            valid_blocknet_address = xbridge_utils.generate_random_valid_address()
            with self.subTest("random garbage"):
                try:
                    tmp_list = []
                    tmp_list = set_of_invalid_parameters
                    tmp_list.extend(valid_blocknet_address)
                    blocknetdxaddress = random.choice(tmp_list)
                    message = random.choice(tmp_list)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.signmessage(blocknetdxaddress, message), dict)
                    log_json = {"group": "test_signmessage", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_signmessage", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('ca_random_tx_id: %s \n' % xbridge_utils.ca_random_tx_id)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_signmessage", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_signmessage unit test ERROR: %s' % json_excpt)
            
    # VALID COMBINATIONS
    # autocombinerewards <true/false> threshold
    def test_autocombinerewards_valid(self):
        try:
            log_json = ""
            success_str = "Auto Combine Rewards Threshold Set"
            xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.VALID_DATA)            
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, -99999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, -9999999999999999999999999999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, 9999999999999999999999999999999999999), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(False, xbridge_utils.ca_random_tx_id), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, 0), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.fixed_negative_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.fixed_positive_int), success_str)
            self.assertEqual(xbridge_rpc.rpc_connection.autocombinerewards(True, xbridge_utils.valid_random_positive_int), success_str)
            log_json = {"group": "autocombinerewards", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "autocombinerewards", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('autocombinerewards valid unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('fixed_positive_int: %s \n' % xbridge_utils.fixed_positive_int)
            xbridge_logger.logger.info('fixed_negative_int: %s \n' % xbridge_utils.fixed_negative_int)
            xbridge_logger.logger.info('valid_random_positive_int: %s \n' % xbridge_utils.valid_random_positive_int)
        except JSONRPCException as json_excpt:
            log_json = {"group": "autocombinerewards", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('autocombinerewards unit test ERROR: %s' % json_excpt)

    # SUBTESTS WITH PARAMETER ORDER AND TYPE RANDOMNIZATION
    # INVALID COMBINATIONS : GARBAGE + OUT-OF-BOUNDS DATA + DATA WE EXPECT THE FUNCTION TO REJECT
    # autocombinerewards <true/false> threshold
    # TODO : Add floats
    # @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_autocombinerewards_invalid(self):
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("autocombinerewards combinations"):
                try:      
                    true_false = random.choice(set_of_invalid_parameters)
                    threshold = random.choice(set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.autocombinerewards, true_false, threshold)
                    log_json = {"group": "autocombinerewards", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "autocombinerewards", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('autocombinerewards invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('autocombinerewards unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "autocombinerewards", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)        

    # SUBTESTS WITH PARAMETER ORDER AND TYPE RANDOMNIZATION
    # move "fromaccount" "toaccount" amount ( minconf "comment" )
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_move_invalid(self):
        log_json = ""
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("move combinations"):
                try:      
                    fromAccount = random.choice(set_of_invalid_parameters)
                    toaccount = random.choice(set_of_invalid_parameters)
                    amount = random.choice(set_of_invalid_parameters)
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_comment = ""
                    else:
                        optional_comment = random.choice([set_of_invalid_parameters])
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.move, fromAccount, toaccount, amount, optional_comment)
                    log_json = {"group": "move", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "move", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('move invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('move unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "move", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    
    # lockunspent unlock [{"txid":"txid","vout":n},...]
    @unittest.skip("DISABLED - IN PROGRESS - UNTESTED")
    def test_lockunspent_invalid(self):
        log_json = ""
        global set_of_invalid_parameters
        for i in range(1, 51):
            log_json = ""
            with self.subTest("lockunspent combinations"):
                try:      
                    fromAccount = random.choice(set_of_invalid_parameters)
                    toaccount = random.choice(set_of_invalid_parameters)
                    amount = random.choice(set_of_invalid_parameters)
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_minconf = ""
                    else:
                        optional_minconf = random.choice([set_of_invalid_parameters])
                    if random.choice(["", set_of_invalid_parameters]) == "":
                        optional_comment = ""
                    else:
                        optional_comment = random.choice([set_of_invalid_parameters])
                    # self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.lockunspent, fromAccount, toaccount, amount, optional_comment)
                    log_json = {"group": "lockunspent", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "lockunspent", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('lockunspent invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('lockunspent unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "lockunspent", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
            
# unittest.main()
