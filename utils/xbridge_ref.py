
from rpc_test_cases import xbridge_rpc_accept_tx_test
from rpc_test_cases import xbridge_rpc_canceltx_test
from rpc_test_cases import xbridge_rpc_get_tx_info_test
from rpc_test_cases import xbridge_rpc_createtx_test
from rpc_test_cases import xbridge_rpc_misc_test

from rpc_test_cases import xbridge_rpc_signtx_test
from rpc_test_cases import xbridge_rpc_sendtx_test

from rpc_test_cases import xbridge_rpc_blockchain_test
from rpc_test_cases import xbridge_rpc_blocknetdx_test
from rpc_test_cases import xbridge_rpc_network_test
from rpc_test_cases import xbridge_rpc_mining_test

from rpc_test_cases import xbridge_rpc_wallet_list_test
from rpc_test_cases import xbridge_rpc_wallet_set_test
from rpc_test_cases import xbridge_rpc_wallet_get_test

from rpc_test_cases import xbridge_rpc_send_test
from rpc_test_cases import xbridge_rpc_privkey_test
from rpc_test_cases import xbridge_rpc_utils_test

from rpc_test_cases import xbridge_rpc_encrypt_test
from rpc_test_cases import xbridge_rpc_decoderawtx_test

unit_tests_module_strings = [xbridge_rpc_createtx_test,
                            xbridge_rpc_canceltx_test,
                            xbridge_rpc_accept_tx_test,
                            xbridge_rpc_get_tx_info_test,
                            xbridge_rpc_blockchain_test,
                            xbridge_rpc_blocknetdx_test,
                            xbridge_rpc_network_test,
                            xbridge_rpc_wallet_list_test,
                            xbridge_rpc_wallet_get_test,
                            xbridge_rpc_wallet_set_test,
                            xbridge_rpc_mining_test,
                            xbridge_rpc_send_test,
                            xbridge_rpc_misc_test,
                            xbridge_rpc_signtx_test,
                            xbridge_rpc_sendtx_test,
                            xbridge_rpc_privkey_test,
                            xbridge_rpc_utils_test,
                            xbridge_rpc_encrypt_test,
                            xbridge_rpc_decoderawtx_test,
                            xbridge_rpc_encrypt_test
                            ]

all_UT_class_names = [xbridge_rpc_misc_test.Misc_UnitTest,
                          xbridge_rpc_accept_tx_test.accept_Tx_Test,
                          xbridge_rpc_send_test.send_UnitTest,
                          xbridge_rpc_createtx_test.create_Tx_Test,
                          xbridge_rpc_canceltx_test.cancelUnitTest,
                          xbridge_rpc_get_tx_info_test.get_Tx_Info_UnitTest,
                          xbridge_rpc_signtx_test.signUnitTest,
                          xbridge_rpc_sendtx_test.sendUnitTest,
                          xbridge_rpc_blockchain_test.Blockchain_UnitTest,
                          xbridge_rpc_blocknetdx_test.Blocknetdx_UnitTest,
                          xbridge_rpc_network_test.Network_UnitTest,
                          xbridge_rpc_wallet_list_test.wallet_List_UnitTest,
                          xbridge_rpc_wallet_get_test.wallet_get_UnitTest,
                          xbridge_rpc_wallet_set_test.wallet_Set_UnitTest,
                          xbridge_rpc_mining_test.Mining_UnitTest,
                          xbridge_rpc_utils_test.Utils_UnitTest,
                          xbridge_rpc_decoderawtx_test.decodeUnitTest,
                          xbridge_rpc_encrypt_test.Encrypt_UnitTest
                          ]

polling_UT_class_names = [xbridge_rpc_get_tx_info_test.get_Tx_Info_UnitTest,
                          xbridge_rpc_wallet_list_test.wallet_List_UnitTest,
                          xbridge_rpc_wallet_get_test.wallet_get_UnitTest
                          ]

market_actions_UT_class_names = [
    xbridge_rpc_accept_tx_test.accept_Tx_Test,
    xbridge_rpc_createtx_test.create_Tx_Test,
    xbridge_rpc_canceltx_test.cancelUnitTest
]

market_and_polling_UT_class_names = [
    xbridge_rpc_accept_tx_test.accept_Tx_Test,
    xbridge_rpc_createtx_test.create_Tx_Test,
    xbridge_rpc_canceltx_test.cancelUnitTest,
    xbridge_rpc_get_tx_info_test.get_Tx_Info_UnitTest,
]

wallet_actions_UT_class_names = [
    xbridge_rpc_wallet_list_test.wallet_List_UnitTest,
    xbridge_rpc_wallet_get_test.wallet_get_UnitTest,
    xbridge_rpc_wallet_set_test.wallet_Set_UnitTest,
]
