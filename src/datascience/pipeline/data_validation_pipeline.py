from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience.utils import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self, stage_name):
        self.stage_name = stage_name

    def initiate_data_validation(self):
        try:
            logger.info(f"{">"*10} Stage: {self.stage_name} started {"<"*10}")

            # Get the variables from needed for the process
            data_validation_config = ConfigurationManager().get_data_validation_config()
            
            # Instantiate the object for performing the Data Ingestion
            data_validation_object = DataValidation(data_validation_config)

            # Download and extract
            validate_column_names_status = data_validation_object.validate_column_names()
            validate_column_type_status = data_validation_object.validate_column_types()

            logger.info(f"{">"*10} Stage: {self.stage_name} completed {"<"*10}")


        except Exception as e:
            logger.error(f"Error during data_validation. Error {e}")
            raise(e)