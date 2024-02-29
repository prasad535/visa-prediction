# import os
# from visa.constants import MONGODB_URL_KEY, DATABASE_NAME, COLLECTION_NAME
# from visa.data_access.usvisa_data import USvisaData
# from visa.logger import logging
# from visa.exception import VisaException


# # obj = MongoDBClient(database_name=DATABASE_NAME)
# # print(obj)
# # print(obj.client)
# # export MONGODB_URL="mongodb+srv://prasad535:sample535@cluster0.z6sv9yb.mongodb.net/?retryWrites=true&w=majority"

# obj = USvisaData()

# df = obj.export_collection_as_dataframe(collection_name=COLLECTION_NAME)
# logging.info(df)

"""
MongoDB connection demo
"""
# from visa.configuration.mongo_db_connection import MongoDBClient


# obj = MongoDBClient()

"""
usvisa_data : Export collection records as dataframe
"""
import os
import sys
from visa.logger import logging
from visa.exception import VisaException
# from visa.data_access.usvisa_data import USvisaData
# from visa.constants import COLLECTION_NAME
# try:
#     obj = USvisaData()
#     obj.export_collection_as_dataframe(collection_name = COLLECTION_NAME)
# except Exception as e:
#     raise VisaException(e,sys)

"""
1. update constants
2. update config_entity.py
3. update artifact_entity.py
4. update component_name.py
5. update training_pipeline.py
5. test demo.py
"""

from visa.pipline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()