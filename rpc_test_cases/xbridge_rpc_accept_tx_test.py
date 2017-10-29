from strgen import StringGenerator
import time
import unittest
import sys

from utils import xbridge_utils
from interface import xbridge_rpc


"""
    - Combine optional parameters in a way that generate the test cases you want.
"""

def dxAccept_RPC_sequence(nb_of_runs=1000, data_nature=xbridge_utils.RANDOM_VALID_INVALID, char_min_size=1, char_max_size=12000):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        xbridge_utils.generate_new_set_of_data(data_nature, char_min_size, char_max_size)
        ts = time.time()
        xbridge_rpc.accept_tx(xbridge_utils.a_random_tx_id, xbridge_utils.a_src_Address, xbridge_utils.a_dest_Address)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxAcceptTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("dxAccept_RPC_sequence.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***
        - Time is not a consideration here.
"""

class accept_Tx_Test(unittest.TestCase):
    # Generate new data before each run
    def setUp(self):
       # Valid data
       self.valid_txid = xbridge_utils.generate_random_valid_txid()
       self.valid_src_Address = xbridge_utils.generate_random_valid_address()
       self.valid_dest_Address = xbridge_utils.generate_random_valid_address()
       # Invalid data
       self.invalid_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.long_txid = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       self.long_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(10000, 12000))
       
    # Combinations of valid and invalid parameters
    def test_invalid_accept_tx_1(self):
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.invalid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, self.invalid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.invalid_txid, self.invalid_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.invalid_txid, self.valid_src_Address, self.valid_dest_Address), dict)

    # Combinations of empty parameters
    def test_invalid_accept_tx_2(self):
        # Test many combinations of 0 to 10 000 white spaces
        self.assertIsInstance(xbridge_rpc.accept_tx(StringGenerator('[\s]{0:10000}').render(), StringGenerator('[\s]{0:10000}').render(), StringGenerator('[\s]{0:10000}').render()), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx("", self.valid_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, "", self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, ""), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx("", "", ""), dict)
    
    # Combinations of character classes
    # This test may LOOK like the others, but it is not, because the generator generates inputs from random combinations of classes.
    def test_invalid_accept_tx_3(self):
        self.assertIsInstance(xbridge_rpc.accept_tx(xbridge_utils.generate_input_from_random_classes_combinations(1, 500), self.valid_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, xbridge_utils.generate_input_from_random_classes_combinations(1, 500), self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, xbridge_utils.generate_input_from_random_classes_combinations(1, 500)), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(xbridge_utils.generate_input_from_random_classes_combinations(1, 500), xbridge_utils.generate_input_from_random_classes_combinations(1, 500), xbridge_utils.generate_input_from_random_classes_combinations(1, 500)), dict)
    
    # Combinations of very long addresses and transaction ids
    def invalid_accept_tx_4(self):
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.long_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.long_txid, self.long_src_Address, self.valid_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.long_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.long_txid, self.valid_src_Address, self.long_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.long_src_Address, self.long_dest_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.long_txid, self.long_src_Address, self.long_dest_Address), dict)
    
    # Combinations of same source and dest Addresses
    def test_invalid_accept_tx_5(self):
        self.assertIsInstance(xbridge_rpc.accept_tx(invalid_txid, self.valid_src_Address, self.valid_src_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.valid_src_Address, self.valid_src_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx("", self.valid_src_Address, self.valid_src_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(invalid_txid, self.invalid_src_Address, self.invalid_src_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx(self.valid_txid, self.invalid_src_Address, self.invalid_src_Address), dict)
        self.assertIsInstance(xbridge_rpc.accept_tx("", self.invalid_src_Address, self.invalid_src_Address), dict)
        

def repeat_accept_tx_unit_tests(nb_of_runs):
    for i in (1, nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)
