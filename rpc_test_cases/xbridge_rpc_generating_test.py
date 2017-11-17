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

class Generate_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)

    def test_getgenerate(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.getgenerate(), bool)
            log_json = {"group": "test_getgenerate", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_getgenerate", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_getgenerate", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
        
    def test_gethashespersec(self):
        try:
            log_json = ""
            self.assertIsInstance(xbridge_rpc.rpc_connection.gethashespersec(), int)
            log_json = {"group": "test_gethashespersec", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            log_json = {"group": "test_gethashespersec", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except JSONRPCException as json_excpt:
            log_json = {"group": "test_gethashespersec", "success": 0, "failure": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)       

    # setgenerate generate ( genproclimit )
    def test_setgenerate_invalid(self):
        for i in range(subTest_count):
            log_json = ""
            with self.subTest("test_setgenerate_invalid"):
                try:
                    set_without_bools = [x for x in xbridge_utils.set_of_invalid_parameters if not isinstance(x, bool)]
                    generate = random.choice(set_without_bools)
                    if random.choice(["", xbridge_utils.set_of_invalid_parameters]) == "":
                        genproclimit = None
                    else:
                        genproclimit = random.choice(xbridge_utils.set_of_invalid_parameters)
                    self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.setgenerate, generate, genproclimit)
                    log_json = {"group": "test_setgenerate_invalid", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    log_json = {"group": "test_setgenerate_invalid", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_setgenerate_invalid FAILED: %s' % ass_err)
                    xbridge_logger.logger.info('generate: %s \n' % generate)
                    xbridge_logger.logger.info('genproclimit: %s \n' % str(genproclimit))
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_setgenerate_invalid", "success": 0, "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_setgenerate_invalid ERROR: %s' % json_excpt)
                    xbridge_logger.logger.info('generate: %s \n' % generate)
                    xbridge_logger.logger.info('genproclimit: %s \n' % str(genproclimit))
            

# unittest.main()

"""
suite = unittest.TestSuite()
suite.addTest(Misc_UnitTest("test_getgenerate"))
runner = unittest.TextTestRunner()
runner.run(suite)
"""
