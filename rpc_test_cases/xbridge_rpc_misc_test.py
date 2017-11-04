import unittest
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import *

from interface import xbridge_rpc
from utils import xbridge_utils

"""                       ***  UNIT TESTS ***

"""

# OK
# No param, returns int
no_param_returns_int_func_list = [xbridge_rpc.rpc_connection.getconnectioncount,
                    xbridge_rpc.rpc_connection.getdifficulty
                    ]

# OK
# int or double param
single_amount_param_func_list = [
                    xbridge_rpc.rpc_connection.keypoolrefill]

# OK but make assertions more precise
# account/single string as param
account_func_list = [
                    xbridge_rpc.rpc_connection.submitblock,
                    xbridge_rpc.rpc_connection.gettransaction,
                    xbridge_rpc.rpc_connection.importaddress,
                    xbridge_rpc.rpc_connection.dumpprivkey,
                    xbridge_rpc.rpc_connection.dumpwallet,
                    xbridge_rpc.rpc_connection.getbalance,
                    xbridge_rpc.rpc_connection.backupwallet
                    ]

# OK
no_param_returns_dict_func_list = [
                        xbridge_rpc.rpc_connection.getnettotals,
                        xbridge_rpc.rpc_connection.getnetworkinfo,
                        xbridge_rpc.rpc_connection.getstakingstatus,
                        xbridge_rpc.rpc_connection.getwalletinfo
                    ]

# UNTESTED
no_param_returns_list_func_list = [
                        xbridge_rpc.rpc_connection.getaddressesbyaccount,
                        xbridge_rpc.rpc_connection.listaccounts,
                        xbridge_rpc.rpc_connection.listaddressgroupings,
                        xbridge_rpc.rpc_connection.listlockunspent,
                        xbridge_rpc.rpc_connection.listreceivedbyaccount,
                        xbridge_rpc.rpc_connection.listreceivedbyaddress
                    ]
                    
class Misc_UnitTest(unittest.TestCase):
    def setUp(self):
        xbridge_utils.generate_new_set_of_data(data_nature=3, char_min_size=1, char_max_size=10000)
        
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
            
    @unittest.skip("Still untested ==> generate rpc error")
    def test_group_no_param_return_int(self):
        for func_name in no_param_returns_int_func_list:
            with self.subTest("test_group_no_param_return_int"):
                try:
                    result = func_name()
                    print("%s: %s" % (func_name, result))
                    self.assertIsInstance(result , int)
                    self.assertGreater(result, 0)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    # @unittest.skip("disabled")
    def test_group_no_param_return_dict_batch(self):
        for func_name in no_param_returns_dict_func_list:
            with self.subTest("batch test of no_param_returns_dict_func_list"):
                try:
                    result = func_name()
                    print("%s: %s" % (func_name, result))
                    self.assertIsInstance(result, dict)
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
        
    @unittest.skip("Disabled -> generate Auth Error")
    def test_group_amount_param(self):
        for func_name in single_amount_param_func_list:
            with self.subTest("test_group_amount_param"):
                try:
                    result = func_name()
                    self.assertIsNotNone(result)
                except AssertionError as e:
                    xbridge_logger.logger.info('%s unit test FAILED' % str(func_name))

    def test_setfee(self):
        try:
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(0))
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(10))
            self.assertTrue(xbridge_rpc.rpc_connection.settxfee(0.00000000000000000000000000000000000000000000000000000001))
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, -10)
            neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999, -0.0000000000000000000000000000000000000000000000000000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, neg_number)
            large_positive_nb = xbridge_utils.generate_random_number(999999999999999999999999, 99999999999999999999999999999999999999999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, large_positive_nb)
        except AssertionError:
            xbridge_logger.logger.info('test_setfee unit test FAILED')

    def test_get_stake_threshold(self):
        try:
            # return {'split stake threshold set to ': 2000}
            rst = xbridge_rpc.rpc_connection.getstakesplitthreshold()
            self.assertIsInstance(rst, dict)
        except AssertionError:
            xbridge_logger.logger.info('get_stake_threshold unit test FAILED')

    def test_getpeerinfo(self):
        try:
            peer = xbridge_rpc.rpc_connection.getpeerinfo()
            self.assertIsInstance(peer, list)
            self.assertGreater(len(peer), 0)
        except AssertionError:
            xbridge_logger.logger.info('getpeerinfo unit test FAILED')

    def test_new_address(self):
        try:
            new_address = xbridge_rpc.rpc_connection.getnewaddress()
            self.assertIsInstance(new_address, str)
            # self.assertGreater(len(peer), 0)
        except AssertionError:
            xbridge_logger.logger.info('getnewaddress unit test FAILED')

    def test_get_received_by_account(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(""), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(" "), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("----"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("["), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("[]"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{}"), Decimal)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount("{}"), Decimal)
            # self.assertIsInstance(xbridge_rpc.rpc_connection.getreceivedbyaccount(xbridge_utils.ca_random_tx_id, Decimal))
        except AssertionError:
            xbridge_logger.logger.info('get_received_by_account unit test FAILED')

    def test_getreceivedbyaddress(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, "{}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getreceivedbyaddress, xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('getreceivedbyaddress unit test FAILED')

    def test_getaccount(self):
        try:
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, " ")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "----")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "{")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "}")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "[")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "[]")
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, "{}")
            # self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getaccount, xbridge_utils.ca_random_tx_id)
        except AssertionError:
            xbridge_logger.logger.info('getaccount unit test FAILED')

    def test_getaccountaddress(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(""), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(" "), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("----"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("{"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("}"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("["), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("]"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("[]"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress("{}"), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaccountaddress(xbridge_utils.ca_random_tx_id), str)
        except AssertionError:
            xbridge_logger.logger.info('getaccountaddress unit test FAILED')

    def test_getaddressesbyaccount(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(""), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(" "), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("----"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("****"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("{"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("}"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("["), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("]"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("[[]]"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount("{}"), list)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getaddressesbyaccount(xbridge_utils.ca_random_tx_id), list)
        except AssertionError:
            xbridge_logger.logger.info('getaddressesbyaccount unit test FAILED')

    def test_getblockhash(self):
        try:
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(0), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(10), str)
            self.assertIsInstance(xbridge_rpc.rpc_connection.getblockhash(100000), str)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -10)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 100000000000000)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, -0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 0.0000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, 10.2)
            neg_number = xbridge_utils.generate_random_number(-9999999999999999999999999999999999999999999999999999,
                                                              -0.0000000000000000000000000000000000000000000000000000000000001)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.getblockhash, neg_number)
            large_positive_nb = xbridge_utils.generate_random_number(99999999999999999999999999,
                                                                     99999999999999999999999999999999999999999999999999999999999999999999999999)
            self.assertRaises(JSONRPCException, xbridge_rpc.rpc_connection.settxfee, large_positive_nb)
        except AssertionError:
            xbridge_logger.logger.info('getblockhash unit test FAILED')


# xbridge_rpc.rpc_connection.getblockhash,
# unittest.main()
