import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_paths= os.path.join(from_root,"logs",LOG_FILE)

os.makedirs(log_paths,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_paths,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(name)s - %(levelname)s - %(module)s - %(message)s",
    level=logging.DEBUG
)