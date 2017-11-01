import configparser
import os

config = configparser.ConfigParser()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
conf_file_path = os.path.join(__location__, 'tests.conf')

config.read(conf_file_path)

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

def get_conf_sequence_run_number():
    try:
        if not conf_exists():
            return 1
        if "DEFAULT_NUMBER_OF_RUNS" in config.sections():
            return config.getint('DEFAULT_NUMBER_OF_RUNS', 'SEQUENCE_TESTS_NB_OF_RUNS')
        else:
            return 1
    except KeyError:
            return 1

def get_conf_unit_tests_run_number():
    try:
        if not conf_exists():
            return 1
        if "DEFAULT_NUMBER_OF_RUNS" in config.sections():
            return config.getint('DEFAULT_NUMBER_OF_RUNS', 'UNIT_TESTS_NB_OF_RUNS')
        else:
            return 1
    except KeyError:
            return 1



