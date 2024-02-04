import logging
import os
from datetime import datetime
from pathlib import Path
from from_root import from_root


ROOT_DIR = Path(__file__).parent.parent 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"
log_paths= os.path.join(from_root(),"logs")

os.makedirs(log_paths,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_paths,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(name)s - %(levelname)s - %(module)s - %(message)s",
    level=logging.DEBUG
)