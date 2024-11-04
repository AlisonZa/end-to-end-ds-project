from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.utils import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self, stage_name):
        self.stage_name = stage_name

    def initiate_data_ingestion(self):
        try:
            logger.info(f"{">"*10} Stage: {self.stage_name} started {"<"*10}")

            # Get the variables from needed for the process
            data_ingestion_config = ConfigurationManager().get_data_ingestion_config()
            
            # Instantiate the object for performing the Data Ingestion
            data_ingestion_object = DataIngestion(data_ingestion_config)

            # Download and extract
            data_ingestion_object.download_file()
            data_ingestion_object.extract_zip_file()

            logger.info(f"{">"*10} Stage: {self.stage_name} completed {"<"*10}")

        except Exception as e:
            logger.exception(e)
            raise(e)