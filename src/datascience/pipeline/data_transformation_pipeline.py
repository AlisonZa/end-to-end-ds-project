from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.utils import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self, stage_name):
        self.stage_name = stage_name

    def initiate_data_transformation(self):
        try:
            logger.info(f"{">"*10} Stage: {self.stage_name} started {"<"*10}")

            # Get the variables from needed for the process
            data_transformation_config = ConfigurationManager().get_data_transformation_config()
            
            # Instantiate the object for performing the Data Transformation
            data_transformation_object = DataTransformation(data_transformation_config)

            # Split and save
            X_train, X_test, y_train, y_test = data_transformation_object.split_data()
            data_transformation_object.save_splits(X_train, X_test, y_train, y_test)

            logger.info(f"{">"*10} Stage: {self.stage_name} completed {"<"*10}")


        except Exception as e:
            logger.error(f"Error during data_ingestion. Error {e}")
            raise e