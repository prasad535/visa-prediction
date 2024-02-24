import logging
import os

from from_root import from_root
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR = 'logs'

LOG_FILE_PATH = os.path.join(from_root(), LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] -  %(levelname)s - %(message)s"
)

