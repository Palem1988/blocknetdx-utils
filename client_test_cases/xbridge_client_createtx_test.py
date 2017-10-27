import time
import unittest
import sys

from utils import xbridge_utils
from interface import xbridge_client


"""                       ***  COMMENT ***

    - Here, the length of the garbage data is very high and increased.
    The "j" parameter in the "generate_garbage_input" function is the length of the garbage input we want.

    - Non-numerical parameters are only garbage data.

    - Numerical parameters are both valid and out-of-bounds numbers.

    - export_data() function generates :
        1) an Excel File with the recorded timing information.
        2) a small descriptive table with mean, standard deviation, and some quantiles (25%, 50%, 75%).
"""

def test_createtx_garbage_load_v1(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for j in range(10000, 10000+nb_of_runs):
        garbage_input_str1 = xbridge_utils.generate_garbage_input(j)
        garbage_input_str2 = xbridge_utils.generate_garbage_input(j)
        garbage_input_str3 = xbridge_utils.generate_garbage_input(j)
        garbage_input_str4 = xbridge_utils.generate_garbage_input(j)
        source_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999)
        dest_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999)
        ts = time.time()
        xbridge_client.CHECK_CREATE_TX(garbage_input_str1, garbage_input_str2, source_nb, garbage_input_str3, garbage_input_str4,
                            dest_nb)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxCreateTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_createtx_garbage_load_v1.xlsx", time_distribution)


"""                       ***  COMMENT ***

    1. Here, the length of garbage parameters is random.
    2. Numerical parameters are both valid and out-of-bounds numbers.

"""

def test_createtx_garbage_load_v2(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        garbage_input_str1 = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 10000))
        garbage_input_str2 = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 10000))
        garbage_input_str3 = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 10000))
        garbage_input_str4 = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 10000))
        source_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999)
        dest_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, 99999999999999999999999999999999999999999999999)
        ts = time.time()
        xbridge_client.CHECK_CREATE_TX(garbage_input_str1, garbage_input_str2, source_nb, garbage_input_str3, garbage_input_str4,
                            dest_nb)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": "dxCreateTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_createtx_garbage_load_v2.xlsx", time_distribution)


"""                       ***  COMMENT ***

    1. Here, The length of parameters is kept fixed, we just increase the number of iterations ==> Pure load test, when resources are available.
    2. Numerical parameters are both valid and out-of-bounds numbers.
    3. Address and tokens parameters are garbage data.

"""

def test_createtx_valid_load(number_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, number_of_runs):
        garbage_input_str1 = xbridge_utils.generate_garbage_input(64)
        garbage_input_str2 = xbridge_utils.generate_garbage_input(64)
        garbage_input_str3 = xbridge_utils.generate_garbage_input(64)
        garbage_input_str4 = xbridge_utils.generate_garbage_input(64)
        source_nb = xbridge_utils.generate_random_number(0.1, 1000)
        dest_nb = xbridge_utils.generate_random_number(0.1, 1000)
        ts = time.time()
        xbridge_client.CHECK_CREATE_TX(garbage_input_str1, garbage_input_str2, source_nb, garbage_input_str3, garbage_input_str4,
                            dest_nb)
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "char_nb": 64, "API": "dxCreateTransaction"}
        time_distribution.append(json_str)
    xbridge_utils.export_data("test_createtx_valid_load.xlsx", time_distribution)


"""                       ***  UNIT TESTS ***

        - Here we test combinations of valid and invalid data.
        - Time is not a consideration here.

"""

