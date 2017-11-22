import configparser
import os

config = configparser.ConfigParser()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
conf_file_path = os.path.join(__location__, 'tests.conf')

config.read(conf_file_path)

MAX_CHAR_LENGTH_TO_DISPLAY = 20000

def conf_exists():
    if not os.path.exists(conf_file_path):
        return False
    else:
        return True

def get_conf_log_dir():
    try:
        if not conf_exists():
            return ""
        if "OUTPUT" in config.sections():
            return config['OUTPUT']['LOG_DIR']
        else:
            return ""
    except KeyError:
        return ""
    except configparser.NoOptionError:
        return ""

def get_conf_login():
    try:
        if not conf_exists():
            return ""
        if "CONNECTION" in config.sections():
            return config['CONNECTION']['LOGIN']
        else:
            return ""
    except KeyError:
        return ""
    except configparser.NoOptionError:
        return ""

def get_conf_password():
    try:
        if not conf_exists():
            return ""
        if "CONNECTION" in config.sections():
            return config['CONNECTION']['PASSWORD']
        else:
            return ""
    except KeyError:
            return ""

def get_conf_IP():
    try:
        if not conf_exists():
            return ""
        if "CONNECTION" in config.sections():
            return config['CONNECTION']['IP']
        else:
            return ""
    except KeyError:
        return ""
    except configparser.NoOptionError:
        return ""

def should_log_Excel_files():
    try:
        if not conf_exists():
            return True
        if "OUTPUT" in config.sections():
            return config["OUTPUT"].getboolean('LOG_EXCEL_FILES')
        else:
            return True
    except KeyError:
        return True
    except configparser.NoOptionError:
        return True

def get_conf_sequence_run_number():
    try:
        if not conf_exists():
            return 0
        if "DEFAULT_NUMBER_OF_RUNS" in config.sections():
            return config.getint('DEFAULT_NUMBER_OF_RUNS', 'SEQUENCE_TESTS_NB_OF_RUNS')
        else:
            return 0
    except KeyError:
            return 0

def get_conf_unit_tests_run_number():
    if not conf_exists():
        return 0
    if "DEFAULT_NUMBER_OF_RUNS" in config.sections():
        try:
            return config.getint('DEFAULT_NUMBER_OF_RUNS', 'UNIT_TESTS_NB_OF_RUNS')
        except configparser.NoOptionError:
            return 0
        except KeyError:
            return 0
    else:
        return 0

def get_conf_subtests_run_number():
    if not conf_exists():
        return 10
    if "DEFAULT_NUMBER_OF_RUNS" in config.sections():
        try:
            return config.getint('DEFAULT_NUMBER_OF_RUNS', 'SUB_TESTS_NB_OF_RUNS')
        except KeyError:
            return 10
        except configparser.NoOptionError:
            return 10
    else:
        return 10

def should_run_extended_tests():
    try:
        if not conf_exists():
            return False
        if "BEHAVIOR" in config.sections():
            return config["BEHAVIOR"].getboolean('run_extended_tests')
        else:
            return False
    except KeyError:
        return False
    except configparser.NoOptionError:
        return False

def get_wallet_decryption_passphrase():
    try:
        if not conf_exists():
            return "mypwd"
        if "WALLET" in config.sections():
            return config['WALLET']['wallet_decryption_passphrase']
        else:
            return "mypwd"
    except KeyError:
            return "mypwd"

def get_param_max_char_length_to_display():
    if not conf_exists():
        return 20000
    if "OUTPUT" in config.sections():
        try:
            return config.getint('OUTPUT', 'MAX_CHAR_LENGTH_TO_DISPLAY')
        except configparser.NoOptionError:
            return 20000
        except KeyError:
            return 20000
    else:
        return 20000