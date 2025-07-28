import logging
import datetime
from environment import *

# Configure basic logging
if log_level == "DEBUG":
    log_level = logging.DEBUG
if log_level == "INFO":
    log_level = logging.INFO
if log_level == "ERR":
    log_level = logging.ERROR

file_name = ""
current_log_dir = ""
logger = None


def set_file_name(t_filename):
    global file_name
    global current_log_dir

    current_time = datetime.datetime.now()
    time_stamp = current_time.strftime("%Y-%m-%d-%H-%M-%S")
    dir_name = t_filename + "_" + time_stamp
    current_log_dir = automation_log_dir + "/" + dir_name + "/"
    os.mkdir(current_log_dir)
    file_name = current_log_dir + "automation.log"

def set_my_logger(testcase):
    set_file_name(testcase)
    global logger
    global file_name
    logger = logging.getLogger(testcase)
    file_handler = logging.FileHandler(file_name)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s <%(filename)s: %(funcName)s>  %(message)s"))
    logger.addHandler(file_handler)

logging.basicConfig(
    level=log_level,
    format='%(asctime)s %(levelname)s <%(filename)s: %(funcName)s>  %(message)s',
    filename= file_name,
    filemode= "w"
)


