import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class Blocknetdx_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # mnbudgetvoteraw <servicenode-tx-hash> <servicenode-tx-index> <proposal-hash> <yes|no> <time> <vote-sig>
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnbudgetvoteraw(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    service_node_tx_hash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_index = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_hash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_yes_no = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_time = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_vote_sig = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.mnbudgetvoteraw, service_node_tx_hash, service_node_tx_index,
                                                             service_node_tx_proposal_hash, service_node_tx_proposal_yes_no, service_node_tx_proposal_time, service_node_tx_proposal_vote_sig)
                    xbridge_logger.XLOG("test_mnbudgetvoteraw", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_mnbudgetvoteraw", 1, ass_err, [service_node_tx_hash, service_node_tx_index, service_node_tx_proposal_hash, service_node_tx_proposal_yes_no, service_node_tx_proposal_time, service_node_tx_proposal_vote_sig])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_mnbudgetvoteraw", 2, json_excpt, [service_node_tx_hash, service_node_tx_index, service_node_tx_proposal_hash, service_node_tx_proposal_yes_no, service_node_tx_proposal_time, service_node_tx_proposal_vote_sig])

    # spork <name> [<value>]
    @unittest.skip("DISABLED - IN REVIEW - HAS SOMETIMES UNPREDICTABLE BEHAVIOR")
    def test_spork(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("spork combinations"):
                try:      
                    name_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    value_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.spork, name_param, value_param)
                    xbridge_logger.XLOG("test_spork", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_spork", 1, ass_err, [name_param, value_param])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_spork", 2, json_excpt, [name_param, value_param])

    def test_get_budget_valid(self):
        try:
            budget = xbridge_rpc.get_budget()
            self.assertIsInstance(budget, dict)
            xbridge_logger.XLOG("test_get_budget_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_get_budget_valid", 1, ass_err)
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_get_budget_valid", 2, json_excpt)
            
    # servicenode "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_servicenode_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_servicenode_invalid"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.servicenode, cmd_param)
                    xbridge_logger.XLOG("test_servicenode_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_servicenode_invalid", 1, ass_err, [cmd_param])
    
    # obfuscation <blocknetdxaddress> <amount>
    # @unittest.skip("DISABLED - UNTESTED")
    def test_obfuscation_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    blocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                    amount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.obfuscation, blocknetdxaddress, amount)
                    xbridge_logger.XLOG("test_obfuscation_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_obfuscation_invalid", 1, ass_err, [blocknetdxaddress, amount])
                
    # mnsync [status|reset]
    # @unittest.skip("DISABLED - UNTESTED")
    # "failure" or JSONRPCException: -1: get_value< string > called on integer Value
    def test_mnsync_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    set_without_str = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, str)]
                    cmd_param = random.choice(set_without_str)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnsync, cmd_param)
                    xbridge_logger.XLOG("test_mnsync_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_mnsync_invalid", 1, ass_err, [cmd_param])
                    
    # mnsync [status|reset]
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnsync_valid(self):
        valid_params = ["status", "reset"]
        for valid_param in valid_params:
            log_json = ""
            with self.subTest(valid_param=valid_param):
                try:      
                    if valid_param == "reset":
                        self.assertIsInstance(xbridge_rpc.rpc_connection.mnsync(valid_param), str)
                        log_json = {"group": "test_mnsync_valid", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    else:
                        self.assertIsInstance(xbridge_rpc.rpc_connection.mnsync(valid_param), dict)
                        log_json = {"group": "test_mnsync_valid", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_mnsync_valid", 1, ass_err, [valid_param])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_mnsync_valid", 2, json_excpt, [valid_param])
                    
    # mnbudget "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnbudget_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_passphrase = None
                    else:
                        optional_passphrase = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnbudget, cmd_param, optional_passphrase)
                    xbridge_logger.XLOG("test_mnbudget_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_mnbudget_invalid", 1, ass_err, [cmd_param, optional_passphrase])

    # mnfinalbudget "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnfinalbudget_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        optional_passphrase = None
                    else:
                        optional_passphrase = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnfinalbudget, cmd_param, optional_passphrase)
                    xbridge_logger.XLOG("test_mnfinalbudget_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_mnfinalbudget_invalid", 1, ass_err, [cmd_param, optional_passphrase])
    
# unittest.main()
