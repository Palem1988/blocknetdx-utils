import time
import random
import unittest

from utils import xbridge_ref
from utils import xbridge_utils

from interface import xbridge_rpc

"""
test_suite = unittest.TestSuite()
testloader = unittest.TestLoader()
for class_name in xbridge_ref.all_UT_class_names:
    # print(test._tests)
    testnames = testloader.getTestCaseNames(class_name)
    # print(len(testnames))
    for name in testnames:
      ## suite.addTest(testcase_klass(name, param=param))
      # print(name)
      list_of_tests.append((class_name, name))
"""

def run_sequence(nb_of_runs=10):
    list_of_tests_to_run = []
    list_of_tests_to_run.extend(build_random_of_any_sequence(nb_of_runs))
    list_of_tests_to_run.extend(build_random_polling_sequence(nb_of_runs))
    list_of_tests_to_run.extend(build_random_market_orders_sequence(nb_of_runs))
    list_of_tests_to_run.extend(build_wallet_actions_sequence(nb_of_runs))
    start_custom_test_runner(list_of_tests_to_run)

def build_random_market_orders_sequence(nb_of_runs=10):
    list_of_available_tests = []
    testloader = unittest.TestLoader()
    for class_name in xbridge_ref.market_actions_UT_class_names :
        testnames = testloader.getTestCaseNames(class_name)
        # We filter out tests that are marked because they are not relevant in sequence tests.
        testnames = [x for x in testnames if "noseq" not in x]
        for name in testnames:
            list_of_available_tests.append((class_name, name))
    selected_Tests = []
    for i in range(nb_of_runs):
        selected_Test = random.choice(list_of_available_tests)
        # print(selected_Test)
        selected_Tests.append(selected_Test)
    return selected_Tests     

def build_random_polling_sequence(nb_of_runs=10):
    list_of_available_tests = []
    testloader = unittest.TestLoader()
    for class_name in xbridge_ref.polling_UT_class_names:
        testnames = testloader.getTestCaseNames(class_name)
        # We filter out tests that are marked because they are not relevant in sequence tests.
        testnames = [x for x in testnames if "noseq" not in x]
        for name in testnames:
            list_of_available_tests.append((class_name, name))
    selected_Tests = []
    for i in range(nb_of_runs):
        selected_Test = random.choice(list_of_available_tests)
        # print(selected_Test)
        selected_Tests.append(selected_Test)
    return selected_Tests

def build_wallet_actions_sequence(nb_of_runs=10):
    list_of_available_tests = []
    testloader = unittest.TestLoader()
    for class_name in xbridge_ref.wallet_actions_UT_class_names:
        testnames = testloader.getTestCaseNames(class_name)
        # We filter out tests that are marked because they are not relevant in sequence tests.
        testnames = [x for x in testnames if "noseq" not in x]
        for name in testnames:
            list_of_available_tests.append((class_name, name))
    selected_Tests = []
    for i in range(nb_of_runs):
        selected_Test = random.choice(list_of_available_tests)
        # print(selected_Test)
        selected_Tests.append(selected_Test)
    return selected_Tests
    
def build_random_of_any_sequence(nb_of_runs=10):
    list_of_available_tests = []
    testloader = unittest.TestLoader()
    for class_name in xbridge_ref.all_UT_class_names:
        testnames = testloader.getTestCaseNames(class_name)
        # We filter out tests that are marked because they are not relevant in sequence tests.
        testnames = [x for x in testnames if "noseq" not in x]
        for name in testnames:
            list_of_available_tests.append((class_name, name))
    selected_Tests = []
    for i in range(nb_of_runs):
        selected_Test = random.choice(list_of_available_tests)
        # print(selected_Test)
        selected_Tests.append(selected_Test)
    return selected_Tests

def start_custom_test_runner(list_of_tests_to_run, data_nature=3, char_min_size=1, char_max_size=12000):
    time_distribution = []
    elapsed_Time = 0
    run_count = 0
    # print("API call order will be random. Number of runs: %s" % (str(nb_of_runs)))
    print("Expected run count: %s" % (len(list_of_tests_to_run)))
    # print(str(list_of_tests_to_run))
    for selected_Test in list_of_tests_to_run:
        xbridge_utils.generate_new_set_of_data(data_nature=xbridge_utils.INVALID_DATA, char_min_size = 1, char_max_size = 12000)
        te = 0
        ts = 0
        suite = unittest.TestSuite()
        suite.addTest(selected_Test[0](selected_Test[1]))
        ts = time.time()
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        # sys.exit(not result.wasSuccessful())
        te = time.time()
        elapsed_Time = te - ts
        print("Random sequence test - %s (%s secs)" % (str(selected_Test[1]), str(elapsed_Time)))
        full_json_str = {"version": xbridge_rpc.get_core_version(), "sequence": "non-defined", "API": str(selected_Test[1]), "time": elapsed_Time}
        xbridge_utils.TIME_DISTRIBUTION.append(full_json_str)
        run_count += 1
        # json_str = {"time": elapsed_Time, "API": str(selected_Test)}
        # time_distribution.append(json_str)
    # xbridge_utils.export_data("random_RPC_calls_sequence.xlsx", time_distribution)


# run_sequence(10)
