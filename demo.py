from visa.logger import logging
from visa.exception import VisaException
import sys
logging.info(f"this is custom log")


try:
    a = 1/ 'a'
except Exception as e:
    logging.info(VisaException(e, sys))
    raise VisaException(e, sys)