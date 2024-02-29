import os
import sys

from visa.logger import logging
from visa.exception import VisaException

from visa.configuration.mongo_db_connection import MongoDBClient
from visa.constants import DATABASE_NAME, COLLECTION_NAME
from typing import Optional
import pandas as pd
import numpy as np

class USvisaData:
    """
    Description : This class helps to export entire collection as pandas dataframe
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            logging.info(VisaException(e, sys))
            raise VisaException(e, sys)

    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            logging.info(f"collection : {collection}")

            df = pd.DataFrame(list(collection.find()))

            logging.info(f"DataFrame shape: {df.shape}")
            logging.info(f"Initial Columns List:: {df.columns}")

            if "_id" in df.columns.to_list():
                df = df.drop(columns = ["_id"], axis=1)
            logging.info(f"Columns list after removing MongoDB unique ID(_id) : {df.columns.to_list()}")

            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            logging.info(VisaException(e, sys))
            raise VisaException(e, sys)