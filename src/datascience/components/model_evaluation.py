import urllib.parse as urlparse
import pandas as pd
import numpy as np
from sklearn.base import RegressorMixin
import joblib
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.datascience.config.configuration import ModelEvaluationConfig
import os
from src.datascience.utils.commons import save_json
from pathlib import Path

                            # is being marked as decrapted, but it is not.

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        # config should be an instance of DataTransformationConfig(the output of the previous cell)
        self.config = config

        # model_evaluation_config = ModelEvaluationConfig(
        #     # config.yaml
        #     root_dir= config.root_dir,
        #     X_test_data_path= config.X_test_data_path, 
        #     y_test_data_path= config.y_test_data_path,
        #     model_path= config.model_path,
        #     metric_file_name= config.metric_file_name,

        #     #params.yaml
        #     params= params

    def load_test_data(self) -> tuple[np.ndarray, np.ndarray]:
        """Loads and converts training and test data to NumPy arrays."""
        
        # Load the data:
        X_test = pd.read_csv(self.config.X_test_data_path)
        y_test = pd.read_csv(self.config.y_test_data_path)

        # Convert to np.arrays
        X_test = X_test.values
        y_test = y_test.values

        return X_test, y_test        

    def load_model(self):
        model = joblib.load(self.config.model_path)
        return model
    
    def predict(self,model, X_test):
        pred = model.predict(X_test)    
        return pred

    def eval_metrics(self, y_test, pred):
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        mae = mean_absolute_error(y_test, pred)
        r2 = r2_score(y_test, pred)
        return rmse, mae, r2    

    def log_to_mlflow(self, model, y_test, pred) -> RegressorMixin:
        
        # environ settings:
        mlflow.set_registry_uri(os.getenv("MLFLOW_TRACKING_URI"))
        tracking_url_type_store = urlparse.urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            (rmse, mae, r2) = self.eval_metrics(y_test, pred)

            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Logging to the server:
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            # Logging the parameters
            mlflow.log_params(self.config.all_params)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
        mlflow.end_run()