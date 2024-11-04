import pandas as pd
from src.datascience.utils import logger
from sklearn.model_selection import train_test_split
import os
from src.datascience.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        # config should be an instance of DataTransformationConfig(the output of the previous cell)
        self.config = config

    def split_data(self) -> pd.DataFrame:
        """Splits the Data"""
        try:
            data = pd.read_csv(self.config.data_path)

            X = data.iloc[:, :-1]  # Features
            y = data.iloc[:, -1]   # Target variable

            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size= 0.2,)
            
            logger.info(f"Sucesfully splitted the data \nX_train dimensions:{X_train.shape}\nX_test dimensions:{X_test.shape}\ny_train dimensions:{y_train.shape}\ny_test dimensions:{y_test.shape}   ")

            return X_train, X_test, y_train, y_test
        
        except Exception as e:
            logger.exception(f"Exception during data_splitting \n Exception:{e}")
            raise e
    
    def save_splits(self, X_train, X_test, y_train, y_test):
        try:
            X_train.to_csv(os.path.join(self.config.root_dir, "X_train.csv"), index = False)
            X_test.to_csv(os.path.join(self.config.root_dir, "X_test.csv"), index = False)
            y_train.to_csv(os.path.join(self.config.root_dir, "y_train.csv"), index = False)
            y_test.to_csv(os.path.join(self.config.root_dir, "y_test.csv"), index = False)

            logger.info(f"Sucesfully Saved the splits to: {self.config.root_dir}")

        except Exception as e:
            logger.exception(f"Exception during data_splitting \n Exception:{e}")
            raise e