import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***
"""

class Blocknetdx_UnitTest(unittest.TestCase):
    def test_get_budget(self):
        try:
            budget = xbridge_rpc.get_budget()
            hash_value = "1e23e3b04773450f84584ce222e318682b50d2a65d2a082a4821b378145263fe"
            self.assertIsInstance(budget, dict)
            # self.assertEqual(budget["dev-fund"]["Hash"], hash_value)
            log_json = {"group": "test_get_budget", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_get_budget", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_budget valid unit test FAILED: %s' % ass_err)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_get_budget", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_get_budget unit test ERROR: %s' % json_excpt)
            
    # servicenode "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_servicenode(self):
        for i in range(1, 51):
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
                    xbridge_logger.logger.info('test_servicenode invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_servicenode unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_servicenode", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   
    
    # spork <name> [<value>]
    # @unittest.skip("DISABLED - UNTESTED")
    def test_spork(self):
        for i in range(1, 51):
            log_json = ""
            with self.subTest("spork combinations"):
                try:      
                    name_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    value_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.spork, name_param, value_param)
                    log_json = {"group": "test_spork", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_spork", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_spork invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_spork unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_spork", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   

    # obfuscation <blocknetdxaddress> <amount>
    # @unittest.skip("DISABLED - UNTESTED")
    def test_obfuscation(self):
        for i in range(1, 51):
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
                    xbridge_logger.logger.info('test_obfuscation invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_obfuscation unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_obfuscation", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   

    # mnsync [status|reset]
    # @unittest.skip("DISABLED - UNTESTED")
    # "failure" or JSONRPCException: -1: get_value< string > called on integer Value
    def test_mnsync_invalid(self):
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    cmd_param = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.mnsync, cmd_param)
                    self.assertIsInstance(xbridge_rpc.rpc_connection.mnsync(cmd_param), str)
                    log_json = {"group": "test_mnsync_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnsync_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnsync_invalid invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnsync_invalid unit test ERROR: %s' % str(json_excpt))
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
                    xbridge_logger.logger.info('test_mnsync_valid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnsync_valid unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnsync_valid", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   
                    
    # mnbudgetvoteraw <servicenode-tx-hash> <servicenode-tx-index> <proposal-hash> <yes|no> <time> <vote-sig>
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfd in position 89: invalid start byte
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnbudgetvoteraw(self):
        for i in range(1, 51):
            log_json = ""
            with self.subTest("combinations"):
                try:      
                    service_node_tx_hash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_index = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_hash = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_yes_no = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_time = random.choice(xbridge_utils.set_of_invalid_parameters)
                    service_node_tx_proposal_vote_sig = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(UnicodeDecodeError, xbridge_rpc.rpc_connection.mnbudgetvoteraw, service_node_tx_hash, service_node_tx_index,
                                                            service_node_tx_proposal_hash, service_node_tx_proposal_yes_no, service_node_tx_proposal_time, service_node_tx_proposal_vote_sig)
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_mnbudgetvoteraw invalid unit test FAILED: %s' % ass_err)
                except JSONRPCException as json_excpt:
                    xbridge_logger.logger.info('test_mnbudgetvoteraw unit test ERROR: %s' % str(json_excpt))
                    log_json = {"group": "test_mnbudgetvoteraw", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)   

    # mnbudget "command"... ( "passphrase" )
    # @unittest.skip("DISABLED - UNTESTED")
    def test_mnbudget(self):
        for i in range(1, 51):
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
        for i in range(1, 51):
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
