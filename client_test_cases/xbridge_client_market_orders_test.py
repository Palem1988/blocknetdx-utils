import time
import random
from utils import xbridge_utils
from interface import xbridge_client


"""
    - UNORDERED + ORDERED SEQUENCE OF MARKET ACTIONS
    - CANCELTX + ACCEPT_TX + CREATE_TX
"""

c_src_Address = ""
c_dest_Address = ""
c_src_Token = ""
c_dest_Token = ""
source_nb = ""
dest_nb = ""
a_random_tx_id = ""
a_src_Address = ""
a_dest_Address = ""
ca_random_tx_id = ""


def generate_new_set_of_data():
    c_src_Address = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    c_dest_Address = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    c_src_Token = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    c_dest_Token = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    source_nb = xbridge_utils.generate_random_number(-999999999999999999999999999999999999999999999999999999999999999,
                                                     999999999999999999999999999999999999999999999999999999999999999)
    dest_nb = xbridge_utils.generate_random_number(-999999999999999999999999999999999999999999999999999999999999999,
                                                   999999999999999999999999999999999999999999999999999999999999999)
    a_random_tx_id = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    a_src_Address = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    a_dest_Address = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))
    ca_random_tx_id = xbridge_utils.generate_input_from_random_classes_combinations(
        xbridge_utils.generate_random_number(0, 12000))



"""
    - UNORDERED SEQUENCE OF MARKET ACTIONS
    - CANCELTX + ACCEPT_TX + CREATE_TX
"""

def random_seq_market_actions_api_calls(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        generate_new_set_of_data()
        func_list = [xbridge_client.CHECK_CREATE_TX, xbridge_client.CHECK_ACCEPT_TX,
                                 xbridge_client.CHECK_CANCEL_TX]
        selected_func = random.choice(func_list)
        func_str = ""
        ts = time.time()
        if selected_func == xbridge_client.CHECK_CREATE_TX:
            xbridge_client.CHECK_CREATE_TX(c_src_Address, c_src_Token, source_nb, c_dest_Address, c_dest_Token, dest_nb)
            func_str = "CHECK_CREATE_TX"
        if selected_func == xbridge_client.CHECK_ACCEPT_TX:
            xbridge_client.CHECK_ACCEPT_TX(a_random_tx_id, a_src_Address, a_dest_Address)
            func_str = "CHECK_ACCEPT_TX"
        if selected_func == xbridge_client.CHECK_CANCEL_TX:
            xbridge_client.CHECK_CANCEL_TX(ca_random_tx_id)
            func_str = "CHECK_CANCEL_TX"
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": func_str}
        time_distribution.append(json_str)
    xbridge_utils.export_data("random_seq_market_actions_api_calls.xlsx", time_distribution)


"""
    - ORDERED SEQUENCE OF MARKET ACTIONS
    - CANCELTX + ACCEPT_TX + CREATE_TX
"""

def defined_seq_market_actions_api_calls(nb_of_runs):
    time_distribution = []
    total_elapsed_seconds = 0
    for i in range(1, nb_of_runs):
        generate_new_set_of_data()
        func_str = ""
        ts = time.time()
        if i % 3 == 0:
            xbridge_client.CHECK_CREATE_TX(c_src_Address, c_src_Token, source_nb, c_dest_Address, c_dest_Token, dest_nb)
            func_str = "CHECK_CREATE_TX"
        if i % 3 == 1:
            xbridge_client.CHECK_ACCEPT_TX(a_random_tx_id, a_src_Address, a_dest_Address)
            func_str = "CHECK_ACCEPT_TX"
        if i % 3 == 2:
            xbridge_client.CHECK_CANCEL_TX(ca_random_tx_id)
            func_str = "CHECK_CANCEL_TX"
        te = time.time()
        total_elapsed_seconds += te - ts
        json_str = {"time": te - ts, "API": func_str}
        time_distribution.append(json_str)
    xbridge_utils.export_data("defined_seq_market_actions_api_calls.xlsx", time_distribution)

