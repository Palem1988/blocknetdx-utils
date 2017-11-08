from strgen import StringGenerator
import time
import unittest
import xbridge_logger

from utils import xbridge_utils
from interface import xbridge_rpc


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""

def dxAccept_RPC_sequence(nb_of_runs=1000, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    for i in range(1, 1 + nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
        te = time.time()
        elapsed_Time = te - ts
        json_str = {"time": te - ts, "API": "dxAcceptTransaction"}
        time_distribution.append(json_str)
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "dxAccept_RPC_sequence",
                         "API": "dxAccept", "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
    xbridge_utils.export_data("dxAccept_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***
        - Time is not a consideration here.
"""

class accept_Tx_Test(unittest.TestCase):
    def setUp(self):
       # Valid data
       self.valid_txid = xbridge_utils.generate_random_valid_txid()
       self.valid_src_Address = xbridge_utils.generate_random_valid_address()
       self.valid_dest_Address = xbridge_utils.generate_random_valid_address()
       # Invalid data from garbage character classes
       self.invalid_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.long_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       # Invalid data from random character classes
       self.input_str_from_random_classes_1 = xbridge_utils.generate_input_from_random_classes_combinations(1, 4000)
       self.input_str_from_random_classes_2 = xbridge_utils.generate_input_from_random_classes_combinations(9000, 12000)
       self.input_str_from_random_classes_3 = xbridge_utils.generate_input_from_random_classes_combinations(1, 100)
       
    # Combinations of valid and invalid parameters
    def test_invalid_accept_tx_1(self):
        try:
           log_json = ""
           self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.valid_dest_Address))
           self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.valid_dest_Address))
           self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.invalid_dest_Address))
           self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, self.invalid_dest_Address))
           self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, self.valid_dest_Address))
           self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.valid_src_Address, self.valid_dest_Address))
           # print("dxAccept Unit Test Group 1 OK")
           log_json = {"group": "test_invalid_accept_tx_1", "success": 1, "failure": 0, "error": 0}
           xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            # print("****** dxAccept Unit Test Group 1 FAILED ******")
            log_json = {"group": "test_invalid_accept_tx_1", "success": 0, "error": 1}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('-------- dxAccept unit test group 1 FAILED --------: %s \n' % str(ass_err))
            xbridge_logger.logger.info('valid_txid: %s', self.valid_txid)
            xbridge_logger.logger.info('invalid_txid: %s', self.invalid_txid)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address)
            xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address)

    # Combinations of empty parameters
    def test_invalid_accept_tx_2(self):
        try:
            log_json = ""
            # Test many combinations of 0 to 10 000 white spaces
            whitespace_str_1 = StringGenerator('[\s]{1:10000}').render()
            whitespace_str_2 = StringGenerator('[\s]{1:10000}').render()
            whitespace_str_3 = StringGenerator('[\s]{1:10000}').render()
            self.assertIsNone(xbridge_rpc.accept_tx(whitespace_str_1, whitespace_str_2, whitespace_str_3))
            self.assertIsNone(xbridge_rpc.accept_tx("", self.valid_src_Address, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx("", self.invalid_src_Address, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, "", self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, ""))
            self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, "", self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, ""))
            self.assertIsNone(xbridge_rpc.accept_tx("", "", ""))
            # print("dxAccept Unit Test Group 2 OK")
            log_json = {"group": "test_invalid_accept_tx_2", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            # print("****** dxAccept Unit Test Group 2 FAILED ******")
            log_json = {"group": "test_invalid_accept_tx_2", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('-------- dxAccept unit test group 2 FAILED --------: %s \n' % str(ass_err))
            xbridge_logger.logger.info('valid_txid: %s', self.valid_txid)
            xbridge_logger.logger.info('invalid_txid: %s', self.invalid_txid)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address)
            xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address)
            xbridge_logger.logger.info('whitespace_str_1 length: %s', len(whitespace_str_1))
            xbridge_logger.logger.info('whitespace_str_2 length: %s', len(whitespace_str_2))
            xbridge_logger.logger.info('whitespace_str_3 length: %s', len(whitespace_str_3))
            
    
    # Input parameter(s) is from combination of random character classes
    def test_invalid_accept_tx_3(self):
        try:
            log_json = ""
            self.assertIsNone(xbridge_rpc.accept_tx(self.input_str_from_random_classes_1, self.valid_src_Address, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.input_str_from_random_classes_1, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.input_str_from_random_classes_1))
            self.assertIsNone(xbridge_rpc.accept_tx(self.input_str_from_random_classes_1, self.input_str_from_random_classes_1, self.input_str_from_random_classes_1))
            self.assertIsNone(xbridge_rpc.accept_tx(self.input_str_from_random_classes_1, self.input_str_from_random_classes_2, self.input_str_from_random_classes_3))
            # print("dxAccept Unit Test Group 3 OK")
            log_json = {"group": "test_invalid_accept_tx_3", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            # print("****** dxAccept Unit Test Group 3 FAILED ******")
            log_json = {"group": "test_invalid_accept_tx_3", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('-------- dxAccept unit test group 3 FAILED --------: %s \n' % str(ass_err))
            xbridge_logger.logger.info('valid_txid: %s', self.valid_txid)
            xbridge_logger.logger.info('input_str_from_random_classes_1: %s', self.input_str_from_random_classes_1)
            xbridge_logger.logger.info('input_str_from_random_classes_2: %s', self.input_str_from_random_classes_2)
            xbridge_logger.logger.info('input_str_from_random_classes_3: %s', self.input_str_from_random_classes_3)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address)
            xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address)
        
    
    # Combinations of very long addresses and transaction ids
    def invalid_accept_tx_4(self):
        try:
            log_json = ""
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.long_src_Address, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.long_txid, self.long_src_Address, self.valid_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.long_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.long_txid, self.valid_src_Address, self.long_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.long_src_Address, self.long_dest_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.long_txid, self.long_src_Address, self.long_dest_Address))
            # print("dxAccept Unit Test Group 4 OK")
            log_json = {"group": "invalid_accept_tx_4", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            # print("****** dxAccept Unit Test Group 4 FAILED ******")
            log_json = {"group": "invalid_accept_tx_4", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('-------- dxAccept unit test group 4 FAILED --------: %s \n' % str(ass_err))
            xbridge_logger.logger.info('valid_txid: %s', self.valid_txid)
            xbridge_logger.logger.info('long_txid: %s', self.long_txid)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('valid_dest_Address: %s', self.valid_dest_Address)
            xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address)
            xbridge_logger.logger.info('invalid_dest_Address: %s', self.invalid_dest_Address)
            xbridge_logger.logger.info('long_src_Address: %s', self.long_src_Address)
            xbridge_logger.logger.info('long_dest_Address: %s', self.long_dest_Address)
    
    # Combinations of same source and dest Addresses
    def test_invalid_accept_tx_5(self):
        try:
            log_json = ""
            self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.valid_src_Address, self.valid_src_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.valid_src_Address))
            self.assertIsNone(xbridge_rpc.accept_tx("", self.valid_src_Address, self.valid_src_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, self.invalid_src_Address))
            self.assertIsNone(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.invalid_src_Address))
            self.assertIsNone(xbridge_rpc.accept_tx("", self.invalid_src_Address, self.invalid_src_Address))
            # print("dxAccept Unit Test Group 5 OK")
            log_json = {"group": "test_invalid_accept_tx_5", "success": 1, "failure": 0, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
        except AssertionError as ass_err:
            # print("****** dxAccept Unit Test Group 5 FAILED ******")
            log_json = {"group": "test_invalid_accept_tx_5", "success": 0, "failure": 1, "error": 0}
            xbridge_utils.ERROR_LOG.append(log_json)
            xbridge_logger.logger.info('-------- dxAccept unit test group 5 FAILED --------: %s \n' % str(ass_err))
            xbridge_logger.logger.info('valid_txid: %s', self.valid_txid)
            xbridge_logger.logger.info('invalid_txid: %s', self.invalid_txid)
            xbridge_logger.logger.info('valid_src_Address: %s', self.valid_src_Address)
            xbridge_logger.logger.info('invalid_src_Address: %s', self.invalid_src_Address)
        
"""
def repeat_accept_tx_unit_tests(nb_of_runs):
    for i in (1, 1+nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

unittest.main()
"""


