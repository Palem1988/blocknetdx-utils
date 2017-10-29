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

```

# Testing model

- The code uses randomness to generate various groups of data and scenarios and mix them together (valid, invalid, out-of-bounds data).
So the longer the tests are run, the better.

- It is therefore **strongly** advised to run these tests continuously for days to let the program generate a very high number of combinations of scenarios.

- It would also be advisable to run them on a periodic basis. Because the newly run tests will *always* be different from the previous ones (due to the randomness nature).

- Randomness is used for the following variables:
  - call order in the sequence.
  - size of parameters sent to the API.
  - content type.
  - valid / invalid nature of parameter.



# TODO

- Add test case where Token and Address are not consistent.

