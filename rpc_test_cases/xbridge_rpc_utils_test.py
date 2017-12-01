import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random
from decimal import *

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class Utils_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    # estimatefee nblocks
    def test_estimatefee(self):
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, int):
                        if basic_str in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999):
                            self.assertIsNone(xbridge_rpc.estimatepriority(basic_str))
                        else:
                            self.assertIsInstance(xbridge_rpc.estimatepriority(basic_str), Decimal)
                    else:
                        self.assertIsNone(xbridge_rpc.estimatefee(basic_str))
                    xbridge_logger.XLOG("test_estimatefee", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_estimatefee", 1, ass_err, [basic_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_estimatefee", 2, json_excpt, [basic_str])

    # estimatepriority nblocks
    def test_estimatepriority(self):
        # modified_set = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, int)]
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, int):
                        if basic_str in (-9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999):
                            self.assertIsNone(xbridge_rpc.estimatepriority(basic_str))
                        else:
                            self.assertIsInstance(xbridge_rpc.estimatepriority(basic_str), Decimal)
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.estimatepriority, basic_str)
                    xbridge_logger.XLOG("test_estimatepriority", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_estimatepriority", 1, ass_err, [basic_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_estimatepriority", 2, json_excpt, [basic_str])

    # validateaddress "blocknetdxaddress"
    # Trello OK
    def test_validateaddress_invalid(self):
        for basic_str in xbridge_utils.set_of_invalid_parameters:
            log_json = ""
            with self.subTest(basic_str=basic_str):
                try:
                    if isinstance(basic_str, str):
                        self.assertIsInstance(xbridge_rpc.validateaddress(basic_str), dict)
                    else:
                        self.assertIsNone(xbridge_rpc.validateaddress(basic_str))
                    xbridge_logger.XLOG("test_validateaddress_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_validateaddress_invalid", 1, ass_err, [basic_str])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_validateaddress_invalid", 2, json_excpt, [basic_str])

    # validateaddress "blocknetdxaddress"
    def test_validateaddress_valid(self):
        try:
            valid_block_address = xbridge_utils.generate_valid_blocknet_address()
            self.assertIsInstance(xbridge_rpc.validateaddress(valid_block_address), dict)
            xbridge_logger.XLOG("test_validateaddress_valid", 0)
        except AssertionError as ass_err:
            xbridge_logger.XLOG("test_validateaddress_valid", 1, ass_err, [valid_block_address])
        except JSONRPCException as json_excpt:
            xbridge_logger.XLOG("test_validateaddress_valid", 2, json_excpt, [valid_block_address])

    # verifymessage "blocknetdxaddress" "signature" "message"
    # Trello OK
    def test_verify_message_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_verify_message_invalid"):
                try:
                    blocknetdxaddress = random.choice(xbridge_utils.set_of_invalid_parameters)
                    signature = random.choice(xbridge_utils.set_of_invalid_parameters)
                    message = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertIsNone(xbridge_rpc.verifymessage(blocknetdxaddress, signature, message))
                    xbridge_logger.XLOG("test_verify_message_invalid", 0)
                except AssertionError as ass_err:
                    xbridge_logger.XLOG("test_verify_message_invalid", 1, ass_err, [blocknetdxaddress, signature, message])
                except JSONRPCException as json_excpt:
                    xbridge_logger.XLOG("test_verify_message_invalid", 2, json_excpt, [blocknetdxaddress, signature, message])
   
# unittest.main()

"""
suite = unittest.TestSuite()
# suite.addTest(Misc_UnitTest("test_validateaddress_valid"))
suite.addTest(Misc_UnitTest("test_validateaddress_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

