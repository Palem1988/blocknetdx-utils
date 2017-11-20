import unittest
import random
import itertools

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from utils import xbridge_utils
from interface import xbridge_rpc
import xbridge_logger
from utils import xbridge_custom_exceptions

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class create_Tx_Test(unittest.TestCase):
    # Generate new data before each run
    def setUp(self):
       xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
       # Valid data
       self.valid_txid = xbridge_utils.generate_random_valid_txid()
       self.valid_src_Token = xbridge_utils.generate_random_valid_token()
       self.valid_dest_Token = xbridge_utils.generate_random_valid_token()
       self.valid_src_Address = xbridge_utils.generate_random_valid_address()
       self.valid_dest_Address = xbridge_utils.generate_random_valid_address()
       self.valid_positive_nb_1 = xbridge_utils.generate_random_number(1, 10000)
       self.valid_positive_nb_2 = xbridge_utils.generate_random_number(1, 10000)
       # Invalid data
       self.invalid_neg_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, -0.0000000000000000000000000000000000000000000000000001)
       self.invalid_sm_positive_nb = 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
       self.invalid_lg_positive_nb = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.invalid_dest_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.nb_with_leading_zeros_1 = xbridge_utils.generate_random_number_with_leading_zeros()
       self.nb_with_leading_zeros_2 = xbridge_utils.generate_random_number_with_leading_zeros()

    def test_invalid_create_tx_v0(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("random garbage"):
                try:
                    txid = random.choice(xbridge_utils.set_of_invalid_parameters)
                    src_Address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    dest_Address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    fromAmount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    toAmount = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.create_tx, src_Address, src_Token, fromAmount, dest_Address, dest_Token, toAmount)
                    log_json = {"group": "test_invalid_create_tx_v0", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_invalid_create_tx_v0", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_create_tx_v0 unit test FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('src_Address: %s', src_Address)
                    xbridge_logger.logger.info('dest_Address: %s', dest_Address)
                    xbridge_logger.logger.info('src_Token: %s', src_Token)
                    xbridge_logger.logger.info('dest_Token: %s', dest_Token)
                    xbridge_logger.logger.info('fromAmount: %s', fromAmount)
                    xbridge_logger.logger.info('toAmount: %s', toAmount)

    # Various numerical parameter combinations
    def test_invalid_create_tx_v1(self):
        try:
            # negative_number + positive_number, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.valid_dest_Address, self.valid_dest_Token, self.valid_positive_nb_2), dict)
            # positive_number + negative_number, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb), dict)
            # negative_number + negative_number, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb), dict)
            # 0 + negative_number, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, 0, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb), dict)
            # positive_number + 0, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, 0), dict)
            # 0 + 0, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, 0, self.valid_dest_Address, self.valid_dest_Token, 0), dict)
            log_json = {"group": "test_invalid_create_tx_v1", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v1", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v1 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_neg_nb: %s', self.invalid_neg_nb)
            xbridge_logger.logger.info('valid_positive_nb_1: %s', self.valid_positive_nb_1)
            xbridge_logger.logger.info('valid_positive_nb_2: %s', self.valid_positive_nb_2)
            
    # Combinations with empty addresses
    def test_invalid_create_tx_v2(self):
        try:
            new_address = xbridge_utils.generate_random_valid_address()
            self.assertIsInstance(xbridge_rpc.create_tx(" ", self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.valid_positive_nb_2), dict)
            self.assertIsInstance(xbridge_rpc.create_tx(new_address, self.valid_src_Token, self.valid_positive_nb_1, " ", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            self.assertIsInstance(xbridge_rpc.create_tx(" ", self.valid_src_Token, self.valid_positive_nb_1, " ", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            log_json = {"group": "test_invalid_create_tx_v2", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v2", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v2 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('new_address: %s', new_address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_positive_nb_1: %s', self.valid_positive_nb_1)
            xbridge_logger.logger.info('valid_positive_nb_2: %s', self.valid_positive_nb_2)
            

    def test_invalid_create_tx_v3(self):
        try:
            # Same source and destination Addresses, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_src_Address, self.valid_dest_Token, self.valid_positive_nb_2), dict)
            # Same source and destination Tokens, different addresses, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_src_Token, self.valid_positive_nb_2), dict)
            # Same source and destination Addresses and Tokens, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_2), dict)
            log_json = {"group": "test_invalid_create_tx_v3", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v3", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v3 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_src_Token: %s', self.valid_src_Token)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_positive_nb_1: %s', self.valid_positive_nb_1)
            xbridge_logger.logger.info('valid_positive_nb_2: %s', self.valid_positive_nb_2)
            
        
    # Combinations of address parameters containing quotes
    def test_invalid_create_tx_v4(self):
        try:
            # Address 1 contains quotes, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_src_Token, self.valid_positive_nb_1, "12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            # Address 2 contains quotes, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.valid_positive_nb_1, "'12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey'", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            # Both Addresses contain quotes, all other parameters being valid
            self.assertIsInstance(xbridge_rpc.create_tx("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_src_Token, self.valid_positive_nb_1, "'12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey'", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            log_json = {"group": "test_invalid_create_tx_v4", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v4", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v4 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_src_Token: %s', self.valid_src_Token)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('valid_positive_nb_1: %s', self.valid_positive_nb_1)
            xbridge_logger.logger.info('valid_positive_nb_2: %s', self.valid_positive_nb_2)
            

    # Combinations of quotes + out-of-bounds quantities
    def test_invalid_create_tx_v5(self):
        try:
            self.assertIsInstance(xbridge_rpc.create_tx("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_src_Token, self.invalid_neg_nb, "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_dest_Token, self.invalid_neg_nb), dict)
            self.assertIsInstance(xbridge_rpc.create_tx("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.valid_positive_nb_1, "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_dest_Token, self.invalid_neg_nb), dict)
            self.assertIsInstance(xbridge_rpc.create_tx("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.invalid_neg_nb, "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_dest_Token, self.valid_positive_nb_1), dict)
            log_json = {"group": "test_invalid_create_tx_v5", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v5", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v5 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('invalid_neg_nb: %s', self.invalid_neg_nb)
            xbridge_logger.logger.info('valid_src_Token: %s', self.valid_src_Token)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('valid_src_Address_1: %s', "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'")
            xbridge_logger.logger.info('valid_src_Address_2: %s', "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'")
            xbridge_logger.logger.info('valid_src_Address_3: %s', "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'")
            xbridge_logger.logger.info('valid_dest_Address_1: %s', "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'")
            xbridge_logger.logger.info('valid_dest_Address_2: %s', "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'")
            xbridge_logger.logger.info('valid_dest_Address_3: %s', "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy")
            xbridge_logger.logger.info('valid_positive_nb_1: %s', "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy")
            
            
    # Combinations of multiple invalid parameters leading up to ALL parameters being invalid
    def test_invalid_create_tx_v6(self):
        try:
            # Only source Address is valid, the rest is invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.invalid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb), dict)
            # Only source Address + source Token are valid, the rest is invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb), dict)
            # Only source Address + source Token + source_Quantity are valid, the rest is invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb), dict)
            # Only (source + dest) Addresses + source Token + source_Quantity are valid, the rest is invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb), dict)
            # Only (source + dest) Addresses + (source + dest)  Tokens + source_Quantity are valid, the rest is invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb), dict)
            # All parameters are invalid
            self.assertIsInstance(xbridge_rpc.create_tx(self.invalid_src_Address, self.invalid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb), dict)
            log_json = {"group": "test_invalid_create_tx_v6", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_invalid_create_tx_v6", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('test_invalid_create_tx_v6 unit test FAILED: %s' % ass_err)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address)
            xbridge_logger.logger.info('valid_src_Token: %s', self.valid_src_Token)
            xbridge_logger.logger.info('valid_dest_Token: %s', self.valid_dest_Token)
            xbridge_logger.logger.info('invalid_src_Token: %s', self.invalid_src_Token)
            xbridge_logger.logger.info('invalid_dest_Token: %s', self.invalid_dest_Token)
            xbridge_logger.logger.info('valid_positive_nb_1: %s', self.valid_positive_nb_1)
            xbridge_logger.logger.info('invalid_neg_nb: %s', self.invalid_neg_nb)

    # Combinations of very small and very large numerical parameters, all other parameters being valid
    # bitcoinrpc.authproxy.JSONRPCException: -32700: Parse error
    def test_invalid_create_tx_v8(self):
        # very small + very small
        with self.subTest("test_invalid_create_tx_v8-1"):
            try:
                self.assertIsInstance(
                    xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                          self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb),
                    dict)
                log_json = {"group": "test_invalid_create_tx_v8-1", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_invalid_create_tx_v8-1", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('')
                xbridge_logger.logger.info('dxCreate unit test group 8 subtest-1 FAILED on parameter:')
                xbridge_logger.logger.info("invalid_sm_positive_nb: %s" % self.invalid_sm_positive_nb)
        # very small + very large
        with self.subTest("test_invalid_create_tx_v8-2"):
            try:
                self.assertRaises(JSONRPCException,
                    xbridge_rpc.create_tx, self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                          self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb)
                log_json = {"group": "test_invalid_create_tx_v8-2", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_invalid_create_tx_v8-2", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('')
                xbridge_logger.logger.info('dxCreate unit test group 8 subtest-2 FAILED on parameter:')
                xbridge_logger.logger.info("invalid_sm_positive_nb: %s" % self.invalid_sm_positive_nb)
                xbridge_logger.logger.info("invalid_lg_positive_nb: %s" % self.invalid_lg_positive_nb)
        # very large + very small
        with self.subTest("test_invalid_create_tx_v8-3"):
            try:
                self.assertRaises(JSONRPCException,
                    xbridge_rpc.create_tx, self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                          self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb)
                log_json = {"group": "test_invalid_create_tx_v8-3", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_invalid_create_tx_v8-3", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('')
                xbridge_logger.logger.info('dxCreate unit test group 8 subtest-3 FAILED on parameter:')
                xbridge_logger.logger.info("invalid_lg_positive_nb: %s" % self.invalid_lg_positive_nb)
                xbridge_logger.logger.info("invalid_sm_positive_nb: %s" % self.invalid_sm_positive_nb)
        # very large + very large
        with self.subTest("test_invalid_create_tx_v8-4"):
            try:
                self.assertRaises(JSONRPCException,
                    xbridge_rpc.create_tx, self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                          self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb)
                log_json = {"group": "test_invalid_create_tx_v8-4", "success": 1, "failure": 0, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
            except AssertionError as ass_err:
                log_json = {"group": "test_invalid_create_tx_v8-4", "success": 0, "failure": 1, "error": 0}
                xbridge_utils.ERROR_LOG.append(log_json)
                xbridge_logger.logger.info('')
                xbridge_logger.logger.info('dxCreate unit test group 8 subtest-4 FAILED on parameter:')
                xbridge_logger.logger.info("invalid_lg_positive_nb: %s" % self.invalid_lg_positive_nb)
                xbridge_logger.logger.info("invalid_lg_positive_nb: %s" % self.invalid_lg_positive_nb)
                
# unittest.main()
