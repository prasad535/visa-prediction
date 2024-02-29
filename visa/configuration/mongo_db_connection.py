import os
import sys

from visa.logger import logging
from visa.exception import VisaException

from visa.constants import DATABASE_NAME, MONGODB_URL_KEY

import pymongo
import certifi

from dotenv import load_dotenv
load_dotenv()

ca = certifi.where()

class MongoDBClient:
    """
    Class Name  : export_data_into_feature
    Description : This method exports the dataframe from mongodb feature store as dataframe

    Output  : connection to mongodb database
    Onfailure   : Raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if mongodb_url is None:
                    logging.info(f"Environment Key: {MONGODB_URL_KEY} is not set.")
                    raise Exception(f"Environment Key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongodb_url, tlsCAFile=ca)
                logging.info(f"mongoDB Connection client established: {MongoDBClient.client}")
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"client : {self.client}")
            logging.info(f"database : {self.database}")
            logging.info(f"database name : {self.database_name}")

        except Exception as e:
            logging.info(VisaException(e, sys))
            raise VisaException(e, sys)