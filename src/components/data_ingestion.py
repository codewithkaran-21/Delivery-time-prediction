from src.constants import *
from src.config.configuration import *
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os , sys
from dataclasses import dataclass
from src.components.data_transformation import DataTransformationConfig , DataTransformation


@dataclass
class DataIngestionConfig:
    train_data_path : str = TRAIN_FILE_PATH
    test_data_path  : str = TEST_FILE_PATH
    raw_data_path : str = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingest started")
            df = pd.read_csv(DATASET_PATH)
            logging.info(f"Data read from the path : {DATASET_PATH} sucessfully")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path))

            df.to_csv(self.data_ingestion_config.raw_data_path , index= False)
            logging.info(f"Data saved to path : {RAW_FILE_PATH}")
            logging.info(f"Train test split started")
            train_set , test_set = train_test_split(df , test_size=0.20 , random_state=42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            
            train_set.to_csv(self.data_ingestion_config.train_data_path , header = True)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)

            test_set.to_csv(self.data_ingestion_config.test_data_path , header = True)
            logging.info(f"Data ingestion completed sucessfully")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr , test_arr , preprocessor_obj = data_transformation.initiate_data_transformation(train_data , test_data)
