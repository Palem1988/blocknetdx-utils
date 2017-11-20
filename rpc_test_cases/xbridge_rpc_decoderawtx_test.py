import unittest
import time
import xbridge_logger
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from interface import xbridge_rpc
from utils import xbridge_utils
from utils import xbridge_custom_exceptions

from strgen import StringGenerator

class decodeUnitTest(unittest.TestCase):
    def setUp(self):
       xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size=1, char_max_size=10000)
    
    @unittest.skip("IN TESTING")
    def test_valid_decode_1(self):
        try:
            """
                [I] 2017-Oct-31 23:42:48 [0xb8] rpc call <decoderawtransaction>
                [I] 2017-Oct-31 23:42:48 [0xb8] HTTP: req  decoderawtransaction {"method":"decoderawtransaction","params":["01000000814ef9590108a03740afeb62f97908aba6d79ba512162a0448ead78c1d9acb808b65814914000000006a4730440220111cbcdb9ccdc0e17b65e7fa1e4ec265bf76dcba8202b304b3e34ac833c297b6022008d37ca8ca5ed54bb5d217f5bcdb19c8159059e437a7dbe665c2455b1cfb93fc0121036fa429dbb28304585ebfdae5688bbac546339e578ac4403dcafdc7e15b4f08e1ffffffff0290ab1e000000000017a9145abd1ae96433936b627d249c0c1a57770456323587b0a8db02000000001976a914a5a4651accd909fccaa66e34a7fb5c275c6270ef88ac00000000"],"id":1}

                [I] 2017-Oct-31 23:42:48 [0xb8] HTTP: resp 200 {"result":{"txid":"2e2acb1b085c3b3c5f900153a3280be69a3727b44134342c8a67b0288430f8d6","version":1,"time":1509510785,"locktime":0,"vin":[{"txid":"144981658b80cb9a1d8cd7ea48042a1612a59bd7a6ab0879f962ebaf4037a008","vout":0,"scriptSig":{"asm":"30440220111cbcdb9ccdc0e17b65e7fa1e4ec265bf76dcba8202b304b3e34ac833c297b6022008d37ca8ca5ed54bb5d217f5bcdb19c8159059e437a7dbe665c2455b1cfb93fc01 036fa429dbb28304585ebfdae5688bbac546339e578ac4403dcafdc7e15b4f08e1","hex":"4730440220111cbcdb9ccdc0e17b65e7fa1e4ec265bf76dcba8202b304b3e34ac833c297b6022008d37ca8ca5ed54bb5d217f5bcdb19c8159059e437a7dbe665c2455b1cfb93fc0121036fa429dbb28304585ebfdae5688bbac546339e578ac4403dcafdc7e15b4f08e1"},"sequence":4294967295}],"vout":[{"value":2.01000000,"n":0,"scriptPubKey":{"asm":"OP_HASH160 5abd1ae96433936b627d249c0c1a577704563235 OP_EQUAL","hex":"a9145abd1ae96433936b627d249c0c1a57770456323587","reqSigs":1,"type":"scripthash","addresses":["bM143kSgrZsEksuk2QkiU7zCdGFffyx7iG"]}},{"value":47.95000000,"n":1,"scriptPubKey":{"asm":"OP_DUP OP_HASH160 a5a4651accd909fccaa66e34a7fb5c275c6270ef OP_EQUALVERIFY OP_CHECKSIG","hex":"76a914a5a4651accd909fccaa66e34a7fb5c275c6270ef88ac","reqSigs":1,"type":"pubkeyhash","addresses":["SD4EUkDd5kyiGByjYbGtUPrvHqFjv5nVnZ"]}}]},"error":null,"id":1}
            """
            self.assertIsInstance(xbridge_rpc.decode_raw_tx("01000000814ef9590108a03740afeb62f97908aba6d79ba512162a0448ead78c1d9acb808b65814914000000006a4730440220111cbcdb9ccdc0e17b65e7fa1e4ec265bf76dcba8202b304b3e34ac833c297b6022008d37ca8ca5ed54bb5d217f5bcdb19c8159059e437a7dbe665c2455b1cfb93fc0121036fa429dbb28304585ebfdae5688bbac546339e578ac4403dcafdc7e15b4f08e1ffffffff0290ab1e000000000017a9145abd1ae96433936b627d249c0c1a57770456323587b0a8db02000000001976a914a5a4651accd909fccaa66e34a7fb5c275c6270ef88ac00000000"), dict)
        except AssertionError as e:
            xbridge_logger.logger.info('test_valid_decode_1 FAILED')
    
    def test_invalid_decode_1(self):
        for basic_garbage_str in xbridge_utils.set_of_invalid_parameters:
            with self.subTest(basic_garbage_str=basic_garbage_str):
                try:
                    if basic_garbage_str in (9999999999999999999999999999999999999999999999999999999999999999, -9999999999999999999999999999999999999999999999999999999999999999):
                        self.assertIsNone(xbridge_rpc.decode_raw_tx(basic_garbage_str))
                    else:
                        self.assertRaises(xbridge_custom_exceptions.ValidBlockNetException, xbridge_rpc.decode_raw_tx, basic_garbage_str)
                    log_json = {"group": "test_invalid_decode_1", "success": 1, "failure": 0, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                except AssertionError as ass_err:
                    xbridge_logger.logger.info('test_invalid_decode_1 unit test FAILED: %s' % ass_err)
                    log_json = {"group": "test_invalid_decode_1", "success": 0, "failure": 1, "error": 0}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('basic_garbage_str: %s \n' % basic_garbage_str)
                    xbridge_logger.logger.info('param: %s' % basic_garbage_str)
                except JSONRPCException as json_excpt:
                    log_json = {"group": "test_invalid_decode_1", "success": 0,  "failure": 0, "error": 1}
                    xbridge_utils.ERROR_LOG.append(log_json)
                    xbridge_logger.logger.info('test_invalid_decode_1 unit test ERROR: %s' % str(json_excpt))
                    xbridge_logger.logger.info('param: %s' % basic_garbage_str)

    
    """
          - We test various random inputs from individual character classes.
          - We then combine those character classes.
          - Size of the input parameter is fixed.
    """
    def test_invalid_decode_2(self):
        string_length=64
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_length) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.decode_raw_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_decode_2", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        xbridge_logger.logger.info('test_invalid_decode_2 FAILED: %s', ass_err)
                        log_json = {"group": "test_invalid_decode_2", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('param: %s \n' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_decode_2", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_decode_2 ERROR: %s' % str(json_excpt))
                        xbridge_logger.logger.info('param: %s \n' % generated_str)


    """
          - Same as before, but now the random strings are of random but always very long size [9 000-11 000]
    """
    def test_invalid_decode_3(self):
        string_lower_bound=9000
        string_upper_bound=11000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.decode_raw_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_decode_3", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        xbridge_logger.logger.info('test_invalid_decode_3 FAILED: %s', ass_err)
                        log_json = {"group": "test_invalid_decode_3", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('param: %s \n' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_decode_3", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_decode_3 ERROR: %s' % str(json_excpt))
                        xbridge_logger.logger.info('param: %s \n' % generated_str)

                            
    """
          - Same as before, but now the random input parameters are of random length [1-4 000]
    """
    def test_invalid_decode_4(self):
        run_count = 0
        string_lower_bound=1
        string_upper_bound=4000
        for itm in [xbridge_utils.one_classes_list, xbridge_utils.two_classes_list, xbridge_utils.three_classes_list, xbridge_utils.four_classes_list, xbridge_utils.five_classes_list]:
            for sub_item in itm:
                with self.subTest(sub_item=sub_item):
                    clss_str = sub_item + "{" + str(string_lower_bound) + ":" + str(string_upper_bound) + "}"
                    try:
                        generated_str = StringGenerator(clss_str).render()
                        self.assertIsInstance(xbridge_rpc.decode_raw_tx(generated_str), dict)
                        log_json = {"group": "test_invalid_decode_4", "success": 1, "failure": 0, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                    except AssertionError as ass_err:
                        xbridge_logger.logger.info('test_invalid_decode_4 FAILED: %s', ass_err)
                        log_json = {"group": "test_invalid_decode_4", "success": 0, "failure": 1, "error": 0}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('param: %s \n' % generated_str)
                    except JSONRPCException as json_excpt:
                        log_json = {"group": "test_invalid_decode_4", "success": 0, "failure": 0, "error": 1}
                        xbridge_utils.ERROR_LOG.append(log_json)
                        xbridge_logger.logger.info('test_invalid_decode_4 ERROR: %s' % str(json_excpt))
                        xbridge_logger.logger.info('param: %s \n' % generated_str)


"""
def repeat_decode_raw_tx_unit_tests(runs=1000):
    for j in (1, runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)
"""

"""
if __name__ == '__main__':
    unittest.main()

unittest.main()
"""