class create_Tx_Test(unittest.TestCase):
    # Generate new data before each run
    def setUp(self):
       # Valid data
       self.valid_txid = xbridge_utils.generate_random_valid_txid()
       self.valid_src_Token = xbridge_utils.generate_random_valid_token()
       self.valid_dest_Token = xbridge_utils.generate_random_valid_token()
       self.valid_src_Address = xbridge_utils.generate_random_valid_address()
       self.valid_dest_Address = xbridge_utils.generate_random_valid_address()
       self.valid_positive_nb_1 = xbridge_utils.generate_random_number(1, 10000)
       self.valid_positive_nb_2 = xbridge_utils.generate_random_number(1, 10000)
       # Invalid data
       self.invalid_neg_nb = xbridge_utils.generate_random_number(-99999999999999999999999999999999999999999999999, -0.0000000000000000000000000000000000000000000000000001)
       self.invalid_sm_positive_nb = 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
       self.invalid_lg_positive_nb = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
       self.invalid_src_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_dest_Address = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 5000))
       self.invalid_src_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.invalid_dest_Token = xbridge_utils.generate_garbage_input(xbridge_utils.generate_random_number(1, 500))
       self.nb_with_leading_zeros_1 = xbridge_utils.generate_random_number_with_leading_zeros()
       self.nb_with_leading_zeros_2 = xbridge_utils.generate_random_number_with_leading_zeros()

    # Various numerical parameter combinations
    def test_invalid_create_tx_v1(self):
        # negative_number + positive_number, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.valid_dest_Address, self.valid_dest_Token, self.valid_positive_nb_2))
        # positive_number + negative_number, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb))
        # negative_number + negative_number, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb))
        # 0 + negative_number, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, 0, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb))
        # positive_number + 0, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, 0))
        # 0 + 0, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, 0, self.valid_dest_Address, self.valid_dest_Token, 0))

    # Combinations with empty addresses
    def test_invalid_create_tx_v2(self):
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(" ", self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, "SYS", self.valid_positive_nb_2))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.valid_positive_nb_1, " ", "SYS", self.valid_positive_nb_2))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(" ", self.valid_src_Token, self.valid_positive_nb_1, " ", "SYS", self.valid_positive_nb_2))

    def test_invalid_create_tx_v3(self):
        # Same source and destination Addresses, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_src_Address, self.valid_dest_Token, self.valid_positive_nb_2))
        # Same source and destination Tokens, different addresses, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_src_Token, self.valid_positive_nb_2))
        # Same source and destination Addresses and Tokens, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_2))

    # Combinations of address parameters containing quotes
    def test_invalid_create_tx_v4(self):
        # Address 1 contains quotes, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_src_Token, self.valid_positive_nb_1, "12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey", self.valid_dest_Token, self.valid_positive_nb_2))
        # Address 2 contains quotes, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.valid_positive_nb_1, "'12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey'", self.valid_dest_Token, self.valid_positive_nb_2))
        # Both Addresses contain quotes, all other parameters being valid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", self.valid_src_Token, self.valid_positive_nb_1, "'12BueeBVD2uiAHViXf7jPVQb2MSQ1Eggey'", self.valid_dest_Token, self.valid_positive_nb_2))

    # Combinations of quotes + out-of-bounds quantities
    def test_invalid_create_tx_v5(self):
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", "LTC", self.invalid_neg_nb, "'LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy'", "LTC", self.invalid_neg_nb))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.valid_positive_nb_1, "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", "LTC", self.invalid_neg_nb))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX("LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", self.valid_src_Token, self.invalid_neg_nb, "LTnoVFAnKSMj4v2eFXBJuMmyjqSQT9eXBy", "LTC", self.valid_positive_nb_1))

    # Combinations of multiple invalid parameters leading up to ALL parameters being invalid
    def test_invalid_create_tx_v6(self):
        # Only source Address is valid, the rest is invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.invalid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb))
        # Only source Address + source Token are valid, the rest is invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb))
        # Only source Address + source Token + source_Quantity are valid, the rest is invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb))
        # Only (source + dest) Addresses + source Token + source_Quantity are valid, the rest is invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb))
        # Only (source + dest) Addresses + (source + dest)  Tokens + source_Quantity are valid, the rest is invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.invalid_neg_nb))
        # All parameters are invalid
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.invalid_src_Address, self.invalid_src_Token, self.invalid_neg_nb, self.invalid_dest_Address, self.invalid_dest_Token, self.invalid_neg_nb))

    # Combinations of numerical parameters containining leading Zeros, all other parameters being valid
    def test_invalid_create_tx_v7(self):
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.nb_with_leading_zeros_1, self.valid_dest_Address, self.valid_dest_Token, self.valid_positive_nb_2))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.valid_positive_nb_1, self.valid_dest_Address, self.valid_dest_Token, self.nb_with_leading_zeros_1))
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.nb_with_leading_zeros_1, self.valid_dest_Address, self.valid_dest_Token, self.nb_with_leading_zeros_2))

    # Combinations of very small and very large numerical parameters, all other parameters being valid
    def test_invalid_create_tx_v8(self):
        # very small + very small
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb))
        # very small + very large
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_sm_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb))
        # very large + very small
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_sm_positive_nb))
        # very large + very large
        self.assertIsNone(xbridge_client.CHECK_CREATE_TX(self.valid_src_Address, self.valid_src_Token, self.invalid_lg_positive_nb, self.valid_dest_Address, self.valid_dest_Token, self.invalid_lg_positive_nb))


def repeat_create_tx_unit_tests(nb_of_runs):
    for i in (1, nb_of_runs):
        wasSuccessful = unittest.main(exit=False).result.wasSuccessful()
        if not wasSuccessful:
            sys.exit(1)

# unittest.main()
