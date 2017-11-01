## BlocknetDX Utils Recent Changelog

- (Upcoming) Unit tests for getblockcount, servicenodelist, getbudget
- If for any reason, there's a problem with the tests.conf file, the default values of the number of tests to run is now set to 0. Default values for the absence of optional parameters on the command line is also set to 0.
- Code fixes in dxGetTransactionInfo
- Fixed wrong log string in createTx.
- Added support for a configuration file for easier deployment.


# Running the tests

1. Update the tests.conf file with your credential parameters, and adjust the options to control some
behaviors of the program.

    - If some required parameters are not filled, the program will stop.
    - Also set the number of runs you want launch by default, when command line parameters are not provided.
    - Make sure the **tests.conf** file is in the same directory as the main program.

2. Run the python with or without the optional parameters.

    - If you don't specify the optional parameters, those in the **tests.conf** file will be used.
    - If you specify them, they have priority over the ones in the **tests.conf** file.

```
python build_time_tests.py
python build_time_tests.py --unittest=100 --sequence=200
```

3. Check the logs (log and Excel files) to analyze results.
Do not rely on your console for that. The console will only display what the program is currently doing, not the results.


## Remarks !

- By default, the sequence tests will output a lot of Excel files, with the timing information.
You can turn that off, by specifying **LOG_EXCEL_FILES = no** in the **tests.conf** file.
- If you want for example run only unittests, just put **--unittest=100 --sequence=0**.
or set them accordingly in the **tests.conf** file.


# Tests.conf file

```
[CONNECTION]
IP = 127.0.0.1:41414
LOGIN = Your_login
PASSWORD = Your_password

[OUTPUT]
LOG_DIR = C:\Users\...\Blocknet_unit_tests\test_outputs\
LOG_EXCEL_FILES = yes

[DEFAULT_NUMBER_OF_RUNS]
SEQUENCE_TESTS_NB_OF_RUNS = 1
UNIT_TESTS_NB_OF_RUNS = 1
```


# Optional command-Line options for build-time automation

All arguments are optional.
- Use *-s* or *--sequence* argument to specify the number of sequence tests to run.
- Use *-u* or *--unittest* argument to specify the number of unit tests to run.

You can avoid using these parameters if you set the **tests.conf** file properly.

# Current known issues

- dxCreateTx test group 8 failed assertions without known reason for now.

# Current focus

- Completing defined sequence tests.

# TODO

- Add unit tests with valid data present in the dex once it's loaded.
- Add test case where Token and Address are not consistent.
- Running tests and analyzing results.
- Add more APIs once they are available.

# Requirements

- This code won't run on Python < 3.4 because of the use of subtests.

# Sequence Tests Usage Examples

- Optional parameters are available for sequence test functions to make their use easy, allow for some flexibility, and place boundaries on the randomness to test for specific scenarios.

For example, the following calls do the same thing: 
```python
random_RPC_sequence()
random_RPC_sequence(nb_of_runs=1000)
random_RPC_sequence(nb_of_runs=1000, data_nature=RANDOM_VALID_INVALID, char_min_size=1, char_max_size=12000)
```

- To generate only valid data, set **data_nature=VALID_DATA**. 
- To generate only garbage data, set **data_nature=INVALID_DATA**.

If **data_nature=INVALID_DATA**, *char_min_size* and *char_min_size* define how long the string will be supplied by the random generator.

The following combinations may be used during the testing phase, because they generate very different test cases:
```python
random_RPC_sequence(nb_of_runs=50000, data_nature=INVALID_DATA, char_min_size=10000, char_max_size=12000)
random_RPC_sequence(nb_of_runs=50000, data_nature=VALID_DATA)
# This will generate both valid and invalid data, because the parameter is not specified.
random_RPC_sequence(nb_of_runs=50000, char_max_size=1000)

defined_order_RPC_sequence(nb_of_runs=30000, data_nature=INVALID_DATA, char_min_size=5000, char_max_size=12000)
defined_order_RPC_sequence(nb_of_runs=30000, data_nature=VALID_DATA)
defined_order_RPC_sequence(nb_of_runs=30000, char_max_size=10000)

dxCancel_RPC_sequence(nb_of_runs=20000, data_nature=INVALID_DATA, char_min_size=1, char_max_size=15000)
dxCancel_RPC_sequence(nb_of_runs=20000, data_nature=VALID_DATA)
dxCancel_RPC_sequence(nb_of_runs=20000, char_max_size=5000)

dxCreate_RPC_sequence(nb_of_runs=x, char_min_size=y)

dxAccept_RPC_sequence(nb_of_runs=x, data_nature=INVALID_DATA, char_max_size=y)
dxGetTransactionInfo_RPC_sequence(nb_of_runs=x, data_nature=INVALID_DATA, char_max_size=y)

```


# Unit Tests Usage Examples

- TODO

# Testing model

- The code uses randomness to generate various groups of data and scenarios and mix them together (valid, invalid, out-of-bounds data).
So the longer the tests are run, the better.

- It is therefore **strongly** advised to run these tests continuously for days to let the program generate a very high number of combinations of scenarios.

- It would also be advisable to run them on a periodic basis. Because the newly run tests will *always* be different from the previous ones (due to the randomness nature).

- Randomness is used for the following variables:
  - call order in the sequence.
  - size of parameters sent to the API.
  - content type (hexadecimal, numeric, alpha-numeric, garbage data, or a mix of them).
  - valid / invalid nature of parameter.
 
  
# Testing groups

- Unit tests for each API.
- Single API sequences.
- Random multi API sequences.
- Ordered multi API sequences.

# Difference between Single API Sequences and Unit Tests.

It's easy to think they are similar, but they do not work the same way.
- Single API sequence tests use input parameters that are generated from random character classes.
User can set boundaries to randomness and even choose to generate valid data or a mix of valid / invalid data.
- Unit tests will test sequentially *for sure* some defined character classes and combinations of them to generate invalid random data.

In short, the source of the randomness is not the same.
Moreover, Single API sequence tests record the timing distribution for further analysis. To check for example for RPC slowing response times. There is no speed consideration in Unit Tests.

Both type of tests are therefore complementary and not really overlapping. They may occasionally overlap, but only on rare instances.

# Program outputs

- Unit tests will log data and tell if each test was successful (and the number of runs) and an assertion error was thrown (with the input parameter that was used to make the call).
- Sequence tests generate an Excel file with the timing distribution.



