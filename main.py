from src.datascience.config.configuration import ConfigurationManager
from src.datascience.utils import logger

from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.components.data_validation import DataValidation
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

# entry_point

if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion Stage"
    DataIngestionTrainingPipeline(STAGE_NAME).initiate_data_ingestion()

    STAGE_NAME = "Data Validation Stage"
    DataValidationTrainingPipeline(STAGE_NAME).initiate_data_validation()




