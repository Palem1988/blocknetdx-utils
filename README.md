# bdex-utils
BlocknetDX Utils

# Usage Examples

- Optional parameters with default values are being added for some functions to make their use easy, allow for some flexibility, and place boundaries on the randomness to test for specific scenarios.

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

# In Progress

- Better code modularity.
- Code refactorings, cleaning and improvements for unit tests.
- Logging parameters when an assertion error occurs.
- Central easy-to-use test launchers.
- Completing defined sequence tests.

# TODO

- Add test case where Token and Address are not consistent.
- Running tests and analyzing results.
- Comment improvements.


# Testing model

- The code uses randomness to generate various groups of data and scenarios and mix them together (valid, invalid, out-of-bounds data).
So the longer the tests are run, the better.

- It is therefore **strongly** advised to run these tests continuously for days to let the program generate a very high number of combinations of scenarios.

- It would also be advisable to run them on a periodic basis. Because the newly run tests will *always* be different from the previous ones (due to the randomness nature).

- Randomness is used for the following variables:
  - call order in the sequence.
  - size of parameters sent to the API.
  - content type.
  Example of random strings generated:
'''
4i7E1dX^l_4HlEDYGjYaxLv3 ^H!cZ52i~i8y}B/f[3?\O\_(e1290e7%0+-!8_
|87'd7?3C^*649A4!9/{?!c#&a=(B/0"f8<4ff505/,^)8[*,"cD>a36+d_&+'!7
._}a{&_}$^1@{"#+\(	0?27_~#.0)%37[ 	 ['^a$,00*3
'''
  - valid / invalid nature of parameter.
  
# Testing groups

- Unit tests for each API.
- Single API sequences.
- Random multi API sequences.
- Ordered multi API sequences.
