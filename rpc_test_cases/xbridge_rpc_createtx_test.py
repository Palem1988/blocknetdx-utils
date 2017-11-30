import unittest
import random

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from utils import xbridge_utils
from interface import xbridge_rpc
import xbridge_logger

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class create_Tx_Test(unittest.TestCase):
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
       self.invalid_sm_positive_nb = xbridge_utils.generate_random_number(0.000000000000000000000000001, 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
       self.invalid_lg_positive_nb = xbridge_utils.generate_random_number(9999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.invalid_dest_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.nb_with_leading_zeros_1 = xbridge_utils.generate_random_number_with_leading_zeros()
       self.nb_with_leading_zeros_2 = xbridge_utils.generate_random_number_with_leading_zeros()
       # Common pools from which parameters will be randomnly picked
       valid_token = xbridge_utils.generate_random_valid_token()
       self.token_pool = [valid_token, xbridge_utils.c_src_Token]
       valid_address = xbridge_utils.generate_random_valid_address()
       invalid_address_short = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 40))
       invalid_address_med = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       invalid_address_long = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(5000, 15000))
       self.address_pool = [valid_address, invalid_address_short, invalid_address_med, invalid_address_long]
       self.amount_pool = [xbridge_utils.invalid_random_positive_float,
                                            xbridge_utils.valid_random_positive_float,
                                            -xbridge_utils.invalid_random_positive_float,
                                            -xbridge_utils.valid_random_positive_float,
                                            xbridge_utils.fixed_small_positive_float,
                                            xbridge_utils.fixed_large_positive_int, 0]

    # Sometimes return a None object
    @unittest.skip("IN REVIEW")
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
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, fromAmount, dest_Address, dest_Token, toAmount), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v0", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_create_tx_v0", 1, ass_err, [txid, src_Address, dest_Address, src_Token, dest_Token, fromAmount, toAmount])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_create_tx_v0", 2, json_excpt, [txid, src_Address, dest_Address, src_Token, dest_Token, fromAmount, toAmount])

    # Numerical parameter combinations
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
            xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v2", 1, ass_err)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_src_Address: %s', str(self.valid_src_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Token: %s', str(self.valid_dest_Token)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_neg_nb: %s', str(self.invalid_neg_nb)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_1: %s', str(self.valid_positive_nb_1)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_2: %s', str(self.valid_positive_nb_2)[:MAX_LOG_LENGTH])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_create_tx_v2", 2, json_excpt)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('valid_src_Address: %s', str(self.valid_src_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Token: %s', str(self.valid_dest_Token)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('invalid_neg_nb: %s', str(self.invalid_neg_nb)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_1: %s', str(self.valid_positive_nb_1)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_2: %s', str(self.valid_positive_nb_2)[:MAX_LOG_LENGTH])

    @unittest.skip("IN TESTING")
    def test_invalid_create_tx_v1(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    src_Token = random.choice(self.token_pool)
                    dest_Token = random.choice(self.token_pool)
                    src_Address = random.choice(self.address_pool)
                    dest_Address = random.choice(self.address_pool)
                    # negative_number + positive_number
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, self.invalid_neg_nb, dest_Address, dest_Token, self.valid_positive_nb_2), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    # positive_number + negative_number
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, self.valid_positive_nb_1, dest_Address, dest_Token, self.invalid_neg_nb), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    # negative_number + negative_number
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, self.invalid_neg_nb, dest_Address, dest_Token, self.invalid_neg_nb), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    # 0 + negative_number
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, 0, dest_Address, dest_Token, self.invalid_neg_nb), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    # positive_number + 0
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, self.valid_positive_nb_1, dest_Address, dest_Token, 0), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    # 0 + 0
                    self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, 0, dest_Address, dest_Token, 0), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 0)
                    param_vector = [src_Address, src_Token, self.invalid_neg_nb, src_Address, dest_Token, self.valid_positive_nb_2, self.valid_positive_nb_1]
                    for param in param_vector:
                        print("test_invalid_create_tx_v1 param: %s" % (str(param)[:10]))
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 1, ass_err, param_vector)
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_create_tx_v1", 2, json_excpt, param_vector)

    # Combinations with empty addresses
    def test_invalid_create_tx_v2(self):
        try:
            new_address = xbridge_utils.generate_random_valid_address()
            self.assertIsInstance(xbridge_rpc.create_tx(" ", self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.valid_positive_nb_2), dict)
            self.assertIsInstance(xbridge_rpc.create_tx(new_address, self.valid_src_Token, self.valid_positive_nb_1, " ", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            self.assertIsInstance(xbridge_rpc.create_tx(" ", self.valid_src_Token, self.valid_positive_nb_1, " ", self.valid_dest_Token, self.valid_positive_nb_2), dict)
            xbridge_logger.XLOG("test_invalid_create_tx_v2", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v2", 1, ass_err)
            if MAX_LOG_LENGTH > 0:
                xbridge_logger.logger.info('new_address: %s', str(new_address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Token: %s', str(self.valid_dest_Token)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_dest_Address: %s', str(self.valid_dest_Address)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_1: %s', str(self.valid_positive_nb_1)[:MAX_LOG_LENGTH])
                xbridge_logger.logger.info('valid_positive_nb_2: %s', str(self.valid_positive_nb_2)[:MAX_LOG_LENGTH])

    # @unittest.skip("IN TESTING")
    def test_invalid_create_tx_v3(self):
        for i in range(subTest_count):
            src_Token = random.choice(self.token_pool)
            dest_Token = random.choice(self.token_pool)
            # We try to make sure they are different
            if (src_Token == dest_Token):
                dest_Token = random.choice(self.token_pool)
            src_Amount = random.choice(self.amount_pool)
            dest_Amount = random.choice(self.amount_pool)
            src_Address = random.choice(self.address_pool)
            dest_Address = random.choice(self.address_pool)
            if (src_Address == dest_Address):
                dest_Address = random.choice(self.address_pool)
        with self.subTest("Same source and destination Addresses"):
            try:
                # print("test_invalid_create_tx_v3 - src_Address: %s" % str(src_Address))
                self.assertIsInstance(
                    xbridge_rpc.create_tx(src_Address, src_Token, src_Amount, src_Address, dest_Token, dest_Amount),
                    dict)
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 0)
            except AssertionError as ass_err:
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 1, ass_err,
                                    [src_Address, src_Token, src_Amount, src_Address, dest_Token, dest_Amount])
            except JSONRPCException as json_excpt:
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 2, json_excpt,
                                    [src_Address, src_Token, src_Amount, src_Address, dest_Token, dest_Amount])
        with self.subTest("same source and destination Tokens, different addresses"):
            try:
                self.assertIsInstance(
                    xbridge_rpc.create_tx(src_Address, src_Token, src_Amount, src_Address, src_Token, dest_Amount),
                    dict)
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 0)
                param_vector = [src_Address, src_Token, src_Amount, src_Address, src_Token, dest_Amount]
                # for param in param_vector:
                #    print("test_invalid_create_tx_v3 param: %s" % (str(param)[:10]))
            except AssertionError as ass_err:
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 1, ass_err, param_vector)
            except JSONRPCException as json_excpt:
                xbridge_logger.XLOG("test_invalid_create_tx_v3", 2, json_excpt, param_vector)

    # Combinations of address parameters containing quotes. At least one address will contain quotes. The other params may be valid or invalid.
    # @unittest.skip("IN TESTING")
    def test_invalid_create_tx_v4(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("combinations"):
                try:
                    address_with_quotes_1 = "'" + str(xbridge_utils.generate_random_valid_address()) + "'"
                    address_with_quotes_2 = "'" + str(xbridge_utils.generate_random_valid_address()) + "'"
                    address_wo_quotes = str(xbridge_utils.generate_random_valid_address())
                    src_Address = random.choice([address_wo_quotes, address_with_quotes_1, address_with_quotes_2])
                    dest_Address = random.choice([address_wo_quotes, address_with_quotes_1, address_with_quotes_2])
                    if (src_Address == address_wo_quotes) and (dest_Address == address_wo_quotes):
                        if random.choice(True, False) is True:
                            src_Address = random.choice([address_with_quotes_1, address_with_quotes_2])
                        else:
                            dest_Address = random.choice([address_with_quotes_1, address_with_quotes_2])
                    src_Token = random.choice(self.token_pool)
                    dest_Token = random.choice(self.token_pool)
                    src_Amount = random.choice(self.amount_pool)
                    dest_Amount = random.choice(self.amount_pool)
                    param_vector = [src_Address, src_Token, src_Amount, src_Address, dest_Token, dest_Amount]
                    for param in param_vector:
                        print("test_invalid_create_tx_v4 param: %s" % (str(param)[:10]))
                    self.assertIsInstance(xbridge_rpc.create_tx(src_Address, src_Token, src_Amount, src_Address, dest_Token, dest_Amount), dict)
                    xbridge_logger.XLOG("test_invalid_create_tx_v4", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_create_tx_v4", 1, ass_err, param_vector)
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_create_tx_v4", 2, json_excpt, param_vector)

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
            xbridge_logger.XLOG("test_invalid_create_tx_v6", 0)
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

    # very small + very small, all other parameters being valid
    def test_invalid_create_tx_v8(self):
        try:
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token,
                                                        self.invalid_sm_positive_nb, self.valid_dest_Address,
                                                        self.valid_dest_Token, self.invalid_sm_positive_nb), dict)
            xbridge_logger.XLOG("test_invalid_create_tx_v8", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v8", 1, ass_err, [self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_create_tx_v8", 2, json_excpt, [self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb])

    # very small + very large, all other parameters being valid
    def test_invalid_create_tx_v9(self):
        try:
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb), dict)
            xbridge_logger.XLOG("test_invalid_create_tx_v9", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v9", 1, ass_err, [self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_create_tx_v9", 2, json_excpt, [self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb])

    # very large + very small, all other parameters being valid
    def test_invalid_create_tx_v10(self):
        try:
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb), dict)
            xbridge_logger.XLOG("test_invalid_create_tx_v10", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v10", 1, ass_err, [self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_create_tx_v10", 2, json_excpt, [self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb])

    # very large + very small, all other parameters being valid
    def test_invalid_create_tx_v11(self):
        try:
            self.assertIsInstance(xbridge_rpc.create_tx(self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb,
                                      self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb), dict)
            xbridge_logger.XLOG("test_invalid_create_tx_v11", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_invalid_create_tx_v11", 1, ass_err, [self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_invalid_create_tx_v11", 2, json_excpt, [self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb])

# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(10):
    suite.addTest(create_Tx_Test("test_invalid_create_tx_v3"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""