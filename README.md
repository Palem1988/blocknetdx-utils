## BlocknetDX Utils Recent Changelog

-	Expanded coverage and improved existing test groups.
-	Improved logging: a) increased verbosity.  b) summary, when applicable, of failure and error counts (at the end of log file).
- Higher entropy through parameter order and type randomnization.
Note ! Many unit tests now each generate a lot of subtests to shuffle out-of-bounds or garbage around the parameters ; therefore, the number of
atomic tests will increase exponentially as you increase the number of unit tests you will run.
- Revamped sequenced tests: better scaling by now leveraging directly the unit tests.
- Code cleanings.

- Important Note ! The console will wrongly report assertion failures. You can safely ignore these. Only the log file will report the real assertions failures. This is due to exception chaining.


# Current known issues

- Popups will appear when using the client.

# TODO

- Add unit tests with valid data present in the dex once it's loaded.
- Add test case where Token and Address are not consistent.
- Running tests and analyzing results.
- When the code of the RPC calls are settled, apply the same structure for the client.
- Documentation.

# Running the tests

Wallet needs to be encrypted and unlocked.

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

[DEFAULT_NUMBER_OF_RUNS]
SEQUENCE_TESTS_NB_OF_RUNS = 1
UNIT_TESTS_NB_OF_RUNS = 1
```

# Optional command-Line options for build-time automation

All arguments are optional.- Use *-s* or *--sequence* argument to specify the number of sequence tests to run.- Use *-u* or *--unittest* argument to specify the number of unit tests to run.You can avoid using these parameters if you set the **tests.conf** file properly.

# Requirements

- This code won't run on Python < 3.4 because of the use of subtests and exception chaining.

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

# Program outputs

- Unit tests will log data and tell if each test was successful (and the number of runs) and an assertion error was thrown (with the input parameter that was used to make the call).
- Sequence tests generate an Excel file with the timing distribution.



