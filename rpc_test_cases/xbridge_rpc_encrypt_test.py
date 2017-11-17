import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import random

from utils import xbridge_custom_exceptions
from interface import xbridge_rpc
from utils import xbridge_utils

import sys
sys.path.insert(0,'..')
import xbridge_config

subTest_count = xbridge_config.get_conf_subtests_run_number()

class Encrypt_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    @unittest.skip("NEED A SPECIAL FLAG SO IT DOES NOT SHUTDOWN")
    def test_encryptwallet_noseq(self):
        try:
            log_json = ""
            random_str = random.choice([xbridge_utils.invalid_str_from_random_classes_1, 
                                        xbridge_utils.invalid_str_from_random_classes_2, 
                                        xbridge_utils.invalid_str_from_random_classes_3, 
                                        xbridge_utils.invalid_str_from_random_classes_4])
            self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.encryptwallet, )
            log_json = {"group": "test_encryptwallet", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_encryptwallet", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_encryptwallet", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
    
    def test_bip38encrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38encrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38encrypt, invalid_blocknet_address)
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38encrypt_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_bip38encrypt_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38encrypt_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
    
    def test_bip38decrypt_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_bip38decrypt_invalid"):
                try:
                    invalid_blocknet_address = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.bip38decrypt,
                                      invalid_blocknet_address)
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38decrypt_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_bip38decrypt_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_bip38decrypt_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('invalid_blocknet_address: %s \n' % invalid_blocknet_address)
    
    
# unittest.main()

"""
suite = unittest.TestSuite()
for i in range(20):
    suite.addTest(Encrypt_UnitTest("test_bip38encrypt_invalid"))
    suite.addTest(Encrypt_UnitTest("test_bip38decrypt_invalid"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""

