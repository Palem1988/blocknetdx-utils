import unittest
import xbridge_logger
import random

from interface import xbridge_rpc
from interface import xbridge_utils



"""                       ***  UNIT TESTS ***

"""

# No param, returns int
no_param_returns_int_func_list = [xbridge_rpc.rpc_connection.getconnectioncount,
                    xbridge_rpc.rpc_connection.getdifficulty,
                    xbridge_rpc.rpc_connection.getstakesplitthreshold
                    ]

# int or double param
single_amount_param_func_list = [xbridge_rpc.rpc_connection.settxfee,
                    xbridge_rpc.rpc_connection.getblockhash,
                    xbridge_rpc.rpc_connection.keypoolrefill,
                    xbridge_rpc.rpc_connection.setstakesplitthreshold]
               
# account/single string as param
account_func_list = [xbridge_rpc.rpc_connection.getnewaddress,
                    xbridge_rpc.rpc_connection.getreceivedbyaccount,
                    xbridge_rpc.rpc_connection.getreceivedbyaddress,
                    xbridge_rpc.rpc_connection.submitblock,
                    xbridge_rpc.rpc_connection.gettransaction,
                    xbridge_rpc.rpc_connection.importaddress,
                    xbridge_rpc.rpc_connection.dumpprivkey,
                    xbridge_rpc.rpc_connection.dumpwallet,
                    xbridge_rpc.rpc_connection.getaccount,
                    xbridge_rpc.rpc_connection.getaccountaddress,
                    xbridge_rpc.rpc_connection.getaddressesbyaccount,
                    xbridge_rpc.rpc_connection.getbalance
                    xbridge_rpc.rpc_connection.backupwallet
                    ]
               

no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo

                    ]
               
no_param_returns_list_func_list = [
                        xbridge_rpc.rpc_connection.listaccounts,
                        xbridge_rpc.rpc_connection.listaddressgroupings,
                        xbridge_rpc.rpc_connection.listlockunspent,
                        xbridge_rpc.rpc_connection.listreceivedbyaccount,
                        xbridge_rpc.rpc_connection.listreceivedbyaddress

                    ]
                    
                    
class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        
    def test_get_blockcount(self):
        try:
            self.assertIsInstance(xbridge_rpc.get_blockcount() , int)
            self.assertGreater(xbridge_rpc.get_blockcount(), 120000)
        except AssertionError as e:
            xbridge_logger.logger.info('get_blockcount unit test FAILED')

    def test_get_budget(self):
        try:
            budget = xbridge_rpc.get_budget()
            hash_value = "1e23e3b04773450f84584ce222e318682b50d2a65d2a082a4821b378145263fe"
            self.assertIsInstance(budget , dict)
            self.assertEqual(budget["dev-fund"]["Hash"], hash_value)
        except AssertionError as e:
            xbridge_logger.logger.info('get_budget unit test FAILED')

    def test_get_node_list(self):
        try:
            node_list = xbridge_rpc.get_node_list()
            self.assertIsInstance(node_list , list)
            self.assertGreater(len(node_list), 250)
        except AssertionError as e:
            xbridge_logger.logger.info('get_node_list unit test FAILED')

    def test_get_version(self):
        try:
            version_nb = xbridge_rpc.get_core_version()
            self.assertIsInstance(version_nb , int)
            self.assertGreater(version_nb, 3073600)
        except AssertionError as e:
            xbridge_logger.logger.info('get_version unit test FAILED')
            
    @unittest.skip("Still untested")
    def test_group_no_param_return_int(self):
        for func_name in no_param_returns_int_func_list:
            with self.subTest("test_group_no_param_return_int-2"):
                try:
                    result = func_name()
                    self.assertIsNotNone(result)
                    self.assertIsInstance(result , int)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))
                    
    @unittest.skip("Still untested")
    def test_group_str_param(self):
        for func_name in account_func_list:
            with self.subTest("test_group_str_param"):
                try:
                    result = func_name()
                    self.assertIsNotNone(result)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))
        
    @unittest.skip("Still untested")
    def test_group_amount_param(self):
        for func_name in single_amount_param_func_list:
            with self.subTest("test_group_amount_param"):
                try:
                    result = func_name()
                    self.assertIsNotNone(result)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))
