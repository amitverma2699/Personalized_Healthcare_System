import logging
import os
from datetime import datetime
from pathlib import Path

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"Logs")

os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)\

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )