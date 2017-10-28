from strgen import StringGenerator
import time
import unittest
import sys

from utils import xbridge_utils
from interface import xbridge_rpc


"""                       ***  COMMENT ***

    - Here, the length of the garbage data is very high and increased.
    The "j" parameter in the "generate_input_from_random_classes_combinations" function is the length of the garbage input we want.

    - export_data() function generates :
        1) an Excel File with the recorded timing information.
        2) a small descriptive table with mean, standard deviation, and some quantiles (25%, 50%, 75%).
"""
def test_accept_garbage_load_v1(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for j in range(10000, 10000+nb_of_runs):
        tx_id_str = xbridge_utils.generate_input_from_random_classes_combinations(j, j)
        src_Address_str = xbridge_utils.generate_input_from_random_classes_combinations(j, j)
        dest_Address_str = xbridge_utils.generate_input_from_random_classes_combinations(j, j)
        ts = time.time()
        xbridge_rpc.accept_tx(tx_id_str, src_Address_str, dest_Address_str)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxAcceptTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_accept_garbage_load_v1.xlsx", time_distribution)


"""                       ***  COMMENT ***
    - Here, the length of garbage parameters is random.
"""

def test_accept_garbage_load_v2(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        tx_id_str = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)
        src_Address_str = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)
        dest_Address_str = xbridge_utils.generate_input_from_random_classes_combinations(1, 10000)
        ts = time.time()
        xbridge_rpc.accept_tx(tx_id_str, src_Address_str, dest_Address_str)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxAcceptTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_accept_garbage_load_v2.xlsx", time_distribution)


"""                       ***  COMMENT ***
        - Only valid data is thrown at the API. Load test only.
"""

def test_accept_valid_load(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        tx_id_str = xbridge_utils.generate_random_valid_txid()
        src_Address_str = xbridge_utils.generate_random_valid_address()
        dest_Address_str = xbridge_utils.generate_random_valid_address()
        ts = time.time()
        xbridge_rpc.accept_tx(tx_id_str, src_Address_str, dest_Address_str)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxAcceptTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_accept_tx_valid_load.xlsx", time_distribution)



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
