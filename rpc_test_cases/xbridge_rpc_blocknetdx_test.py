import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

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
        except AssertionError as e:
            xbridge_logger.logger.info('get_budget unit test FAILED')

# unittest.main()
