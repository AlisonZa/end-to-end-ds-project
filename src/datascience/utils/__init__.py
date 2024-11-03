import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s ]"
                # time of the log 
                              # Level [DEBUG, INFO, WARNING, ERROR, CRITICAL]
                                            # Module of the log action
                                                        # Message     

log_dir = "logs"
log_file_path = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok= True)


logging.basicConfig(
    level= logging.INFO,
    format = logging_str,

    handlers= [
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout),
    ]
)

logger = logging.getLogger("datasciencelogger")