
from src.datascience.utils import logger
import sys
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["MLFLOW_TRACKING_URI"] = os.getenv("MLFLOW_TRACKING_URI")
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")


# entry_points/pipelines
if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion Stage"
    DataIngestionTrainingPipeline(STAGE_NAME).initiate_data_ingestion()

    STAGE_NAME = "Data Validation Stage"
    validate_column_names_status, validate_column_type_status  = DataValidationTrainingPipeline(STAGE_NAME).initiate_data_validation()

    if validate_column_names_status == False or validate_column_type_status == False:
        logger.error("Column types or names do not match the schema. Please check the Data Validation folder.")
        sys.exit(1) 

    STAGE_NAME = "Data Transformation Stage"
    DataTransformationTrainingPipeline(STAGE_NAME).initiate_data_transformation()
    
    STAGE_NAME = "Model Training Stage"
    ModelTrainingPipeline(STAGE_NAME).initiate_model_training()

    STAGE_NAME = "Model Evaluation Stage"
    ModelEvaluationPipeline(STAGE_NAME).initiate_model_evaluation()
    



