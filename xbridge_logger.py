import os, logging, errno, time
import xbridge_config

os.chdir(os.path.dirname(__file__))
program_dir = os.getcwd()

LOG_DIR = program_dir + "\\test_outputs\\"

try:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
except OSError as e:
    if e.errno != errno.EEXIST:
        LOG_DIR = ""
        raise

log_time_str = time.strftime("%Y%m%d-%H%M%S")
log_file_name_str = xbridge_config.get_conf_log_dir() + log_time_str + "_testing_log.txt"
print("log files will be logged there: %s" % log_file_name_str)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file_name_str)
# formatter = logging.Formatter('%(asctime)s - %(message)s')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
