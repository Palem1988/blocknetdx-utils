import unittest
import random
import time

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from utils import xbridge_utils
from interface import xbridge_rpc
import xbridge_logger

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()
MAX_LOG_LENGTH = xbridge_config.get_param_max_char_length_to_display()

class GetTradeHistory_Test(unittest.TestCase):
    def setUp(self):
       xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
       # Valid data
       self.valid_src_Token = xbridge_utils.generate_random_valid_token()
       self.valid_dest_Token = xbridge_utils.generate_random_valid_token()
       # Common pools from which parameters will be randomnly picked
       self.valid_token = xbridge_utils.generate_random_valid_token()
       self.token_pool = [self.valid_token, xbridge_utils.c_src_Token]
       self.invalid_short_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 40))
       self.invalid_med_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_long_str = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(5000, 15000))
       
    """
        dxGetTradeHistory "
                            "(from currency) (to currency) (start time) (end time) (txids - optional) ");
    """

    # All parameters are drawn from an invalid pool
    def test_invalid_gettradehistory_v1(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_starttime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_endtime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime, showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v1", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v1", 1, ass_err, [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v1", 2, json_excpt, [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])

    # All parameters are drawn from an invalid pool, except the first one
    def test_invalid_gettradehistory_v2(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = self.valid_token
                    dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_starttime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_endtime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime,
                                                      showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v2", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v2", 1, ass_err,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v2", 2, json_excpt,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])

    # All parameters, except the first two params, are drawn from an invalid pool
    def test_invalid_gettradehistory_v3(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = self.valid_src_Token
                    dest_Token = self.valid_dest_Token
                    unix_starttime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_endtime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime,
                                                      showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v3", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v3", 1, ass_err,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v3", 2, json_excpt,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])

    # All parameters, except the first three params, are drawn from an invalid pool
    def test_invalid_gettradehistory_v4(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = self.valid_src_Token
                    dest_Token = self.valid_dest_Token
                    unix_starttime = int(time.time())
                    unix_endtime = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime, showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v4", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v4", 1, ass_err,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v4", 2, json_excpt,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])

    # All parameters are invalid, except the first four. The last param is never optional in these scenarios
    def test_invalid_gettradehistory_v5(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    dest_Token = self.valid_dest_Token
                    unix_starttime = int(time.time())
                    unix_endtime = int(time.time())
                    showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsInstance(
                        xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime, showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v5", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v5", 1, ass_err, [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v5", 2, json_excpt, [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])

    # All parameters are valid, except the second one
    def test_invalid_gettradehistory_v6(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    src_Token = self.valid_dest_Token
                    dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    unix_starttime = int(time.time())
                    unix_endtime = int(time.time())
                    if random.choice([True, False]) is True:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    else:
                        showTxids = None
                    self.assertIsInstance(
                        xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime,
                                                      showTxids), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v6", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v6", 1, ass_err,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v6", 2, json_excpt,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime, showTxids])
                                        
    # Parameters are randomly valid or invalid
    # detailLevel has 1/3 probability of being valid
    """
        dxGetTradeHistory "
                            "(from currency) (to currency) (start time) (end time) (txids - optional) ");
    """
    def test_invalid_gettradehistory_v7(self):
        for i in range(subTest_count):
            with self.subTest("random garbage"):
                try:
                    if random.choice([True, False]) is True:
                        src_Token = self.valid_src_Token
                    else:
                        src_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([1, 2, 3, 4, 5]) == 5:
                        dest_Token = src_Token
                    else:
                        dest_Token = random.choice(xbridge_utils.set_of_invalid_parameters)
                    if random.choice([True, False]) is True:
                        unix_starttime = time.time()
                    else:
                        unix_starttime = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999, 0)
                    if random.choice([True, False]) is True:
                        unix_endtime = time.time()
                    else:
                        unix_endtime = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999, 0)
                    showTxids_Type = random.choice([1, 2, 3, 4])
                    if showTxids_Type == 1:
                        showTxids = "txids"
                    if showTxids_Type == 2:
                        showTxids = None
                    # We do this so that the probability of having an invalid parameter is 1/2
                    if showTxids_Type == 3 or showTxids_Type == 4:
                        showTxids = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsInstance(xbridge_rpc.dxGetTradeHistory(src_Token, dest_Token, unix_starttime, unix_endtime), list)
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v7", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v7", 1, ass_err,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_invalid_gettradehistory_v7", 2, json_excpt,
                                        [src_Token, dest_Token, unix_starttime, unix_endtime])


# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(10):
    suite.addTest(GetTradeHistory_Test("test_invalid_gettradehistory_v7"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""