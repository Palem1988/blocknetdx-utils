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

# xbridge_config.MAX_CHAR_LENGTH_TO_DISPLAY

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
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnbudgetvoteraw invalid FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnbudgetvoteraw ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   

    # spork <name> [<value>]
    # @unittest.skip("DISABLED - UNTESTED")
    def test_spork(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("spork combinations"):
                try:      
                    name_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    value_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.spork, name_param, value_param)
                    log_json = {"group": "test_spork", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_spork", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_spork invalid unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('name_param: %s' % name_param)
                    xbridge_logger.logger.info('value_param: %s' % value_param)

    def test_get_budget_valid(self):
        try:
            budget = xbridge_rpc.get_budget()
            self.assertIsInstance(budget, dict)
            log_json = {"group": "test_get_budget", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_budget", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_budget_valid FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_get_budget", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_budget_valid ERROR: %s' % json_excpt)
            
    # servicenode "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_servicenode_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("servicenode combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.servicenode, cmd_param)
                    log_json = {"group": "test_servicenode", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_servicenode", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_servicenode_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('cmd_param: %s' % cmd_param)
    
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
                    log_json = {"group": "test_obfuscation", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_obfuscation", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_obfuscation_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('blocknetdxaddress: %s' % blocknetdxaddress)
                    xbridge_logger.logger.info('amount: %s' % amount)
                
    # mnsync [status|reset]
    # @unittest.skip("DISABLED - UNTESTED")
    # "failure" or JSONRPCException: -1: get_value< string > called on integer Value
    def test_mnsync_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if isinstance(cmd_param, str):
                        self.assertIsInstance(xbridge_rpc.rpc_connection.mnsync(cmd_param), str)
                    else:
                        self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnsync, cmd_param)
                    log_json = {"group": "test_mnsync_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnsync_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnsync_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('param: %s' % str(cmd_param))
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnsync_invalid ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('param: %s' % str(cmd_param))
                    log_json = {"group": "test_mnsync_invalid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   
                    
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
                    log_json = {"group": "test_mnsync_valid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnsync_valid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('param: %s' % valid_param)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnsync_valid ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnsync_valid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('param: %s' % valid_param)
                    

    # mnbudget "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnbudget(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnbudget, cmd_param)
                    log_json = {"group": "test_mnbudget", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnbudget", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnbudget invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnbudget unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnbudget", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   

    # mnfinalbudget "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnfinalbudget(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnfinalbudget, cmd_param)
                    log_json = {"group": "test_mnfinalbudget", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnfinalbudget", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnfinalbudget invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnfinalbudget unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnfinalbudget", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   
    
# unittest.main()
