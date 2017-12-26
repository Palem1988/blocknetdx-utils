import os, logging, errno, time
import xbridge_config

from utils import xbridge_utils

os.chdir(os.path.dirname(__file__))
program_dir = os.getcwd()

# LOG_DIR = program_dir + "\\logs\\"
LOG_DIR = program_dir + os.sep + "logs"

max_Char_Length = xbridge_config.get_param_max_char_length_to_display()

try:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
except OSError as e:
    if e.errno != errno.EEXIST:
        LOG_DIR = ""
        raise

log_time_str = time.strftime("%Y%m%d-%H%M%S")
# log_file_name_str = xbridge_config.get_conf_log_dir() + log_time_str + "_testing_log.txt"
log_file_name_str = LOG_DIR + os.sep + log_time_str + "_testing_log.txt"
print("log files will be logged there: %s" % log_file_name_str)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(log_file_name_str)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 0 = SUCCESS, 1 = FAILURE, 2 = ERROR
def XLOG(func_name, type_int, err_descr=None, lst_of_params=None):
    if not isinstance(type_int, int):
        return
    if type_int == 0:
        log_json = {"group": str(func_name), "success": 1, "failure": 0, "error": 0}
        xbridge_utils.ERROR_LOG.append(log_json)
        return
    if type_int == 1:
        log_json = {"group": str(func_name), "success": 0, "failure": 1, "error": 0}
        logger.info('\n%s FAILED: %s' % (str(func_name), str(err_descr)))
    if type_int == 2:
        log_json = {"group": str(func_name), "success": 0, "failure": 0, "error": 1}
        logger.info('\n%s ERROR: %s' % (str(func_name), str(err_descr)))
    xbridge_utils.ERROR_LOG.append(log_json)
    if lst_of_params is None:
        return
    if max_Char_Length < 1:
        return
    if isinstance(lst_of_params, list):
        if len(lst_of_params) == 0:
            return
        for var_to_log in lst_of_params:
            try:
                logger.info('param: [%s]' % str(var_to_log)[:max_Char_Length])
            except UnicodeEncodeError as err:
                logger.info('param: [%s]' % str(var_to_log))
            except UnicodeDecodeError as err:
                logger.info('param: [%s]' % str(var_to_log))
