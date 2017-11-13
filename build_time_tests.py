import unittest
import argparse

from utils import xbridge_utils
from utils import xbridge_ref
from interface import xbridge_rpc
import xbridge_logger
import xbridge_config

from rpc_test_cases import xbridge_rpc_sequence_new_test

"""
from test_cases import xbridge_client_get_tx_info_test
from test_cases import xbridge_client_accept_tx_test
from test_cases import xbridge_client_canceltx_test
from test_cases import xbridge_client_createtx_test
from test_cases import xbridge_client_sequence_test
"""

"""            
        *****************************************************************************************
        ******************************  SPECIFY THE OPTIONS HERE    *****************************
        *****************************************************************************************
"""

NUMBER_OF_WANTED_RUNS = 0
UNIT_TESTS_NB_OF_RUNS = 0

NUMBER_OF_WANTED_RUNS = xbridge_config.get_conf_sequence_run_number()
UNIT_TESTS_NB_OF_RUNS = xbridge_config.get_conf_unit_tests_run_number()

parser = argparse.ArgumentParser(description='API testing')
parser.add_argument('-s','--sequence', type=int, help='Number of sequence tests run')
parser.add_argument('-u','--unittest', type=int, help='Number of unit tests to run')

args = parser.parse_args()

if args.sequence is not None:
    NUMBER_OF_WANTED_RUNS = args.sequence

if args.unittest is not None:
    UNIT_TESTS_NB_OF_RUNS = args.unittest

"""            
        *****************************************************************************************
        ******************  SPECIFY HERE THE LIST RPC SEQUENCE TESTS TO RUN    ******************
        *****************************************************************************************
"""

xbridge_rpc_sequence_new_test.run_sequence(NUMBER_OF_WANTED_RUNS)

if NUMBER_OF_WANTED_RUNS > 0:
    xbridge_logger.logger.info('')
    print("******** Sequence tests are done ********")
    xbridge_utils.export_Full_Excel_Log()
    print("*****************************************")


"""            
        *****************************************************************************************
        ********************  SPECIFY HERE THE LIST RPC UNITS TESTS TO RUN    *******************
        *****************************************************************************************
"""

if UNIT_TESTS_NB_OF_RUNS < 1:
    print("No unit tests to run")
    exit(0)

xbridge_logger.logger.info('')
xbridge_logger.logger.info('Starting unit tests with version %s \n', str(xbridge_rpc.get_core_version()))

suites = [unittest.TestLoader().loadTestsFromModule(modul) for modul in xbridge_ref.unit_tests_module_strings]
test_suite = unittest.TestSuite(suites)

for i in range(1, 1 + UNIT_TESTS_NB_OF_RUNS):
    suites = [unittest.TestLoader().loadTestsFromModule(modul) for modul in xbridge_ref.unit_tests_module_strings]
    test_suite = unittest.TestSuite(suites)
    # print("%s test cases found" % test_suite.countTestCases())
    for test in test_suite:
        print(test._tests)
    testResult = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
summary_df = xbridge_utils.prepare_results_Summary()
filtered_df = summary_df[ (summary_df["failure"] > 0) | (summary_df["error"] > 0) ]

xbridge_logger.logger.info('\n ********************* SUMMARY *********************\n')
xbridge_logger.logger.info("Successes: %s" % str(summary_df["success"].sum()))
xbridge_logger.logger.info("Failures: %s" % str(summary_df["failure"].sum()))
xbridge_logger.logger.info("Errors: %s" % str(summary_df["error"].sum()))
if not filtered_df.empty:
    xbridge_logger.logger.info("\n %s" % str(filtered_df))

xbridge_logger.logger.info('\n Unit tests are done !')

# xbridge_logger.logger.info('----------------------------------------------------------------------------------------------------------------------------------------------------------')
# xbridge_logger.logger.info('wasSuccessful: %s - testRuns: %s - Failures: %s - Errors: %s' % (str(testResult.wasSuccessful), str(testResult.testsRun), str(testResult.failures), str(testResult.errors)))
