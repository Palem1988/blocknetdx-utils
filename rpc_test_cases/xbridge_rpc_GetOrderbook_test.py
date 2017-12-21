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

class getOrderBook_Test(unittest.TestCase):
    def setUp(self):
       xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
       # Valid data
       self.valid_src_Token = xbridge_utils.generate_random_valid_token()
       self.valid_dest_Token = xbridge_utils.generate_random_valid_token()
       # detailLevel
       self.valid_detailLevel = random.choice([1, 2, 3])
       self.invalid_detailLevel = xbridge_utils.generate_random_int(4, 99999999999999999999)
       self.negative_invalid_detailLevel = xbridge_utils.generate_random_int(-99999999999999999999, -1)
       # Common pools from which parameters will be randomnly picked
       self.token_pool = [self.valid_src_Token, xbridge_utils.c_src_Token]
       self.invalid_short_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 40))
       self.invalid_med_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_long_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(5000, 15000))

    # All parameters are drawn from an invalid set
    def test_invalid_getorderbook_v1a(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = random.choice(xbridge_utils.set_of_invalid_parameters)
                    src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # We create scenarios in which the base and quote currencies are the same, with 1/5 probability
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    # Optional parameter
                    if random.choice([True, False]) is True:
                        maxOrders = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        maxOrders = None
                    # Optional parameter
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token, maxOrders, showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1a", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1a", 1, ass_err, [detailLevel, src_Token, dest_Token, maxOrders, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1a", 2, json_excpt, [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

    # All parameters are drawn from an invalid set, except the first one
    def test_invalid_getorderbook_v1b(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = self.valid_detailLevel
                    src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        maxOrders = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        maxOrders = None
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(
                        xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token, maxOrders,
                                                   showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1b", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1b", 1, ass_err,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1b", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

    # All parameters are drawn from an invalid set, except the first two params
    def test_invalid_getorderbook_v1c(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = self.valid_detailLevel
                    src_Token = self.valid_src_Token
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        maxOrders = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        maxOrders = None
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(
                        xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token,
                                                   maxOrders,
                                                   showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1c", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1c", 1, ass_err,
                                        [detailLevel, src_Token, dest_Token, maxOrders,
                                         showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1c", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

    # All parameters are drawn from an invalid set, except the first three params
    def test_invalid_getorderbook_v1d(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = self.valid_detailLevel
                    src_Token = self.valid_src_Token
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = self.valid_dest_Token
                    if random.choice([True, False]) is True:
                        maxOrders = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        maxOrders = None
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token,
                                                   maxOrders, showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1d", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1d", 1, ass_err,
                                        [detailLevel, src_Token, dest_Token, maxOrders,
                                         showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1d", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

    # The last parameter is invalid, all other params being valid
    def test_invalid_getorderbook_v1e(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = self.valid_detailLevel
                    src_Token = self.valid_src_Token
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = self.valid_dest_Token
                    if random.choice([True, False]) is True:
                        maxOrders = xbridge_utils.generate_random_int(1, 50)
                    else:
                        maxOrders = None
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token,
                                                   maxOrders, showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1e", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1e", 1, ass_err, [detailLevel, src_Token, dest_Token, maxOrders, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1e", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

    # All parameters are valid, except maxOrders
    def test_invalid_getorderbook_v1f(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel = self.valid_detailLevel
                    src_Token = self.valid_src_Token
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = self.valid_dest_Token
                    if random.choice([True, False]) is True:
                        maxOrders = xbridge_utils.generate_random_int(-99999999999999999999, 0)
                    else:
                        maxOrders = None
                    if random.choice([True, False]) is True:
                        showTxids = "txids"
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token,
                                                                     maxOrders, showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1f", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1f", 1, ass_err,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v1f", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])

                                        
    # Parameters are randomly valid or invalid
    # detailLevel has 1/3 probability of being valid
    def test_invalid_getorderbook_v2(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    detailLevel_Type = random.choice([1, 2, 3])
                    if detailLevel_Type == 1:
                        detailLevel = self.valid_detailLevel
                    if detailLevel_Type == 2:
                        detailLevel = xbridge_utils.generate_random_int(-50, 0)
                    if detailLevel_Type == 3:
                        detailLevel = xbridge_utils.generate_random_int(4, 9999999999999999999999999999999)
                    if random.choice([True, False]) is True:
                        src_Token = self.valid_src_Token
                    else:
                        src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        maxOrders = xbridge_utils.generate_random_int(-50, 50)
                    else:
                        maxOrders = None
                    showTxids_Type = random.choice([1, 2, 3, 4])
                    if showTxids_Type == 1:
                        showTxids = "txids"
                    if showTxids_Type == 2:
                        showTxids = None
                    # We do this so that the probability of having an invalid parameter is 1/2
                    if showTxids_Type == 3 or showTxids_Type == 4:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsInstance(xbridge_rpc.dxGetOrderBook(detailLevel, src_Token, dest_Token,
                                                                     maxOrders, showTxids), dict)
                    xbridge_logger.XLOG("test_invalid_getorderbook_v2", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v2", 1, ass_err,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_getorderbook_v2", 2, json_excpt,
                                        [detailLevel, src_Token, dest_Token, maxOrders, showTxids])                                        
    

# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(10):
    suite.addTest(getOrderBook_Test("test_invalid_getorderbook_v3"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""