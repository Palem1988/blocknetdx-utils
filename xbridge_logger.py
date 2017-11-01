import os, logging, errno, time

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
log_file_name_str = LOG_DIR + log_time_str + "_testing_log.txt"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file_name_str)
# formatter = logging.Formatter('%(asctime)s - %(message)s')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
