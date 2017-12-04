from strgen import StringGenerator
import unittest
import random

from utils import xbridge_custom_exceptions
import xbridge_logger

from utils import xbridge_utils
from interface import xbridge_rpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class accept_Tx_Test(unittest.TestCase):
    def setUp(self):
       xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
       # Valid data
       self.valid_txid = xbridge_utils.generate_random_valid_txid()
       self.valid_src_Address = xbridge_utils.generate_random_valid_address()
       self.valid_dest_Address = xbridge_utils.generate_random_valid_address()
       # Invalid data from garbage character classes
       self.invalid_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.long_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       # Invalid data from random character classes
       self.input_str_from_random_classes_1 = xbridge_utils.generate_input_from_random_classes_combinations(1, 4000)
       self.input_str_from_random_classes_2 = xbridge_utils.generate_input_from_random_classes_combinations(9000, 12000)
       self.input_str_from_random_classes_3 = xbridge_utils.generate_input_from_random_classes_combinations(1, 100)
       valid_token = xbridge_utils.generate_random_valid_token()
       self.token_pool = [valid_token, xbridge_utils.c_src_Token]
       valid_address = xbridge_utils.generate_random_valid_address()
       invalid_address_short = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 40))
       invalid_address_med = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       invalid_address_long = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(5000, 15000))
       self.address_pool = [valid_address, invalid_address_short, invalid_address_med, invalid_address_long]
       # Test many combinations of 0 to 10 000 white spaces
       self.simple_whitespace = ""
       self.whitespace_str_1 = StringGenerator('[\s]{1:10000}').render()
       self.whitespace_str_2 = StringGenerator('[\s]{1:10000}').render()
       self.whitespace_str_3 = StringGenerator('[\s]{1:10000}').render()
       self.whitespace_pool = [self.simple_whitespace, self.whitespace_str_1, self.whitespace_str_2, self.whitespace_str_3]
        
    # This test will not run during sequence tests as it contains "noseq" in its name.
    def test_invalid_accept_tx_0a_noseq(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("random garbage"):
                try:
                    txid = random.choice(xbridge_utils.set_of_invalid_parameters)
                    src_Address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    dest_Address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, txid, src_Address, dest_Address)
                    xbridge_logger.XLOG("test_invalid_accept_tx_0a", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_accept_tx_0a", 1, ass_err, [txid, src_Address, dest_Address])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_accept_tx_0a", 2, json_excpt, [txid, src_Address, dest_Address])

    # Specific combinations of valid and invalid parameters
    def test_invalid_accept_tx_1(self):
        try:
           log_json = ""
           self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.invalid_src_Address, self.valid_dest_Address)
           self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.invalid_src_Address, self.invalid_dest_Address)
           self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.invalid_txid, self.invalid_src_Address, self.invalid_dest_Address)
           self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.invalid_txid, self.invalid_src_Address, self.valid_dest_Address)
           self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.invalid_txid, self.valid_src_Address, self.valid_dest_Address)
           xbridge_logger.XLOG("test_invalid_accept_tx_1", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_accept_tx_1", 1, ass_err)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_txid: %s', self.valid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_txid: %s', self.invalid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address[:MAX_LOG_LENGTH])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_accept_tx_1", 2, json_excpt)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_txid: %s', self.valid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_txid: %s', self.invalid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address[:MAX_LOG_LENGTH])

    # Combinations of empty parameters
    def test_invalid_accept_tx_2(self):
        for i in range(subTest_count):
            with self.subTest("combinations"):
                try:
                    whitespace_param_1 = random.choice(self.whitespace_pool)
                    whitespace_param_2 = random.choice(self.whitespace_pool)
                    whitespace_param_3 = random.choice(self.whitespace_pool)
                    whitespace_set = set([whitespace_param_1, whitespace_param_2, whitespace_param_3])
                    src_Address = random.choice(self.address_pool)
                    dest_Address = random.choice(self.address_pool)
                    txid = random.choice(self.address_pool)
                    param_pool = [whitespace_param_1, whitespace_param_1, whitespace_param_1, src_Address, dest_Address, txid]
                    param_1 = random.choice(param_pool)
                    param_2 = random.choice(param_pool)
                    param_3 = random.choice(param_pool)
                    chosen_parameters_set = set([param_1, param_2, param_3])
                    # set intersection to determine if at least one param is whitespace string
                    if len(set(whitespace_set) & set(chosen_parameters_set)) < 1:
                        continue
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, param_1, param_2, param_3)
                    xbridge_logger.XLOG("test_invalid_accept_tx_2", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_accept_tx_2", 1, ass_err, [param_1, param_2, param_3])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_accept_tx_2", 2, json_excpt, [param_1, param_2, param_3])
    
    # Input parameter(s) is from combination of random character classes
    def test_invalid_accept_tx_3(self):
        try:
            log_json = ""
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.input_str_from_random_classes_1, self.valid_src_Address, self.valid_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.input_str_from_random_classes_1, self.valid_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.valid_src_Address, self.input_str_from_random_classes_1)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.input_str_from_random_classes_1, self.input_str_from_random_classes_1, self.input_str_from_random_classes_1)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.input_str_from_random_classes_1, self.input_str_from_random_classes_2, self.input_str_from_random_classes_3)
            log_json = {"group": "test_invalid_accept_tx_3", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_accept_tx_3", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_accept_tx_3 FAILED: %s \n' % str(ass_err))
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_txid: [%s]', self.valid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('input_str_from_random_classes_1: [%s]', self.input_str_from_random_classes_1[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('input_str_from_random_classes_2: [%s]', self.input_str_from_random_classes_2[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('input_str_from_random_classes_3: [%s]', self.input_str_from_random_classes_3[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_src_Address: [%s]', self.valid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: [%s]', self.valid_dest_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_src_Address: [%s]', self.invalid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_dest_Address: [%s]', self.invalid_dest_Address[:MAX_LOG_LENGTH])
        
    # Combinations of very long addresses and transaction ids
    def invalid_accept_tx_4(self):
        try:
            log_json = ""
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.long_src_Address, self.valid_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.long_txid, self.long_src_Address, self.valid_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.valid_src_Address, self.long_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.long_txid, self.valid_src_Address, self.long_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.valid_txid, self.long_src_Address, self.long_dest_Address)
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, self.long_txid, self.long_src_Address, self.long_dest_Address)
            log_json = {"group": "invalid_accept_tx_4", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "invalid_accept_tx_4", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('invalid_accept_tx_4 FAILED: %s \n' % str(ass_err))
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_txid: [%s]', self.valid_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('long_txid: [%s]', self.long_txid[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_src_Address: [%s]', self.valid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: [%s]', self.valid_dest_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_src_Address: [%s]', self.invalid_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_dest_Address: [%s]', self.invalid_dest_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('long_src_Address: [%s]', self.long_src_Address[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('long_dest_Address: [%s]', self.long_dest_Address[:MAX_LOG_LENGTH])
    
    # Combinations of same source and dest Addresses. Txids can be valid or invalid.
    def test_invalid_accept_tx_5(self):
        for i in range(subTest_count):
            with self.subTest("combinations"):
                try:
                    txid_from_invalid_set = random.choice(xbridge_utils.set_of_invalid_parameters)
                    picked_txid = random.choice([txid_from_invalid_set, self.valid_txid])
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.accept_tx, picked_txid, self.valid_src_Address, self.valid_src_Address)
                    xbridge_logger.XLOG("test_invalid_accept_tx_5", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_accept_tx_5", 1, ass_err, [picked_txid, self.valid_src_Address, self.valid_src_Address])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_accept_tx_5", 2, json_excpt, [picked_txid, self.valid_src_Address, self.valid_src_Address])


# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(1):
    # suite.addTest(accept_Tx_Test("test_invalid_accept_tx_5"))
    # suite.addTest(accept_Tx_Test("test_invalid_accept_tx_0a_noseq"))
    suite.addTest(accept_Tx_Test("test_invalid_accept_tx_0b_noseq"))
# suite.addTest(accept_Tx_Test("test_getrawmempool_valid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""
