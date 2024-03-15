from visa.cloud_storage.aws_storage import SimpleStorageService
from visa.entity.estimator import USvisaModel
from visa.exception import VisaException
from visa.logger import logging

import sys
from pandas import DataFrame 


class USvisaEstimator:


    def __init__(self, bucket_name, model_path):

        self.bucket_name = bucket_name
        self.model_path = model_path
        self.s3 = SimpleStorageService()
        self.loaded_model: USvisaModel = None

    def is_model_present(self, model_path) -> USvisaModel:
        try:
            return self.s3.s3_key_path_available(bucket_name = self.bucket_name, s3_key = model_path)
        except Exception as e:
            raise VisaException(e, sys)

    def load_model(self, ) -> USvisaModel:

        return self.s3.load_model(model_name=self.model_path, bucket_name=self.bucket_name)

    def save_model(self, from_file, remove:bool = False) -> None:

        try:
            self.s3.upload_file(from_file,
                                to_filename = self.model_path, 
                                bucket_name = self.bucket_name)
        except Exception as e:
            raise VisaException(e, sys)


    def predict(self, dataframe:DataFrame):

        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise VisaException(e, sys)