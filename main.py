from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.utils import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


logger.info("Welcome to our Custom Logging Functionality")


# entry_point

STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    DataIngestionTrainingPipeline(STAGE_NAME).initiate_data_ingestion()





