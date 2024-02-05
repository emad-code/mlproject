# Contains code relating to retrieving and reading the data

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# any input i require, i will give to this class
# It configures the Data Ingest component in knowing
# where to save the train data, test data and raw data
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # LINE FOR SOURCING DATA 
            df = pd.read_csv('notebook\data\stud.csv')

            logging.info('Read the dataset as dataframe')

            # Makes directory of artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)            
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is complete")

            # Now return file paths for DATA_TRANSFORMATION.py to use
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
            


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()