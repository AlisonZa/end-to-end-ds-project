import urllib.request as request
import pandas as pd
from src.datascience.utils import logger
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.base import RegressorMixin
from sklearn.linear_model import ElasticNet
import joblib
import os
from src.datascience.config.configuration import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_training_data(self) -> tuple[np.ndarray, np.ndarray]:
        """Loads and converts training and test data to NumPy arrays."""
        
        # Load the data:
        X_train = pd.read_csv(self.config.X_train_data_path)
        y_train = pd.read_csv(self.config.y_train_data_path)

        # Convert to np.arrays
        X_train = X_train.values
        y_train = y_train.values

        return X_train, y_train        

    def train_model(self, X_train, y_train) -> RegressorMixin:
        """Trains the model"""
        try:
            # Train the model
            hyperparams = {
                "alpha":self.config.alpha,
                "l1_ratio":self.config.l1_ratio
            }
            elastic_net = ElasticNet(random_state= 42, **hyperparams)
            elastic_net.fit(X_train, y_train)
            logger.info(f"Sucesfully trained the model")
            return elastic_net

        except Exception as e:
            logger.exception(f"Exception during model_training \n Exception:{e}")
            raise e
    
    def save_model(self, model: RegressorMixin):
        try:
            # Ensure the save directory exists
            os.makedirs(self.config.root_dir, exist_ok=True)

            # Define the complete file path
            file_path = os.path.join(self.config.root_dir, self.config.model_name)

            # Save the model
            joblib.dump(model, file_path)
            logger.info(f"Sucesfully Saved the model to: {self.config.root_dir}")

        except Exception as e:
            logger.exception(f"Exception during model_saving \n Exception:{e}")
            raise e