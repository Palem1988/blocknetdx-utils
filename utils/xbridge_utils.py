import time
import random
from strgen import StringGenerator
import pandas as pd
from pandas import ExcelWriter



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
    # Set for create_tx
    c_src_Address = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    c_dest_Address = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    c_src_Token = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    c_dest_Token = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    source_nb = generate_random_number(-999999999999999999999999999999999999999999999999999999999999999,
                                                     999999999999999999999999999999999999999999999999999999999999999)
    dest_nb = generate_random_number(-999999999999999999999999999999999999999999999999999999999999999,
                                                   999999999999999999999999999999999999999999999999999999999999999)
    # set for accept_tx
    a_random_tx_id = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    a_src_Address = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    a_dest_Address = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))
    ca_random_tx_id = generate_input_from_random_classes_combinations(generate_random_number(0, 12000))



def export_data(filepath, list_to_export):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filepath_with_time = timestr + "_" + filepath
    my_df = pd.DataFrame(list_to_export)
    stat_df = my_df["time"].describe()
    writer = ExcelWriter(filepath_with_time)
    my_df.to_excel(writer, 'RawData')
    stat_df.to_excel(writer, 'Summary')
    writer.save()
    print("created: %s" % filepath_with_time)


def generate_random_number(a, b):
    a = int(a * 100)
    b = int(b * 100)
    return float(random.randint(a, b)/100)


def generate_random_valid_address():
    template_str = '[\h]{30:70}'
    return StringGenerator(template_str).render()

    
def generate_random_valid_txid():
    nb_of_cars = 64
    template_str = '[a-zA-Z0-9]{' + str(nb_of_cars) + '}'
    return StringGenerator(template_str).render()
    
    
def generate_random_valid_token():
    nb_of_cars = 5
    template_str = '[A-Z]{' + str(nb_of_cars) + '}'
    return StringGenerator(template_str).render()    

    
def generate_random_number_with_leading_zeros():
    template_str = '[0]{1:5000}&[\d]{1:5000}'
    return StringGenerator(template_str).render()    


def generate_input_from_random_classes_combinations(lower_bound, upper_bound):
    classes_list = ["\w", "\d", "\s", "\W", "\p", "\o", "\a"]
    # Sometimes, the picks will be of the same class, so combinations are from 1 to 7 combinations
    pick_1 = random.choice(classes_list)
    pick_2 = random.choice(classes_list)
    pick_3 = random.choice(classes_list)
    pick_4 = random.choice(classes_list)
    combined_picks = pick_1 + pick_2 + pick_3 + pick_4
    template_str = '[' + str(combined_picks) + ']{' + str(lower_bound) + ':' + str(upper_bound) + '}'
    return StringGenerator(template_str).render()

    
# Generate variable-size malformed data with whitespace + punctuation + digits
def generate_garbage_input(nb_of_cars):
    nb_of_cars = int(nb_of_cars)
    # return StringGenerator('[\w\d\W]{8}').render()
    template_str = '[\w\d\W]{' + str(nb_of_cars) + '}'
    return StringGenerator(template_str).render()

    
def generate_numeric_input(nb_of_digits):
    nb_of_digits = int(nb_of_digits)
    # return StringGenerator('[\w\d\W]{8}').render()
    template_str = '[\d]{' + str(nb_of_digits) + '}'
    return StringGenerator(template_str).render()
